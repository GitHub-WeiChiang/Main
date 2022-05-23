__author__ = "ChiangWei"
__date__ = "2022/5/23"

import logging

logger = logging.getLogger(__name__)
logger.log(logging.DEBUG, 'DEBUG 訊息')
logger.log(logging.INFO, 'INFO 訊息')
logger.log(logging.WARNING, 'WARNING 訊息')
logger.log(logging.ERROR, 'ERROR 訊息')
logger.log(logging.CRITICAL, 'CRITICAL 訊息')
