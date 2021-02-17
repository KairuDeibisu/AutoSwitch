import netmiko


class Device:
    def __init__(self, **kwargs) -> None:

        kwargs.update({"default_enter": "\n",
                       "global_delay_factor": 2})

        self.conn = netmiko.ConnectHandler(**kwargs)

        self.output = ""

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.conn.disconnect()

    def load(self, filename):
        """
        load config from txt file
        """
        self.conn.enable()
        self.output = self.conn.send_config_from_file(filename)
        print(self.output)
