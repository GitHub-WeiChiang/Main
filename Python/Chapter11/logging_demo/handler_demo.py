__author__ = "ChiangWei"
__date__ = "2022/5/24"

import logging

logging.basicConfig(filename='open_home.log')

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler('errors.log'))

logger.log(logging.ERROR, 'ERROR 訊息')
