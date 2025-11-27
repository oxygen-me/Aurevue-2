# --- imports
from ui.tile.tile import TileWidget
from PySide6.QtWidgets import QLabel


# --- MusicTile class
class MusicTile(TileWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, tile_id="music", tile_type="music", **kwargs)

        # --- Layout
        layout = self.inner_layout

        # --- Content
        title = QLabel("Music")
        title.setStyleSheet("font-family: Segoe UI; font-size: 14px; font-weight: light;")
        layout.addWidget(title)

        layout.addStretch(1)