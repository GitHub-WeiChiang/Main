from loguru import logger

trace = logger.add('sample.log')

@logger.catch
def index_error(custom_list: list):
    custom_list[3]

if __name__ == '__main__':
    index_error([1, 2, 3])
