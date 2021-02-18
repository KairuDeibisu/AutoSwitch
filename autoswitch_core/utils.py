import pprint
from serial.tools import list_ports


def display_serial_ports():
    for port in list_ports.comports(True):
        print(port.device)
