from abc import ABC, abstractmethod


# 抽象類別
class Logger(ABC):
    def __init__(self, level):
        self.level = level
        self.next_logger = None

    def set_next_logger(self, next_logger):
        self.next_logger = next_logger

    def log_message(self, log_level, message):
        # 檢查是否為自己可處理的操作
        if log_level <= self.level:
            self.write(message)
        elif self.next_logger is not None:
            self.next_logger.log_message(log_level, message)

    @abstractmethod
    def write(self, message):
        pass


# 具象類別
class ErrorLogger(Logger):
    def __init__(self, level):
        super().__init__(level)

    # 實作抽象方法
    def write(self, message):
        print("Error: " + message)


# 具象類別
class DebugLogger(Logger):
    def __init__(self, level):
        super().__init__(level)

    # 實作抽象方法
    def write(self, message):
        print("Debug: " + message)


# 具象類別
class InfoLogger(Logger):
    def __init__(self, level):
        super().__init__(level)

    # 實作抽象方法
    def write(self, message):
        print("Info: " + message)


# 新增一個日誌級別 (無需修改既有代碼、擴展性強、符合開閉原則、無條件判斷)
class WarningLogger(Logger):
    def __init__(self, level):
        super().__init__(level)

    # 實作抽象方法
    def write(self, message):
        print("Warning: " + message)


if __name__ == "__main__":
    # 創建各個等級的日誌
    error_logger = ErrorLogger(1)
    debug_logger = DebugLogger(2)
    info_logger = InfoLogger(3)

    # 新增 (無需修改既有代碼、擴展性強、符合開閉原則、無條件判斷)
    warning_logger = WarningLogger(4)

    # 責任鏈
    error_logger.set_next_logger(debug_logger)
    debug_logger.set_next_logger(info_logger)

    # 新增 (無需修改既有代碼、擴展性強、符合開閉原則、無條件判斷)
    info_logger.set_next_logger(warning_logger)

    error_logger.log_message(1, "This is an error message")
    error_logger.log_message(2, "This is a debug message")
    error_logger.log_message(3, "This is an info message")
    error_logger.log_message(4, "This is an warning message")
