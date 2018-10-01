from wrappers.debug_controller import DebugController
from wrappers.gphoto_controller import GPhotoController
import argparse
import logging
import configparser

logging.basicConfig(filename='sequence.log',level=logging.DEBUG)

def main():
    """CLI script for running exposure sequences."""
    parser = argparse.ArgumentParser()

    parser.add_argument("count", type=int, help="number of exposures to take")
    parser.add_argument("duration", type=int, help="length of each exposure")
    parser.add_argument("spacing", type=int, help="time between exposures")

    args = parser.parse_args()

    logging.info("starting sequence with args: {}, {}, {}".format(args.count, args.duration, args.spacing))

    config = configparser.RawConfigParser()
    config.read('sequence.cfg')

    controller = None

    if config.getboolean('sequence', 'debug'):
        controller = DebugController()
    else:
        controller = GPhotoController()

    controller.run(args.count, args.duration, args.spacing)
    

if __name__ == "__main__":
    main()