# --- imports
from ui.tile.tile import TileWidget
from PySide6.QtWidgets import QLabel


# --- TopBar Class
class TopBar(TileWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, tile_id="topbar", tile_type="topbar", **kwargs)

        # ----- Layout -----
        layout = self.inner_layout

        # ----- Content -----
        title = QLabel("Aurevue v0.0.2")
        title.setStyleSheet("font-family: Segoe UI; font-size: 36px; font-weight: light;")
        layout.addWidget(title)

        layout.addStretch(1)