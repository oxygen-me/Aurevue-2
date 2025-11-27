"""Aurevue TileWidget Class;
These are the gears of the machine;
A machine may exist without them, but it will never work;
No Frontend/Backend mixing in this v2 model."""

# --- imports
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt

import core.math.metrics as _metrics

# ----------
# TileWidget Class
# ----------
class TileWidget(QWidget):

    # --- define faux gutter
    BUFFER = _metrics.GridConfig.t_buffer

    # --- define tile parameters
    def __init__(self, parent=None, tile_id=None, tile_type="generic",
                 grid_x=0, grid_y=0, grid_w=0, grid_h=0, metrics=None):

        super().__init__(parent)

        # --- store config
        self.tile_id = tile_id
        self.tile_type = tile_type
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.grid_w = grid_w
        self.grid_h = grid_h
        self.metrics = metrics

        # ----------
        # GEOMETRY
        # ----------

        w = h = 120 # << failsafe

        if metrics:
            print(f"[Tile] {self.tile_type} metrics ok", metrics)
            x, y, w, h = metrics.to_pixels(grid_x, grid_y, grid_w, grid_h)
            self.setGeometry(int(x), int(y), int(w), int(h))
        else:
            print(f"[Tile] {self.tile_type} missing metrics.")

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # ----------
        # Inner (Visible) Frame
        # ----------

        self. inner = QWidget(self)
        self.inner.setGeometry(
            self.BUFFER, self.BUFFER,
            w - (2 * self.BUFFER),
            h - (2 * self.BUFFER)
        )
        self.inner.setObjectName("inner")
        self.inner.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        # --- layout for content widgets (root layout for presets)
        self.inner_layout = QVBoxLayout(self.inner)
        self.inner_layout.setContentsMargins(10, 10, 10, 10)
        self.inner_layout.setSpacing(8)

        # --- temporary/fallback QSS sheet
        self.inner.setStyleSheet("""
            QWidget#inner {
                background-color: #ffffff;
                border-radius: 8px;
            }
            QLabel {
                background: transparent;
                border: none;
                color: #000000;
            }
        """)

        # todo: wire this up to shadow/hover/interaction backend later