from wrappers.base_controller import BaseController
import time

class DebugController(BaseController):
    def run(self, count, duration, spacing):
        for exposure in range(count):
            time.sleep(duration + spacing)
            self.log_progress(exposure)