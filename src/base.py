import os
from abc import ABC

import pandas as pd

from src import logger
from src.constant import constant
from src.utils import utils


class Data(object):
    data_type: str
    data_suffix: str

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def get_data(self):
        raise NotImplementedError

    def get_file_path(self):
        file_path = utils.get_data_path(constant.file_name.format(
            start_date=self.start_date, end_date=self.end_date, data_type=self.data_type, suffix=self.data_suffix)
        )
        return file_path

    def save(self, df):
        logger.info(f"开始缓存数据：{self.data_type}")
        file_path = self.get_file_path()
        df.to_csv(file_path, encoding="utf-8", sep=",")

    def get_df(self):
        file_path = self.get_file_path()
        if os.path.exists(file_path):
            logger.info(f"获取缓存：{file_path}")
            df = pd.read_csv(file_path)
        else:
            logger.info(f"开始拉取api数据：{self.data_type}")
            df = self.get_data()
            self.save(df)
        return df


class AggS(Data, ABC):
    data_type: str
    data_suffix: str

    def get_df(self):
        file_path = self.get_file_path()
        if os.path.exists(file_path):
            logger.info(f"获取缓存：{file_path}")
            df = pd.read_csv(file_path)
        else:
            logger.info(f"开始计算：{self.data_type}")
            df = self.run()
            self.save(df)
        return df

    def run(self) -> pd.DataFrame:
        raise NotImplementedError

    def load_require(self):
        _require = getattr(self, constant.require_key)
        for require_name, _require_plugin in _require.items():
            setattr(self, require_name, _require_plugin(self.start_date, self.end_date))
