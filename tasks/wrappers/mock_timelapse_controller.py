from wrappers.base_timelapse_controller import BaseTimelapseController
import time

class MockTimelapseController(BaseTimelapseController):
    def run(self, count, duration, spacing):
        for exposure in range(count):
            time.sleep(duration + spacing)
            print(exposure + 1)