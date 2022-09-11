import pandas as pd

from src.base import Draw
from src.constant import data_type
from src.parse import matlab
from src.register import require, register


@require(data_type.new_share_group_day)
@register
class NewShareDrawPlot(Draw):
    """
    新股发行市值-按天统计-折线图
    """
    data_type = data_type.new_share_group_day_plot_pic
    data_suffix = "png"

    def __init__(self, start_date, end_date):
        super().__init__(start_date, end_date)
        self.load_require()

    def get_data(self):
        df = self.new_share_group_day.get_ret()
        return df

    def run(self):
        df = self.get_data()
        df.sort_values(by=["ipo_date"])
        df['ipo_date'] = pd.to_datetime(df['ipo_date'], format="%Y%m%d")
        y_col_info = {
            "total_price": {"label": "total"},
            "market_total_price": {"label": "market_total"}
        }
        plt_plot = matlab.plot(df, "ipo_date", y_col_info, "day", "price", "day_total_price")
        return plt_plot


@require(data_type.new_share_group_day)
@register
class NewShareDrawBar(NewShareDrawPlot):
    """
    新股发行市值-按天统计-柱状图
    """
    data_type = data_type.new_share_group_day_bar_pic
    data_suffix = "png"

    def __init__(self, start_date, end_date):
        super().__init__(start_date, end_date)
        self.load_require()

    def run(self):
        df = self.get_data()
        df.sort_values(by=["ipo_date"])
        df['ipo_date'] = pd.to_datetime(df['ipo_date'], format="%Y%m%d")
        y_col_info = {
            "total_price": {"label": "total"},
            "market_total_price": {"label": "market_total"}
        }
        bar_plot = matlab.bar(df, "ipo_date", y_col_info, "day", "price", "day_total_price")
        return bar_plot
