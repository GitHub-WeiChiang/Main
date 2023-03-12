from loguru import logger

trace = logger.add('sample.log')

def index_error(custom_list: list):
    try:
        index_value = custom_list[3]
    except IndexError as  err:
        logger.exception(err)
        return


if __name__ == '__main__':
    index_error([1, 2, 3])
