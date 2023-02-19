from configparser import ConfigParser
import os


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Myconfig.ini")


class HandleConfig(ConfigParser):

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding="utf-8")


conf = HandleConfig(file)


if __name__ == '__main__':
    conf = HandleConfig("Myconfig.ini")
    print(conf.get("log", "name"))