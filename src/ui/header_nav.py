"""
Floating Pill Navigation & 1-Click Action Toolbar.
Provides instant access to prebuilt models, node creation, and export actions.
"""

from typing import Optional
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel, QPushButton, QWidget
)
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QFont


class HeaderNavToolbar(QFrame):
    """Floating pill navbar with 1-click decision action buttons."""

    action_triggered = Signal(str)  # action identifier

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setObjectName("headerNav")
        self._init_ui()

    def _init_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(14, 8, 14, 8)
        layout.setSpacing(10)

        # Brand Title & Pulsing Status Pill
        brand_row = QHBoxLayout()
        brand_row.setSpacing(8)

        brand_label = QLabel("DECISION GRAPH")
        brand_label.setObjectName("brandTitle")
        brand_row.addWidget(brand_label)

        status_pill = QLabel("● ENGINES READY")
        status_pill.setObjectName("statusPillGreen")
        brand_row.addWidget(status_pill)

        layout.addLayout(brand_row)
        layout.addSpacing(16)

        # 1-Click Action Buttons
        self.btn_anomaly = QPushButton("⚡ Anomaly Audit")
        self.btn_anomaly.setObjectName("primaryActionBtn")
        self.btn_anomaly.clicked.connect(lambda: self.action_triggered.emit("run_anomaly"))
        layout.addWidget(self.btn_anomaly)

        self.btn_elasticity = QPushButton("📈 Price Elasticity")
        self.btn_elasticity.setObjectName("emeraldActionBtn")
        self.btn_elasticity.clicked.connect(lambda: self.action_triggered.emit("run_elasticity"))
        layout.addWidget(self.btn_elasticity)

        self.btn_cfar = QPushButton("🎲 Cash Flow Stress")
        self.btn_cfar.setObjectName("indigoActionBtn")
        self.btn_cfar.clicked.connect(lambda: self.action_triggered.emit("run_cfar"))
        layout.addWidget(self.btn_cfar)

        self.btn_inventory = QPushButton("📦 Stock MEIO")
        self.btn_inventory.clicked.connect(lambda: self.action_triggered.emit("run_inventory"))
        layout.addWidget(self.btn_inventory)

        self.btn_network = QPushButton("🕸️ Network Fragility")
        self.btn_network.clicked.connect(lambda: self.action_triggered.emit("run_network"))
        layout.addWidget(self.btn_network)

        self.btn_swarm = QPushButton("🤖 Swarm Co-Pilot")
        self.btn_swarm.clicked.connect(lambda: self.action_triggered.emit("toggle_swarm"))
        layout.addWidget(self.btn_swarm)

        layout.addStretch()

        # Add Node & Export Buttons
        self.btn_add_node = QPushButton("➕ Add Node...")
        self.btn_add_node.clicked.connect(lambda: self.action_triggered.emit("add_node_dialog"))
        layout.addWidget(self.btn_add_node)

        self.btn_export = QPushButton("💾 Export Excel")
        self.btn_export.clicked.connect(lambda: self.action_triggered.emit("export_excel"))
        layout.addWidget(self.btn_export)
