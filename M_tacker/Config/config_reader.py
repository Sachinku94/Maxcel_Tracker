import configparser


def read_config(section, key):
    config = configparser.ConfigParser()
    config.read("M_Tracker/Config/config.ini")
    return config.get(section, key)
