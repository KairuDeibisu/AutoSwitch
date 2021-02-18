from autoswitch_core.utils import display_serial_ports
from autoswitch_core.command import *
from autoswitch_core.type import *

from serial.tools import list_ports
import argparse


def main(argv=None) -> int:
    """
    Handle Command line Arguments
    """
    parser = argparse.ArgumentParser(description="Configure Cisco Device")

    # Auth Group
    auth_group = parser.add_argument_group("Authentication")

    auth_group.add_argument(
        "-l", "--username", default="")

    auth_group.add_argument(
        "-p", "--password", default="")
    auth_group.add_argument(
        "-s", "--secret", default="")

    # Tools

    util_group = parser.add_argument_group("Tools")
    util_group.add_argument(
        "--list", help="lists avalible serial ports", action="store_true")

    # Required
    subparsers = parser.add_subparsers(
        dest="Conection", description="Conection")

    # Login with ssh
    ssh_parser = subparsers.add_parser(
        "ssh",  help="Connect to device using ssh")

    # Login with telnet
    telnet_parser = subparsers.add_parser(
        "telnet", help="Connect to device using telnet")

    # Login with serial

    serial_parser = subparsers.add_parser(
        "serial", help="Connect to device using serial cable")

    serial_parser.add_argument(
        "path", help="Config file path", default="", type=path)

    # Serial Specific Options
    serial_parser.add_argument(
        "--port", type=comport, help="COMPORT name", default=list_ports.comports()[0].device)

    serial_parser.add_argument(
        "--baudrate", type=int, default=9600, help="Speed bytes are transferred over serial")

    args = vars(parser.parse_args(argv))

    if args["Conection"] == "serial":
        serial(args)

    elif args["Conection"] == "telnet":
        telnet(args)

    elif args["Conection"] == "ssh":
        ssh(args)
    elif args["list"]:
        display_serial_ports()
    else:
        parser.print_help()
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
