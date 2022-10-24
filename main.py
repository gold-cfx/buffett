from src import logger
from src.constant import constant

from src.register import load_all_tools, root_parser

if __name__ == '__main__':
    load_all_tools()
    args = root_parser.parse_args()
    start_time = getattr(args, constant.start_date)
    end_date = getattr(args, constant.end_date)
    args.cmd_cls.main(start_time, end_date)
    # new_share_group_mouth.NewShareDraw('20210101', '20221231').get_ret()
    logger.info("success")
