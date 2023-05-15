# 抽象表達式接口
class Expression:
    # 抽象方法
    def interpret(self):
        pass

# 具體表達式: 實現 Expression (用於處理打印命令)
class PrintExpression(Expression):
    def __init__(self, message):
        # 成員變量: 儲存打印訊息
        self.message = message

    def interpret(self):
        # 打印
        print(self.message)

# 具體表達式: 實現 Expression (用於處理重複命令)
class RepeatExpression(Expression):
    def __init__(self, repeat_count, expression):
        # 成員變量: 重複次數
        self.repeat_count = repeat_count
        # 需重複執行的表達式
        self.expression = expression

    def interpret(self):
        # 執行
        for i in range(self.repeat_count):
            self.expression.interpret()

def main():
    command = "REPEAT 3 TIMES: PRINT Hello"

    # Split the command into words based on whitespace
    words = command.split(" ")

    # Handle the command
    if words[0].upper() == "REPEAT":
        repeat_count = int(words[1])

        # Create the TerminalExpression for PRINT
        print_expression = PrintExpression(words[4])

        # Create the NonTerminalExpression for REPEAT
        repeat_expression = RepeatExpression(repeat_count, print_expression)

        # Interpret the command
        repeat_expression.interpret()

if __name__ == "__main__":
    main()

# 當需要添加新的表達式時，較具有修改上的彈性。
