"""
details.so Light-Mode Editorial Stylesheet & Visual Theme.
Enforces museum-grade typography, warm paper backgrounds, sub-pixel borders,
and tactile spring-like buttons. Strictly zero dark AI slop or generic fonts.
"""

EDITORIAL_STYLE_QSS = """
/* Global Application Palette & Font Reset */
QWidget {
    background-color: #fbfbfb;
    color: #09090b;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Geist", "Inter", sans-serif;
    font-size: 13px;
    selection-background-color: #10b981;
    selection-color: #ffffff;
}

/* Main Window & Containers */
QMainWindow {
    background-color: #f4f4f5;
}

QFrame#cardFrame {
    background-color: #ffffff;
    border: 1px solid #e4e4e7;
    border-radius: 12px;
}

/* Floating Pill Toolbar & Header */
QFrame#headerNav {
    background-color: #ffffff;
    border: 1px solid #e4e4e7;
    border-radius: 20px;
    margin: 8px 12px 4px 12px;
}

/* High-Impact Tactile Buttons */
QPushButton {
    background-color: #ffffff;
    color: #09090b;
    border: 1px solid #e4e4e7;
    border-radius: 8px;
    padding: 6px 14px;
    font-weight: 500;
    font-size: 12px;
}

QPushButton:hover {
    background-color: #f4f4f5;
    border-color: #d4d4d8;
}

QPushButton:pressed {
    background-color: #e4e4e7;
    transform: scale(0.98);
}

QPushButton#primaryActionBtn {
    background-color: #09090b;
    color: #ffffff;
    border: 1px solid #09090b;
    font-weight: 600;
}

QPushButton#primaryActionBtn:hover {
    background-color: #27272a;
    border-color: #27272a;
}

QPushButton#primaryActionBtn:pressed {
    background-color: #3f3f46;
}

QPushButton#emeraldActionBtn {
    background-color: #ecfdf5;
    color: #065f46;
    border: 1px solid #a7f3d0;
    font-weight: 600;
}

QPushButton#emeraldActionBtn:hover {
    background-color: #d1fae5;
    border-color: #6ee7b7;
}

QPushButton#indigoActionBtn {
    background-color: #eef2ff;
    color: #3730a3;
    border: 1px solid #c7d2fe;
    font-weight: 600;
}

QPushButton#indigoActionBtn:hover {
    background-color: #e0e7ff;
    border-color: #a5b4fc;
}

/* Info Tooltip Hover Badge (i) */
QPushButton#infoHoverBtn {
    background-color: #f4f4f5;
    color: #71717a;
    border: 1px solid #e4e4e7;
    border-radius: 9px;
    font-family: "JetBrains Mono", Consolas, monospace;
    font-size: 11px;
    font-weight: 700;
    padding: 0px;
    min-width: 18px;
    max-width: 18px;
    min-height: 18px;
    max-height: 18px;
}

QPushButton#infoHoverBtn:hover {
    background-color: #09090b;
    color: #ffffff;
    border-color: #09090b;
}

/* Virtualized Spreadsheet QTableView */
QTableView {
    background-color: #ffffff;
    border: 1px solid #e4e4e7;
    border-radius: 8px;
    gridline-color: #f4f4f5;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 12px;
    alternate-background-color: #fafafa;
}

QTableView::item {
    padding: 5px 8px;
    border-bottom: 1px solid #f4f4f5;
}

QTableView::item:selected {
    background-color: #e0e7ff;
    color: #1e1b4b;
}

QHeaderView::section {
    background-color: #fbfbfb;
    color: #52525b;
    border: none;
    border-right: 1px solid #e4e4e7;
    border-bottom: 1px solid #e4e4e7;
    padding: 7px 10px;
    font-weight: 600;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

QHeaderView::section:hover {
    background-color: #f4f4f5;
    color: #09090b;
}

/* Scrollbars */
QScrollBar:vertical {
    border: none;
    background: #f4f4f5;
    width: 8px;
    border-radius: 4px;
}

QScrollBar::handle:vertical {
    background: #d4d4d8;
    min-height: 25px;
    border-radius: 4px;
}

QScrollBar::handle:vertical:hover {
    background: #a1a1aa;
}

QScrollBar:horizontal {
    border: none;
    background: #f4f4f5;
    height: 8px;
    border-radius: 4px;
}

QScrollBar::handle:horizontal {
    background: #d4d4d8;
    min-width: 25px;
    border-radius: 4px;
}

/* Tabs & Splitters */
QTabWidget::pane {
    border: 1px solid #e4e4e7;
    border-radius: 8px;
    background: #ffffff;
}

QTabBar::tab {
    background: #f4f4f5;
    color: #71717a;
    border: 1px solid #e4e4e7;
    border-bottom: none;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    padding: 6px 14px;
    margin-right: 2px;
    font-weight: 500;
}

QTabBar::tab:selected {
    background: #ffffff;
    color: #09090b;
    font-weight: 600;
}

QSplitter::handle {
    background-color: #e4e4e7;
}

QSplitter::handle:horizontal {
    width: 2px;
}

QSplitter::handle:vertical {
    height: 2px;
}

/* Status Chips & Badges */
QLabel#statusPillGreen {
    background-color: #ecfdf5;
    color: #065f46;
    border: 1px solid #a7f3d0;
    border-radius: 10px;
    padding: 3px 10px;
    font-size: 11px;
    font-weight: 600;
}

QLabel#brandTitle {
    font-size: 15px;
    font-weight: 800;
    color: #09090b;
    letter-spacing: -0.3px;
}
"""
