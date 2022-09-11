import os
from abc import ABC

import pandas as pd

from src import logger
from src.all_tools import get_data_path
from src.constant import constant
from src.utils import utils


class Data(object):
    data_type: str
    data_suffix: str

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def get_data(self) -> pd.DataFrame:
        """
        collect: 拉取远程数据
        operator: 获取需要计算的数据（上一层的数据）
        draw: 获取需要计算的数据（上一层的数据）
        """
        raise NotImplementedError

    def get_file_path(self) -> str:
        file_path = get_data_path(constant.file_name.format(
            start_date=self.start_date, end_date=self.end_date, data_type=self.data_type, suffix=self.data_suffix)
        )
        return file_path

    def save(self, df):
        logger.info(f"开始缓存数据：{self.data_type}")
        file_path = self.get_file_path()
        df.to_csv(file_path, encoding="utf-8", sep=",")

    def get_ret(self) -> pd.DataFrame:
        file_path = self.get_file_path()
        if os.path.exists(file_path):
            logger.info(f"获取缓存：{file_path}")
            df = pd.read_csv(file_path)
        else:
            logger.info(f"开始拉取api数据：{self.data_type}")
            df = self.get_data()
            self.save(df)
        return df


class Operator(Data, ABC):
    data_type: str
    data_suffix: str

    @classmethod
    def main(cls, start_date, end_date):
        op = cls(start_date, end_date)
        op.get_ret()

    def get_ret(self) -> pd.DataFrame:
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
        """
        编写计算逻辑
        """
        raise NotImplementedError

    def load_require(self):
        _require = getattr(self, constant.require_key)
        for require_name, _require_plugin in _require.items():
            setattr(self, require_name, _require_plugin(self.start_date, self.end_date))


class Draw(Operator, ABC):
    data_type: str
    data_suffix: str

    @classmethod
    def add_arguments(cls, sub_parse):
        parser = sub_parse.add_parser(cls.data_type, help=cls.__doc__)
        parser.set_defaults(cmd_cls=cls)
        parser.add_argument("-s", dest=constant.start_date, metavar=constant.start_date,
                            required=True, help="开始日期 样例：20221012")
        parser.add_argument("-e", dest=constant.end_date, metavar=constant.end_date,
                            required=True, help="结束日期 样例：20221012")
        return parser

    def run(self):
        """
        编写画图逻辑
        """
        raise NotImplementedError

    def save(self, plt_modul):
        logger.info(f"开始缓存数据：{self.data_type}")
        file_path = self.get_file_path()
        plt_modul.savefig(file_path)

    def get_ret(self):
        file_path = self.get_file_path()
        if os.path.exists(file_path):
            logger.info(f"获取缓存：{file_path}")
        else:
            logger.info(f"开始生成图片：{self.data_type}")
            plot = self.run()
            self.save(plot)
        utils.show(file_path)
