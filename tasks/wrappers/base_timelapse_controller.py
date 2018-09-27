from abc import ABCMeta, abstractmethod

import argparse

class BaseTimelapseController(metaclass=ABCMeta):
    @abstractmethod
    def run(self, count, duration, spacing):
        pass