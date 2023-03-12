from loguru import logger
import platform

trace= logger.add('sample.log', serialize=True)
logger.info(
    'If you are using Python {version}, prefer {feature} of course!',
    version=platform.python_version(),
    feature='f-strings'
)
