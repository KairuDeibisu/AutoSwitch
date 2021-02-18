"""
Networking Functions
"""

from autoswitch_core.device import Device
import os
import pprint


def load_with_ssh(args):
    """
    Configures device with ssh
    """
    pass


def load_with_telnet(args):
    """
    Configures device with telnet
    """
    pass


def load_with_serial(args: dict):
    """
    Configures device with serial
    """

    device_config = {
        "device_type": "cisco_ios_serial",
        "username": args["username"],
        "password": args["password"],
        "secret": args["secret"],
        "serial_settings": {"port": args["port"],
                            "baudrate": args["baudrate"]}
    }

    with Device(**device_config) as device:
        device.load(args["load"])
