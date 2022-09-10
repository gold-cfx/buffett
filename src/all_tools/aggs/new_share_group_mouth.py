from src.base import AggS
from src.constant import data_type
from src.parse.parse_data import add_col_by_func, add_col_by_group_sum
from src.register import require_plugin, register_plugin


@require_plugin(data_type.new_share_total)
@register_plugin
class Agg(AggS):
    data_type = data_type.new_share_group_mouth
    data_suffix = "csv"

    def __init__(self, start_date, end_date):
        super().__init__(start_date, end_date)
        self.load_require()

    def get_data(self):
        df = self.new_share_total.get_df()
        return df

    def run(self):
        df = self.get_data()
        df = add_col_by_func(df, "ipo_date", "ipo_mouth", lambda x: x[0:6], str)
        df = add_col_by_group_sum(df, "ipo_mouth", "total_price", "market_total_price")
        return df
