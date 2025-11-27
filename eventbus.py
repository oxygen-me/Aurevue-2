# ------------------------------
# AUREVUE EVENT ROUTER V2
# NOW WITH SPECIALIZED PORTS
# ------------------------------

# --- imports
from PySide6.QtCore import QObject, Signal

# --- shell level sector
class LowLevelBus(QObject):

    quitRequested = Signal()

mainBus = LowLevelBus()


# --- metrics sector
class MetricLevelBus(QObject):

    dpiDelivery = Signal(int, int, float)

metricBus = MetricLevelBus()