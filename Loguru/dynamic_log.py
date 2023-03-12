from loguru import logger

if __name__ == '__main__':
    trace = logger.add('sample.log')

    logger.error('This is error information')

    logger.remove(trace)
    
    logger.warning('This is warn information')
