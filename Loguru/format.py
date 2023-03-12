from loguru import logger

def format_log():
    trace = logger.add(
        'sample.log',
        format="{time:YYYY-MM-DD HH:mm:ss} {level} From {module}.{function} : {message}"
    )

    logger.warning('This is warn information')

if __name__ == '__main__':
    format_log()
