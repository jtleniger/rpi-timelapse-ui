from abc import ABCMeta, abstractmethod

import argparse

class BaseTimelapseController(metaclass=ABCMeta):
    @abstractmethod
    def run(self, count, duration, spacing):
        pass

    def log_progress(self, exposure):
        f = open('progress_temp', 'w')

        f.write(str(exposure))

        f.close()