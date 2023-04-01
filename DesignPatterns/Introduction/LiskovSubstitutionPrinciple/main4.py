class Calculator:
    def calculate(self, n1, n2):
        return n1 + n2

# 子類別繼承於父類別
class SuperCalculator(Calculator):
    def substract(self, n1, n2):
        return n1 - n2

c = Calculator()
sc = SuperCalculator()
# 在這裡可以把父類別替換為子類別
print(c.calculate(1, 2))
print(sc.calculate(1, 2))
# 在這裡不可以把子類別替換為父類別
print(sc.substract(10, 5))
# Error
# c.substract(10, 5)
