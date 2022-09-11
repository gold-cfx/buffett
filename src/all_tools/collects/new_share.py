from pandas import DataFrame

from src import logger
from src.all_tools.collects import pro
from src.base import Data
from src.constant import data_type
from src.register import register
from src.utils.key_map import KeyMap

new_share_key_map = {
    "keys": ["ts_code", "sub_code", "name", "ipo_date", "issue_date", "amount",
             "market_amount", "price", "pe", "limit_amount", "funds", "ballot"],
    "zh_keys": ["TS股票代码", "申购代码", "名称", "上网发行日期", "上市日期", "发行总量（万股）",
                "上网发行总量（万股）", "发行价格", "市盈率", "个人申购上限（万股）", "募集资金（亿元）", "中签率"],
    "value_type": [str, str, str, str, str, float, float, float, float, float, float],
}


def key_map():
    return KeyMap(new_share_key_map)


@register
class NewShareData(Data):
    data_type = data_type.new_share
    data_suffix = "csv"

    def __init__(self, start_date, end_date):
        super().__init__(start_date, end_date)

    def get_data(self, ):
        logger.info(f"开始拉取{self.data_type}数据，时间{self.start_date}-{self.end_date}")
        df: DataFrame = pro.new_share(start_date=self.start_date, end_date=self.end_date)
        return df


if __name__ == '__main__':
    a = NewShareData('20210101', '20221231')
    a.get_data()
