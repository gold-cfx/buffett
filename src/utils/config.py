import os.path
from configparser import ConfigParser


class Section:
    def __init__(self, name):
        self.name = name


class Config:

    def __init__(self, config_path):
        self.config_path = config_path
        self._parser = ConfigParser()
        if not os.path.exists(config_path):
            raise ValueError(f"{config_path}不存在")
        self._parser.read(config_path)

    def parse(self, value_type_map):
        for section, value_dict in self._parser.items():
            for key, value in value_dict.items():
                conf_key = f"{section}.{key}"
                value = value_type_map[conf_key](value)
                self.set_config(section, key, value)
        return self

    def set_config(self, section, key, value):
        if section not in self.__dict__:
            self.__dict__[section] = Section(section)
        _section: Section = self.__dict__[section]
        setattr(_section, key, value)
