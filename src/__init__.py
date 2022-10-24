import os

from src.utils.config import Config
from src.utils.logger import Logger

logger = Logger()

project_dir = os.path.dirname(os.path.dirname(__file__))
config_path = os.path.join(project_dir, "etc/buffett.conf")
config_dir = os.path.abspath(os.path.dirname(config_path))

config_map = {
    "token.ts_token": str,
    "dir.data_dir": lambda x: os.path.abspath(os.path.join(config_dir, x)),
    "pic.size_width": int,
    "pic.size_height": int
}

config = Config(config_path).parse(config_map)
