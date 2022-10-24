import datetime
import os

from src import config
from src.utils.utils import get_path, get_dir


def get_data_dir():
    today = datetime.date.today().strftime("%Y-%m-%d")
    return get_dir(os.path.join(config.dir.data_dir, today))


def get_data_path(file_name):
    return get_path(get_data_dir(), file_name)
