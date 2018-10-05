from subprocess import Popen
import math

class SequenceHandler(object):
    def __init__(self):
        self.proc = None
        self.count = 0
    
    def start(self, count, duration, spacing):
        """Starts a new tasks/sequence.py process if one isn't already running."""

        if self.proc is not None and self.proc.poll() is not None:
            self.proc = None

        if self.proc is not None:
            raise Exception("Timelapse is already running. pid={}".format(self.proc.pid))

        self.count = count
        
        self.proc = Popen(['python3', './tasks/sequence.py', str(self.count), str(duration), str(spacing)])

    def progress(self):
        """Returns the percent progress for the running sequence"""

        if self.proc is None or self.proc.poll() is not None:
            return 100

        f = open('progress_temp', 'r')

        exposure = int(f.readline())

        f.close()

        return int(math.ceil(((1.0 * exposure) / self.count) * 100))

    def is_running(self):
        """Returns true if a sequence is running."""

        if self.proc is None or self.proc.poll() is not None:
            return False

        return True

    def stop(self):
        """Stops the sequence if one is running."""
        if self.proc is not None:
            self.proc.kill()
            self.proc = None