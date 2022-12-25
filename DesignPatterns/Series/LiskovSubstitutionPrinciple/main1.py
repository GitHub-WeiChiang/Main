import abc

class Calculator:
    # 這是一個抽象方法，應該要被覆寫
    @abc.abstractmethod
    def test():
        raise NotImplementedError
    
    # 這是一個非抽象方法，不應該被覆寫
    def calculate(self, n1, n2):
        return n1 + n2

class SuperCalculator(Calculator):
    # 覆寫抽象方法
    def test():
        print('super test')

    # 不應該這麼做！
    def calculate(self, n1, n2):
        # It's dangerous to overwrite non-abstract methods
        return n1 - n2

c = Calculator()
print(c.calculate(1, 3))
sc = SuperCalculator()
print(sc.calculate(1, 3))
