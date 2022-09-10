from src.base import AggS
from src.constant import data_type
from src.parse.parse_data import add_col_by_multiplication
from src.register import require_plugin, register_plugin


@require_plugin(data_type.new_share)
@register_plugin
class Agg(AggS):
    data_type = data_type.new_share_total
    data_suffix = "csv"

    def __init__(self, start_date, end_date):
        super().__init__(start_date, end_date)
        self.load_require()

    def get_data(self):
        df = self.new_share.get_df()
        return df

    def run(self):
        df = self.get_data()
        df = add_col_by_multiplication(df, "market_amount", "price", "market_total_price")
        df = add_col_by_multiplication(df, "amount", "price", "total_price")
        return df
