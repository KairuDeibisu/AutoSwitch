from setuptools import setup


setup(
    name="autoswitch",
    version="1.0",
    description="Configure Cisco devices",
    author="Kyle Davis",
    author_email="contact@kyledavis.dev",
    url="https://kyledavis.dev",
    packages=["autoswitch"],
    install_requires=[
        "netmiko"
    ]
)
