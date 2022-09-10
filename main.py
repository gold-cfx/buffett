from src import logger

from src.all_tools.aggs import new_share_group_mouth
from src.register import load_all_driver

if __name__ == '__main__':
    load_all_driver()
    new_share_group_mouth.Agg('20210101', '20221231').get_df()
    logger.info("success")
