from autoswitch_core.command import *
from autoswitch_core.type import *

from serial.tools import list_ports
import argparse


def get_serial_parser(subparsers):
    # Login with serial
    serial_parser = subparsers.add_parser(
        "serial", help="Connect using serial cable")

    """SERIAL PARSER"""

    # Optional
    serial_parser.add_argument(
        "--port",  help="COMPORT name", default=list_ports.comports()[0].device)

    serial_parser.add_argument(
        "--baudrate", type=int, default=9600, help="Speed data is transfer over serial")

    return serial_parser


def get_auth_group(parser):
    # Auth Group
    auth_group = parser.add_argument_group("Authentication")

    auth_group.add_argument(
        "-l", "--username", default="")

    auth_group.add_argument(
        "-p", "--password", default="")
    auth_group.add_argument(
        "-s", "--secret", default="")

    return auth_group


def main(argv=None) -> int:

    parser = argparse.ArgumentParser(
        description="Configure Cisco Device")

    auth_group = get_auth_group(parser)

    # Required
    subparsers = parser.add_subparsers(
        dest="Conection Type", description="Conection Type")
    subparsers.required = True

    parser.add_argument(
        "path", help="Config file path", default="", type=path)

    # Login with ssh
    ssh_parser = subparsers.add_parser("ssh",  help="Connect using ssh")

    # Login with telnet
    telnet_parser = subparsers.add_parser(
        "telnet", help="Connect using telnet")

    serial_parser = get_serial_parser(subparsers)

    args = vars(parser.parse_args(argv))

    if args["Conection Type"] == "serial":
        serial(args)

    if args["Conection Type"] == "telnet":
        telnet(args)

    if args["Conection Type"] == "ssh":
        ssh(args)

    return 0


if __name__ == "__main__":
    exit(main())
