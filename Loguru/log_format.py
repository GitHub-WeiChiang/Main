import platform
from loguru import logger

if __name__ == '__main__':
    trace = logger.add('./sample.log')

    logger.info(
        'If you are using Python {version}, prefer {feature} of course!',
        version=platform.python_version(),
        feature='f-strings'
    )
