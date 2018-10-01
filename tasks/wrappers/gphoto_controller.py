from base_controller import BaseController
import subprocess
import logging

class GPhotoController(BaseController):
    CMD = 'gphoto2'
    CFG_FLAG = '--set-config'
    SHUTTER_SPEEDS = {
        0.0002: "0",
        0.0003: "1",
        0.0004: "2",
        0.0005: "3",
        0.0006: "4",
        0.0008: "5",
        0.0010: "6",
        0.0012: "7",
        0.0015: "8",
        0.0020: "9",
        0.0025: "10",
        0.0031: "11",
        0.0040: "12",
        0.0050: "13",
        0.0062: "14",
        0.0080: "15",
        0.0100: "16",
        0.0125: "17",
        0.0166: "18",
        0.0200: "19",
        0.0250: "20",
        0.0333: "21",
        0.0400: "22",
        0.0500: "23",
        0.0666: "24",
        0.0769: "25",
        0.1000: "26",
        0.1250: "27",
        0.1666: "28",
        0.2000: "29",
        0.2500: "30",
        0.3333: "31",
        0.4000: "32",
        0.5000: "33",
        0.6250: "34",
        0.7692: "35",
        1.0000: "36",
        1.3000: "37",
        1.6000: "38",
        2.0000: "39",
        2.5000: "40",
        3.0000: "41",
        4.0000: "42",
        5.0000: "43",
        6.0000: "44",
        8.0000: "45",
        10.0000: "46",
        13.0000: "47",
        15.0000: "48",
        20.0000: "49",
        25.0000: "50",
        30.0000: "51"
    }

    def __init__(self):
        exit_code = subprocess.call([GPhotoController.CMD, GPhotoController.CFG_FLAG, 'capturetarget=1'])

        if exit_code != 0:
            raise Exception('Could not set SD capture.')

    def run(self, count, duration, spacing):
        if (duration > 30):
            self.run_bulb(count, duration, spacing)
        else:
            self.run_timed(count, duration, spacing)

    def run_bulb(self, count, duration, spacing):
        exit_code = subprocess.call([GPhotoController.CMD, GPhotoController.CFG_FLAG, 'shutterspeed=52'])

        if exit_code != 0:
            raise Exception('Could not set shutterspeed to Bulb.')

        for exposure in range(count):
            try:
                exit_code = subprocess.call([
                    GPhotoController.CMD,
                    GPhotoController.CFG_FLAG,
                    'bulb=1',
                    '--wait-event={}s'.format(duration),
                    GPhotoController.CFG_FLAG,
                    'bulb=0',
                    '--wait-event={}s'.format(spacing)
                ])
            except (ex):
                logging.exception("Exception capture photo: {}\nContinuing...".format(ex))
            finally:
                if exit_code != 0:
                    logging.error("Error capturing photo. Code: {}".format(exit_code))

            self.log_progress(exposure)
    
    def run_timed(self, count, duration, spacing):
        duration = float(duration)

        if duration not in GPhotoController.SHUTTER_SPEEDS:
            raise Exception("Invalid shutter speed: {}".format(duration))

        exit_code = subprocess.call([
            GPhotoController.CMD,
            GPhotoController.CFG_FLAG,
            'shutterspeed={}'.format(GPhotoController.SHUTTER_SPEEDS[duration])
        ])

        if exit_code != 0:
            raise Exception('Could not set shutterspeed to {}'.format(duration))

        for exposure in range(count):
            try:
                exit_code = subprocess.call([
                    GPhotoController.CMD,
                    GPhotoController.CFG_FLAG,
                    '--capture-image'
                ])
            except (ex):
                logging.exception("Exception capture photo: {}\nContinuing...".format(ex))
            finally:
                if exit_code != 0:
                    logging.error("Error capturing photo. Code: {}".format(exit_code))

            self.log_progress(exposure)