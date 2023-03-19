import os

from PIL import Image


class MyDict:
    def __init__(self):
        self.dict = {}

    def items(self):
        for k, v in self.dict.items():
            yield k, v

    def get(self, item):
        self.dict.get(item)

    def clean(self):
        del self.dict

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __getitem__(self, item):
        return self.dict[item]

    def __contains__(self, item):
        return item in self.dict


def run_once(func):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return func(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


def get_dir(data_dir):
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)
    return data_dir


def get_path(dir_path, name):
    dir_path = get_dir(dir_path)
    return os.path.join(dir_path, name)


def show(file_path):
    img = Image.open(file_path)
    img.show()
