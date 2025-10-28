import configparser


def read_config(section, key):
    config = configparser.ConfigParser()
    config.read("M_tacker/Config/config.ini")
    return config.get(section, key)
