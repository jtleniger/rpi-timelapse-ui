from abc import ABCMeta, abstractmethod

class BaseController(metaclass=ABCMeta):
    @abstractmethod
    def run(self, count, duration, spacing):
        pass

    def log_progress(self, exposure):
        """ Writes the current exposure number to a temp file. Note: exposure param is 0 indexed."""
        
        f = open('progress_temp', 'w')

        f.write(str(exposure + 1))

        f.close()