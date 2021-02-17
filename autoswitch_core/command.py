"""
This is a comand line utility to allow the user to configure a cisco router or switch
"""

from autoswitch_core.device import Device
import os


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


def serial(args):
    """
    Connect to device with serial
    """

    if not os.path.isfile(args.filepath):
        raise FileNotFoundError(args.filepath)

    device_config = {
        "device_type": "cisco_ios_serial",
        "username": args.username,
        "password": args.password,
        "secret": args.secret,
        "serial_settings": {"port": args.port,
                            "baudrate": args.baudrate}
    }

    with Device(**device_config) as device:
        device.load(args.filepath)
