# ------------------------------
# AUREVUE MAIN SCRIPT v2
# ------------------------------

# --- imports
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from PySide6.QtGui import QScreen

from bootstrap import Bootstrapper
from eventbus import mainBus, metricBus
from core.app import AppShell

# --- main function
def main():
    print("[Main] Start Registered")

    # --- create app
    app = QApplication(sys.argv)

    # --- try handshake
    print("[Main] Attempting handshake")

    boot = Bootstrapper()
    ready, config = boot.initialize()

    # --- parse response
    if not ready:
        raise RuntimeError("[Main] Bootstrap failed!")

    print("[Main] Handshake finalized")

    # --- detect user quit action
    mainBus.quitRequested.connect(app.quit)

    # --- create app
    window = AppShell(config=config)
    window.show()

    # --- run dpi calculation
    dpi_x, dpi_y, dpr = calculate_dpi(app)
    metricBus.dpiDelivery.emit(dpi_x, dpi_y, dpr)

    sys.exit(app.exec())

# --- dpi calculation at build
def calculate_dpi(app):

    primary_screen: QScreen = app.primaryScreen()
    dpi_x = primary_screen.logicalDotsPerInchX()
    dpi_y = primary_screen.logicalDotsPerInchY()
    dpr = primary_screen.devicePixelRatio()

    return dpi_x, dpi_y, dpr

# --- run function
if __name__ == "__main__":
    main()