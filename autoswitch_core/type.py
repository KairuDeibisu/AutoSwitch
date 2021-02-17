import os
import argparse


def path(string: str) -> str:
    """
    Argparse Type: File that exist
    """
    if not os.path.isfile(string):
        raise argparse.ArgumentTypeError(f"FileNotFoundError: {string}")

    return string
