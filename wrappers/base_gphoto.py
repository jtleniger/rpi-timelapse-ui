from abc import ABCMeta, abstractmethod

class BaseGPhoto(metaclass=ABCMeta):
    @abstractmethod
    def capture(duration):
        pass