__author__ = "ChiangWei"
__date__ = "2022/07/08"

from abc import ABCMeta, abstractmethod

class Expression(metaclass=ABCMeta):
    @abstractmethod
    def interpreter(self, var):
        pass

class VarExpression(Expression):
    def __init__(self, key):
        self.__key = key

    def interpreter(self, var):
        return var.get(self.__key)

class SymbolExpression(Expression):
    def __init__(self, left, right):
        self._left = left
        self._right = right

class AddExpression(SymbolExpression):
    def __init__(self, left, right):
        super().__init__(left, right)

    def interpreter(self, var):
        return self._left.interpreter(var) + self._right.interpreter(var)

class SubExpression(SymbolExpression):
    def __init__(self, left, right):
        super().__init__(left, right)

    def interpreter(self, var):
        return self._left.interpreter(var) - self._right.interpreter(var)

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class Calculator:
    def __init__(self, text):
        self.__expression = self.parserText(text)

    def parserText(self, expText):
        stack = Stack()
        left = right = None
        idx = 0
        while(idx < len(expText)):
            if (expText[idx] == '+'):
                left = stack.pop()
                idx += 1
                right = VarExpression(expText[idx])
                stack.push(AddExpression(left, right))
            elif(expText[idx] == '-'):
                left = stack.pop()
                idx += 1
                right = VarExpression(expText[idx])
                stack.push(SubExpression(left, right))
            # 運算元 (變數)
            else:
                stack.push(VarExpression(expText[idx]))
            idx += 1
        return stack.pop()

    def run(self, var):
        return self.__expression.interpreter(var)

def testCalculator():
    expStr = input("請輸入表達式: ");
    newExp, expressionMap = getMapValue(expStr)
    calculator = Calculator(newExp)    # 傳入拆解過的運算式
    result = calculator.run(expressionMap)    # 傳入運算元變數值對應
    print("運算結果為: " + expStr + " = " + str(result))

def getMapValue(expStr):
    preIdx = 0
    expressionMap = {}
    newExp = []
    for i in range(0, len(expStr)):
        if (expStr[i] == '+' or expStr[i] == '-'):
            key = expStr[preIdx:i]     # 運算元 (變數)
            key = key.strip()
            newExp.append(key)
            newExp.append(expStr[i])    # 運算子
            var = input("請輸入參數 " + key + " 的值: ")    # 運算元 (值)
            var = var.strip()
            expressionMap[key] = float(var)
            preIdx = i + 1

    key = expStr[preIdx:len(expStr)]
    key = key.strip()
    newExp.append(key)
    var = input("請輸入參數 " + key + " 的值: ");
    var = var.strip()
    expressionMap[key] = float(var)

    return newExp, expressionMap    # 拆解過的運算式、運算元變數值對應

testCalculator()
