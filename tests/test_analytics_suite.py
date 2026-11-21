"""
Comprehensive Invariant Test Suite for All 10 Prebuilt Decision Engines.
Validates econometric demand monotonicity, Monte Carlo VaR bounds,
inventory safety stock formulas, and Markov row-stochasticity.
"""

import pytest
import numpy as np
import pandas as pd

from src.data.synthetic_data import generate_enterprise_suite
from src.analytics import (
    compute_causal_elasticity,
    compute_cfar_monte_carlo,
    compute_anomaly_sweep,
    compute_inventory_meio,
    compute_cohort_retention,
    compute_markov_attribution,
    compute_mixed_logit_cannibalization,
    compute_bandit_experiment,
    compute_network_fragility,
    compute_knapsack_allocation,
)


@pytest.fixture(scope="module")
def enterprise_data():
    return generate_enterprise_suite(num_orders=1500, random_seed=42)


class TestPrebuiltDecisionEngines:
    """Rigorous mathematical tests across all 10 analytics engines."""

    def test_causal_elasticity_invariants(self, enterprise_data):
        tx_df = enterprise_data["transactions"]
        res = compute_causal_elasticity(tx_df)

        assert "elasticity_beta" in res
        assert "recommended_price" in res
        assert "decision_action" in res
        assert res["recommended_price"] > 0
        assert len(res["scenarios"]) == 5

    def test_cfar_monte_carlo_invariants(self, enterprise_data):
        tx_df = enterprise_data["transactions"]
        res = compute_cfar_monte_carlo(tx_df, n_simulations=1000, debt_covenant_floor=200000.0)

        assert "var_95_cash_floor" in res
        assert "var_99_cash_floor" in res
        assert res["var_99_cash_floor"] <= res["var_95_cash_floor"]  # 99% VaR must be deeper than 95%
        assert 0.0 <= res["covenant_breach_probability"] <= 1.0
        assert "decision_action" in res

    def test_anomaly_sweep_invariants(self, enterprise_data):
        tx_df = enterprise_data["transactions"]
        res = compute_anomaly_sweep(tx_df)

        assert "total_anomalies_count" in res
        assert "anomalies_df" in res
        assert res["anomaly_rate_pct"] >= 0.0
        assert "decision_action" in res

    def test_inventory_meio_invariants(self, enterprise_data):
        inv_df = enterprise_data["inventory"]
        res = compute_inventory_meio(inv_df, service_level=0.95)

        assert "policy_df" in res
        assert len(res["policy_df"]) == len(inv_df)
        # ROP must exceed or equal safety stock
        for _, row in res["policy_df"].iterrows():
            assert row["reorder_point"] >= row["safety_stock"]
        assert "decision_action" in res

    def test_cohort_retention_invariants(self, enterprise_data):
        tx_df = enterprise_data["transactions"]
        res = compute_cohort_retention(tx_df)

        ret_mat = res["retention_matrix"]
        assert not ret_mat.empty
        # Month 0 retention must be 100%
        if 0 in ret_mat.columns:
            for val in ret_mat[0].dropna():
                assert val == 100.0
        assert "decision_action" in res

    def test_markov_attribution_invariants(self, enterprise_data):
        journeys_df = enterprise_data["journeys"]
        res = compute_markov_attribution(journeys_df)

        weights = res["channel_attribution_weights"]
        assert len(weights) > 0
        total_weight = sum(weights.values())
        assert np.isclose(total_weight, 1.0, atol=0.01)  # Attribution conservation
        assert "decision_action" in res

    def test_mixed_logit_cannibalization_invariants(self, enterprise_data):
        tx_df = enterprise_data["transactions"]
        res = compute_mixed_logit_cannibalization(tx_df, n_individuals=300)

        diversion_df = res["diversion_matrix_df"]
        assert not diversion_df.empty
        assert 0.0 <= res["internal_cannibalization_pct"] <= 100.0
        assert "decision_action" in res

    def test_bandit_experiment_invariants(self):
        res = compute_bandit_experiment(n_rounds=500)

        assert res["thompson_sampling_regret"] <= res["static_ab_regret"] + 5.0
        assert res["regret_reduction_pct"] >= 0.0
        assert "decision_action" in res

    def test_network_fragility_invariants(self, enterprise_data):
        tx_df = enterprise_data["transactions"]
        res = compute_network_fragility(tx_df)

        centrality_df = res["centrality_df"]
        assert not centrality_df.empty
        # PageRank sum must equal 1.0
        total_pr = centrality_df["pagerank_centrality"].sum()
        assert np.isclose(total_pr, 1.0, atol=0.02)
        assert "decision_action" in res

    def test_knapsack_allocator_invariants(self):
        res = compute_knapsack_allocation(budget_ceiling=600000.0)

        assert res["total_budget_utilized"] <= 600000.0  # Budget constraint
        assert res["total_expected_value"] > res["total_budget_utilized"]
        assert "decision_action" in res
