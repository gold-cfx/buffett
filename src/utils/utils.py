import datetime
import os

from src.constant import constant


def get_dir(data_dir):
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)
    return data_dir


def get_data_dir():
    today = datetime.date.today().strftime("%Y-%m-%d")
    return get_dir(os.path.join(constant.data_dir, today))


def get_path(dir_path, name):
    dir_path = get_dir(dir_path)
    return os.path.join(dir_path, name)


def get_data_path(file_name):
    return get_path(get_data_dir(), file_name)


class KeyMap:
    def __init__(self, map_dict):
        self.map_dict = map_dict
        self.keys_list = self.map_dict["keys"]
        self.zh_keys_list = self.map_dict["zh_keys"]
        self.value_type_list = self.map_dict["value_type"]
        self.map_key = {}
        self.map_zh_key = {}
        self.parse()

    def parse(self):
        for index, key in enumerate(self.keys_list):
            zh_key = self.zh_keys_list[index]
            value_type = self.value_type_list[index]
            self.map_key[key] = {
                "zh_key": zh_key,
                "type": value_type,
                "index": index
            }
            self.map_zh_key[zh_key] = {
                "key": key,
                "type": value_type,
                "index": index
            }

    def get_useful_key(self):
        return [key for key in self.keys_list if str(key).strip() != ""]
