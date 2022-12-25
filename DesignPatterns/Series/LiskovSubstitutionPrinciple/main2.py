class Calculator:
    def calculate(self, n1, n2):
        return n1 + n2

# 子類別應根據需求擴充所需之方法功能
class SuperCalculator(Calculator):
    sum = 10

    def add(self, n1, n2):
        return n1 + n2

    def substract(self, n1, n2):
        return n1 - n2

sc = SuperCalculator()
print(sc.substract(10, 5))
