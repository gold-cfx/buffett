import tushare as ts
from src import logger
from src import config
from src.constant.constant import ts_token

token = ts_token or config.token.ts_token
logger.once("using ts_token: %s", token)
pro = ts.pro_api(token)
