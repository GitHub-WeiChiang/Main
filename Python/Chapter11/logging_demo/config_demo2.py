__author__ = "ChiangWei"
__date__ = "2022/5/24"

import json
import logging.config

with open('logconf.json') as config:
    LOGGING_CONFIG = json.load(config)
    logging.config.dictConfig(LOGGING_CONFIG)

# 建立logger
logger = logging.getLogger('simple_example')

# 應用程式的程式碼
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
