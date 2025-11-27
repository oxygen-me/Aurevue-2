"""
Aurevue AppShell v2:
This is the heart of Aurevue. A central hub for all widgets to reside.
Keep architecture clean and brief. We don't need to go back class-pass-hell.
"""

# --- imports
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
from PySide6.QtCore import Qt

import core.math.metrics as metrics
from ui.board.tileboard import BoardWidget


# --- create app class
class AppShell(QWidget):
    def __init__(self, config=None):
        super().__init__()

        # --- immediately store reference
        self.config = config
        cfg = self.config

        # --- parse config for window size
        window_cfg = cfg.get("window", {})
        cfg_w = window_cfg.get("width", 1260)
        cfg_h = window_cfg.get("height", 960)

        # --- initialize app
        print("[AppShell] Initializing shell...")

        self.setWindowTitle("Aurevue")
        self.resize(cfg_w, cfg_h)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        window_layout = QVBoxLayout()

        self._center_on_screen()

        # ----------
        # OUTER SHELL CREATION
        # ----------

        self.outer = QWidget(self)
        self.outer.setStyleSheet("background-color: #ffffff; border-radius: 16px;")
        self.outer.setObjectName("outer")

        # --- margin definition
        m = metrics.margins()
        main_margin = m["main"]
        inner_margin = m["inner"]

        # --- outer layout set up for board positioning
        outer_layout = QVBoxLayout()
        outer_layout.setContentsMargins(main_margin, main_margin, main_margin, main_margin)

        # ----------
        # CONTENT AREA CREATION
        # ----------

        self.board = BoardWidget(self.outer)
        self.board.setStyleSheet("background-color: #d0d3d5; border-radius: 12px")
        self.board.setObjectName("board")

        # ----------
        # LAYOUT INITIALIZATION
        # ----------

        outer_layout.addWidget(self.board, 1)
        window_layout.addWidget(self.outer)

        self.outer.setLayout(outer_layout)
        self.setLayout(window_layout)

    # --- center on screen function
    def _center_on_screen(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        window_geometry = self.frameGeometry()

        screen_center = screen_geometry.center()
        window_geometry.moveCenter(screen_center)
        self.move(window_geometry.topLeft())

