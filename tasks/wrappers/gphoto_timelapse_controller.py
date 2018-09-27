from base_timelapse_controller import *
import time

class GPhotoTimelapseController(BaseTimelapseController):
    def run(self, count, duration, spacing):
        raise NotImplementedError()