import logging
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__file__)

project_dir = os.path.dirname(os.path.dirname(__file__))
