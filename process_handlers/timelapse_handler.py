import subprocess
import logging

class TimelapseHandler(object):
    def __init__(self):
        self.proc = None
    
    def start(self, count, duration, spacing):
        if self.proc is not None:
            raise Exception("Timelapse is already running.")
        
        self.proc = subprocess.Popen(['python', '-m', 'tasks/timelapse.py', count, duration, spacing])

        logging.info("started timelapse.py, pid: {}".format(self.proc.pid))

    def status(self):
        if self.proc is None:
            return "Nothing running."
        
        if self.proc.poll() is None:
            return "Running timelapse."

        return "Nothing running."