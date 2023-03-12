from loguru import logger

if __name__ == '__main__':
    # 清除之前的設置
    logger.remove(handler_id=None)

    trace = logger.add('sample.log')

    logger.error('This is error information')
    logger.warning('This is warn information')
