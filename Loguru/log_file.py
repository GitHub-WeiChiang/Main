from loguru import logger

if __name__ == '__main__':
    logger.add(
        "./sample.log",
        rotation="500MB",
        encoding="utf-8",
        enqueue=True,
        retention="10 days"
    )

    logger.info('This is info information')
