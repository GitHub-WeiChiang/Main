# 計算機類別
class Calculator:
    def __init__(self):
        # 計算的結果
        self.result = 0

    # 加法
    def add(self, value):
        self.result += value

    # 減法
    def subtract(self, value):
        self.result -= value

    # 生成 Memento 對象: 保存當前計算結果
    def save(self):
        return self.CalculatorMemento(self.result)

    # 獲取 Memento 對象: 恢復之前計算的結果
    def restore(self, memento):
        self.result = memento.get_result()

    def get_result(self):
        return self.result

    # Memento 類別
    class CalculatorMemento:
        def __init__(self, result):
            # 保存某狀態的計算結果
            self.result = result

        # 訪問所保存的結果
        def get_result(self):
            return self.result


# 用於保存與恢復 Calculator 的類別
class CalculatorHistory:
    def __init__(self):
        self.history = []

    def save(self, calculator):
        # 保存當前計算機狀態
        self.history.append(calculator.save())

    def undo(self, calculator):
        if self.history:
            # 恢復到上一個保存的狀態
            calculator.restore(self.history.pop())


def main():
    # 計算機對象
    calculator = Calculator()
    # 計算機歷史狀態對象
    history = CalculatorHistory()

    # 計算操作
    calculator.add(5)
    calculator.subtract(3)

    # Save state
    history.save(calculator)
    # Output: Result: 2
    print("Result: " + str(calculator.get_result()))

    # 計算操作
    calculator.add(8)
    # Output: Result: 10
    print("Result: " + str(calculator.get_result()))

    # Undo to the previous saved state
    history.undo(calculator)
    # Output: Result: 2
    print("Result: " + str(calculator.get_result()))


if __name__ == "__main__":
    main()
