from subprocess import Popen
import logging

class TimelapseHandler(object):
    def __init__(self):
        self.proc = None
        self.count = 0
    
    def start(self, count, duration, spacing):
        """Starts a new tasks/timelapse.py process if one isn't already running."""

        if self.proc is not None and self.proc.poll() is not None:
            self.proc = None

        if self.proc is not None:
            raise Exception("Timelapse is already running. pid={}".format(self.proc.pid))

        self.count = count
        
        self.proc = Popen(['python', 'tasks/timelapse.py', str(self.count), str(duration), str(spacing)])

        logging.info("started timelapse.py, pid: {}".format(self.proc.pid))

    def progress(self):
        """Returns the percent progress for the running timelapse"""

        if self.proc is None or self.proc.poll() is not None:
            return 0

        f = open('progress_temp', 'r')

        exposure = int(f.readline())

        f.close()

        return round(((1.0 * exposure) / self.count) * 100)

    def is_running(self):
        """Returns true if a timelapse is running."""

        if self.proc is None or self.proc.poll() is not None:
            return False

        return True