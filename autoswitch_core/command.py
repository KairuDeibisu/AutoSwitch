"""
This is a comand line utility to allow the user to configure a cisco router or switch
"""

from autoswitch_core.device import Device
import os
import pprint


def ssh(args):
    """
    Connect to device with ssh
    """
    pass


def telnet(args):
    """
    Connect to device with telnet
    """
    pass


def serial(args: dict):
    """
    Connect to device with serial
    """

    device_config = {
        "device_type": "cisco_ios_serial",
        "username": args["username"],
        "password": args["password"],
        "secret": args["secret"],
        "serial_settings": {"port": args["port"],
                            "baudrate": args["baudrate"]}
    }

    pprint.pprint(device_config)

    # with Device(**device_config) as device:
    #     device.load(args.path)
