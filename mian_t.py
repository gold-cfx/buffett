from src import logger
from src.all_tools.draws import new_share_group_mouth

from src.register import load_all_tools

if __name__ == '__main__':
    load_all_tools()
    new_share_group_mouth.NewShareDrawPlot('20210101', '20221231').get_ret()
    logger.info("success")
