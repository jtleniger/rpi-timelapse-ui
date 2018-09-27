from wrappers.mock_timelapse_controller import MockTimelapseController
import argparse
import logging

logging.basicConfig(filename='timelapse.log',level=logging.DEBUG)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("count", type=int, help="number of exposures to take")
    parser.add_argument("duration", type=int, help="length of each exposure")
    parser.add_argument("spacing", type=int, help="time between exposures")

    args = parser.parse_args()

    logging.info("starting timelapse with args: {}, {}, {}".format(args.count, args.duration, args.spacing))

    controller = MockTimelapseController()

    controller.run(args.count, args.duration, args.spacing)
    

if __name__ == "__main__":
    main()