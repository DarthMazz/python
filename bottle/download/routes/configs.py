import configparser


class Configs:
    test = {}

    def load(environment):
        config_ini = configparser.ConfigParser()
        config_ini.read('config.ini', encoding='utf-8')
        Configs.test = config_ini[environment]