"""
Embedded Chart & Visualization Inspector.
Renders high-resolution interactive charts (demand curves, cash flow distributions,
anomaly scatter plots, and network graphs) inside native PySide6 widgets.
"""

from typing import Dict, Any, Optional
import numpy as np
import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

import matplotlib
matplotlib.use("QtAgg")
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class ChartInspectorWidget(QWidget):
    """Clean editorial chart inspector styled with details.so light palette."""

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        self.title_label = QLabel("Visual Analytics & Distribution")
        self.title_label.setFont(QFont("-apple-system, sans-serif", 12, QFont.Bold))
        self.title_label.setStyleSheet("color: #09090b;")
        layout.addWidget(self.title_label)

        # Matplotlib Figure with light editorial theme
        self.figure = Figure(figsize=(5, 3.5), facecolor="#ffffff", dpi=100)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setStyleSheet("border: 1px solid #e4e4e7; border-radius: 8px;")
        layout.addWidget(self.canvas)

        self.render_placeholder()

    def render_placeholder(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor("#fbfbfb")
        ax.text(
            0.5, 0.5,
            "Select an Analytics Node to view\ninteractive distribution curves",
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=10,
            color="#a1a1aa",
            transform=ax.transAxes
        )
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color("#e4e4e7")
        self.canvas.draw()

    def plot_elasticity(self, elasticity_res: Dict[str, Any]):
        self.figure.clear()
        self.title_label.setText("Causal Demand Curve & Pricing Scenarios")
        ax = self.figure.add_subplot(111)
        ax.set_facecolor("#ffffff")

        scenarios = elasticity_res.get("scenarios", [])
        if scenarios:
            prices = [s["price"] for s in scenarios]
            margins = [s["gross_margin"] for s in scenarios]
            volumes = [s["estimated_volume"] for s in scenarios]

            ax.plot(prices, margins, color="#10b981", marker="o", linewidth=2.2, label="Gross Margin ($)")
            ax.set_xlabel("Effective Price ($)", fontsize=9, color="#52525b")
            ax.set_ylabel("Expected Margin ($)", fontsize=9, color="#065f46")
            ax.tick_params(colors="#71717a", labelsize=8)
            ax.grid(True, linestyle="--", alpha=0.3, color="#d4d4d8")

            rec_p = elasticity_res.get("recommended_price", prices[len(prices)//2])
            ax.axvline(rec_p, color="#09090b", linestyle=":", linewidth=1.8, label=f"Optimal P* (${rec_p:.2f})")
            ax.legend(fontsize=8, frameon=True, facecolor="#fbfbfb", edgecolor="#e4e4e7")

        for spine in ax.spines.values():
            spine.set_color("#e4e4e7")
        self.figure.tight_layout()
        self.canvas.draw()

    def plot_cfar(self, cfar_res: Dict[str, Any]):
        self.figure.clear()
        self.title_label.setText("Cash Flow at Risk (5,000 Monte Carlo Paths)")
        ax = self.figure.add_subplot(111)
        ax.set_facecolor("#ffffff")

        mean_cf = cfar_res.get("mean_simulated_cash_flow", 600000.0)
        std_cf = cfar_res.get("std_dev_cash_flow", 150000.0)
        var_95 = cfar_res.get("var_95_cash_floor", 350000.0)
        covenant = cfar_res.get("debt_covenant_floor", 300000.0)

        # Synthetic normal density for visual representation
        x = np.linspace(mean_cf - 3.5 * std_cf, mean_cf + 3.5 * std_cf, 300)
        y = (1.0 / (std_cf * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean_cf) / std_cf) ** 2)

        ax.plot(x / 1000.0, y * 1000.0, color="#4f46e5", linewidth=2.0)
        # Fill tail loss area
        x_tail = x[x <= var_95]
        y_tail = y[x <= var_95]
        ax.fill_between(x_tail / 1000.0, y_tail * 1000.0, color="#ef4444", alpha=0.25, label="5% Tail Loss Zone")

        ax.axvline(var_95 / 1000.0, color="#dc2626", linestyle="--", linewidth=1.5, label=f"95% VaR (${var_95/1000:.0f}k)")
        ax.axvline(covenant / 1000.0, color="#09090b", linestyle="-.", linewidth=1.5, label=f"Covenant Floor (${covenant/1000:.0f}k)")

        ax.set_xlabel("Operating Cash Flow ($k)", fontsize=9, color="#52525b")
        ax.set_ylabel("Probability Density", fontsize=9, color="#52525b")
        ax.tick_params(colors="#71717a", labelsize=8)
        ax.grid(True, linestyle="--", alpha=0.3, color="#d4d4d8")
        ax.legend(fontsize=8, frameon=True, facecolor="#fbfbfb", edgecolor="#e4e4e7")

        for spine in ax.spines.values():
            spine.set_color("#e4e4e7")
        self.figure.tight_layout()
        self.canvas.draw()

    def plot_anomalies(self, df: pd.DataFrame, anomalies_df: pd.DataFrame):
        self.figure.clear()
        self.title_label.setText("Transaction Outliers & Margin Leaks")
        ax = self.figure.add_subplot(111)
        ax.set_facecolor("#ffffff")

        if "effective_price" in df.columns and "quantity" in df.columns:
            # Normal transactions
            ax.scatter(df["effective_price"], df["quantity"], color="#94a3b8", alpha=0.4, s=18, label="Compliant Orders")
            
            # Anomalous transactions
            if not anomalies_df.empty and "effective_price" in anomalies_df.columns:
                ax.scatter(
                    anomalies_df["effective_price"], anomalies_df["quantity"],
                    color="#ef4444", marker="x", s=50, linewidth=2, label=f"Anomalies ({len(anomalies_df)})"
                )

            ax.set_xlabel("Effective Price ($)", fontsize=9, color="#52525b")
            ax.set_ylabel("Quantity Ordered", fontsize=9, color="#52525b")
            ax.tick_params(colors="#71717a", labelsize=8)
            ax.grid(True, linestyle="--", alpha=0.3, color="#d4d4d8")
            ax.legend(fontsize=8, frameon=True, facecolor="#fbfbfb", edgecolor="#e4e4e7")

        for spine in ax.spines.values():
            spine.set_color("#e4e4e7")
        self.figure.tight_layout()
        self.canvas.draw()
