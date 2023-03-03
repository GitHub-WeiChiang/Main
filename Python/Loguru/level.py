from loguru import logger

trace = logger.add('sample.log', level='ERROR')

logger.info("This is info information")
logger.error("This is error information")
logger.critical("This is critical information")
