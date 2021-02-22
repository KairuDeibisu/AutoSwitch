"""
This is a comand line utility to allow the user to configure a cisco router or switch
Serves an entrypoint, parses user input, and handles user input

"""

from autoswitch_core.utils import *
from autoswitch_core.network import *
from autoswitch_core.type import *

from serial.tools import list_ports
import argparse


def get_auth_group(parser):
    group = parser.add_argument_group("Authentication")

    group.add_argument(
        "-l", "--username", default="")
    group.add_argument(
        "-p", "--password", default="")
    group.add_argument(
        "-s", "--secret", default="")

    return group


def input_handler(args):
    """
    Handles user input
    """

    if args["load"] != None:
        args["load_func"](args)

    if args["list_port"]:
        list_serial_ports()


def main(argv=None) -> int:
    """
    Handle Command line Arguments
    """
    parser = argparse.ArgumentParser(description="Configure Cisco Device")

    subparsers = parser.add_subparsers(
        dest="menu", description="The method used to conected to network device")

    # SSH Menu
    ssh_parser = subparsers.add_parser(
        "ssh",  help="Connect to device using ssh")
    ssh_parser.set_defaults(load_func=load_with_ssh)

    # Telnet Menu
    telnet_parser = subparsers.add_parser(
        "telnet", help="Connect to device using telnet")
    telnet_parser.set_defaults(load_func=load_with_telnet)

    # Serial Menu
    serial_parser = subparsers.add_parser(
        "serial", help="Connect to device using serial cable")
    serial_parser.set_defaults(load_func=load_with_serial)

    serial_auth_group = get_auth_group(serial_parser)

    serial_parser.add_argument(
        "--load", help="Load configuration file to device", default=None, type=path)

    # Tools
    serial_util_group = serial_parser.add_argument_group("Tools")
    serial_util_group.add_argument(
        "--list-port", help="lists avalible serial ports", action="store_true")

    # Serial Specific Options
    serial_parser.add_argument(
        "--port", type=comport, help="COMPORT name", default=list_ports.comports()[0].device)

    serial_parser.add_argument(
        "--baudrate", type=int, default=9600, help="Speed bytes are transferred over serial")

    args = parser.parse_args(argv)

    # Handle args

    if args.menu == None:

        parser.print_help()
        return 1

    input_handler(vars(args))

    return 0


if __name__ == "__main__":
    exit(main())
