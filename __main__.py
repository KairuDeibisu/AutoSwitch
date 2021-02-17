from autoswitch_core.command import *
from serial.tools import list_ports
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Load a configuration file on a cisco device")

    subparser = parser.add_subparsers()

    ssh_parser = subparser.add_parser("ssh")
    telnet_parser = subparser.add_parser("telnet")

    serial_parser = subparser.add_parser("serial")
    serial_parser.set_defaults(func=serial)
    serial_parser.add_argument(
        "filepath", help="configuration file path", default="")
    serial_parser.add_argument(
        "-P", "--port", default=list_ports.comports()[0].device, help="comport name (default: First available comport)")
    serial_parser.add_argument(
        "-b", "--baudrate", type=int, default=9600, help="speed data is transfer over serial (default: 9600)")
    serial_parser.add_argument(
        "-u", "--username", default="")
    serial_parser.add_argument(
        "-p", "--password", default="")
    serial_parser.add_argument(
        "-s", "--secret", default="")

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = main()
    args.func(args)
