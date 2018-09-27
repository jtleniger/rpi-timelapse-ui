from subprocess import PIPE, Popen
import logging

class TimelapseHandler(object):
    def __init__(self):
        self.proc = None
    
    def start(self, count, duration, spacing):
        if self.proc is not None:
            raise Exception("Timelapse is already running.")
        
        self.proc = Popen(['python', 'tasks/timelapse.py', count, duration, spacing], stdout=PIPE)

        logging.info("started timelapse.py, pid: {}".format(self.proc.pid))

    def count_done(self):
        if self.proc is None or self.proc.poll() is not None:
            return 0

        exposure = 0

        while True:
            line = self.proc.stdout.readline()

            if not line:
                break

            exposure = int(line)

        return exposure

    def status(self):
        if self.proc is None or self.proc.poll() is not None:
            return "Nothing running."

        return "Running timelapse."