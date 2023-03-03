from loguru import logger

if __name__ == '__main__':
    logger.add(
        "sample.log",
        filter=lambda record: record["level"].name == "ERROR"
    )

    logger.error('This is error information')
    logger.warning('This is warn information')
