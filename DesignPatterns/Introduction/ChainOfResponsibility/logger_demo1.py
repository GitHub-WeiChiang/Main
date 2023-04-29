class Logger:
    ERROR = 1
    DEBUG = 2
    INFO = 3

    def __init__(self, level):
        self.level = level

    def log_message(self, log_level, message):
        # 透過條件判斷決定日誌列印級別
        if log_level == self.ERROR and log_level <= self.level:
            print("Error: " + message)
        elif log_level == self.DEBUG and log_level <= self.level:
            print("Debug: " + message)
        elif log_level == self.INFO and log_level <= self.level:
            print("Info: " + message)


if __name__ == "__main__":
    logger = Logger(Logger.INFO)

    logger.log_message(Logger.ERROR, "This is an error message")
    logger.log_message(Logger.DEBUG, "This is a debug message")
    logger.log_message(Logger.INFO, "This is an info message")

# 如果日誌類型有增加，
# 條件判斷就需要隨之修改，
# 不但違反了開閉原則，
# 冗長的條件判斷也會讓程式碼過於臃腫且不易閱讀，
# 大量的縮排真的很醜。
