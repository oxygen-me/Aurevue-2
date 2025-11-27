# --- imports
from ui.tile.tile import TileWidget
from PySide6.QtWidgets import QLabel


# --- CommandTile class
class CommandTile(TileWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, tile_id="command", tile_type="command", **kwargs)

        # --- Layout
        layout = self.inner_layout

        # --- Content
        title = QLabel("Command")
        title.setStyleSheet("font-family: Segoe UI; font-size: 14px; font-weight: light;")
        layout.addWidget(title)

        layout.addStretch(1)