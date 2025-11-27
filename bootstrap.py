# ------------------------------
# AUREVUE BOOTSTRAPPER v3
# ------------------------------

# --- established required keys
required_keys = ["user", "window", "toolkit"]

# --- import required json module
import json

# --- create bootstrapper via class
class Bootstrapper:
    def __init__(self):
        self.ready = False
        self.data = {}

    # --- master bootstrap function
    def initialize(self):
        print("[Bootstrapper] Starting Checks")

        # --- try to fetch data
        try:
            self.data = self._load_cfg()
        except Exception as e:
            raise RuntimeError(e)

        # --- verify keys
        for key in required_keys:
            if key not in self.data:
                raise RuntimeError(f"[Bootstrapper] Missing required key in config: {key}")

        # --- debug completion and return parameters (to main)
        print("[Bootstrapper] Checks Completed")
        print(self.data)

        self.ready = True
        return self.ready, self.data

    # --- load config json and parse it
    def _load_cfg(self):
        with open("tools/config.json", "r") as file:
            cfg = json.load(file)
            return cfg