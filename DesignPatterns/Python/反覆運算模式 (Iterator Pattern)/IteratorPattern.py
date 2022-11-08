__author__ = "ChiangWei"
__date__ = "2022/05/29"

class Customer:
    def __init__(self, name):
        self.__name = name
        self.__num = 0
        self.__clinics = None

    def getName(self):
        return self.__name

    def register(self, system):
        system.pushCustomer(self)

    def setNum(self, num):
        self.__num = num

    def getNum(self):
        return self.__num

    def setClinic(self, clinic):
        self.__clinics = clinic

    def getClinic(self):
        return self.__clinics

class NumeralIterator:
    def __init__(self, data):
        self.__data = data
        self.__curIdx = -1

    def next(self):
        if self.__curIdx < len(self.__data) - 1:
            self.__curIdx += 1
            return True
        else:
            return False

    def current(self):
        return self.__data[self.__curIdx] if self.__curIdx < len(self.__data) and self.__curIdx >= 0 else None

class NumeralSystem:
    __clinics = ("1號分診室", "2號分診室", "3號分診室")

    def __init__(self, name):
        self.__customers = []
        self.__curNum = 0
        self.__name = name

    def pushCustomer(self, customer):
        customer.setNum(self.__curNum + 1)
        click = NumeralSystem.__clinics[self.__curNum % len(NumeralSystem.__clinics)]
        customer.setClinic(click)
        self.__curNum += 1
        self.__customers.append(customer)
        print("%s 您好！您已在%s成功掛號，序號：%04d，請耐心等待！" % (customer.getName(), self.__name, customer.getNum()))

    def getIterator(self):
        return NumeralIterator(self.__customers)

    def visit(self):
        for customer in self.__customers:
            print("下一位病人 %04d(%s) 請到 %s 就診。" % (customer.getNum(), customer.getName(), customer.getClinic()))

def testHospital():
    numeralSystem = NumeralSystem("掛號台")
    lily = Customer("Lily")
    lily.register(numeralSystem);
    pony = Customer("Pony")
    pony.register(numeralSystem)
    nick = Customer("Nick")
    nick.register(numeralSystem)
    tony = Customer("Tony")
    tony.register(numeralSystem)
    print()

    iterator = numeralSystem.getIterator()
    while(iterator.next()):
        customer = iterator.current()
        print("下一位病人 %04d(%s) 請到 %s 就診。" % (customer.getNum(), customer.getName(), customer.getClinic()))

# testHospital()

class BaseIterator:
    def __init__(self, data):
        self.__data = data
        self.toBegin()

    def toBegin(self):
        self.__curIdx = -1

    def toEnd(self):
        self.__curIdx = len(self.__data)

    def next(self):
        if self.__curIdx < len(self.__data) - 1:
            self.__curIdx += 1
            return True
        else:
            return False

    def previous(self):
        if self.__curIdx > 0:
            self.__curIdx -= 1
            return True
        else:
            return False

    def current(self):
        return self.__data[self.__curIdx] if self.__curIdx < len(self.__data) and self.__curIdx >= 0 else None

def testBaseIterator():
    print("從前往後遍歷:")
    iterator = BaseIterator(range(0, 10))
    while(iterator.next()):
        customer = iterator.current()
        print(customer, end="\t")
    print()

    print("從後往前遍歷:")
    iterator.toEnd()
    while (iterator.previous()):
        customer = iterator.current()
        print(customer, end="\t")

# testBaseIterator()

# 方法一: 使用 () 定義生成器
gen = (x * x for x in range(10))

# 方法二: 使用 yield 定義 generator 函數
def fibonacci(maxNum):
    a = b = 1
    for i in range(maxNum):
        yield a
        a, b = b, a + b

def testIterable():
    print("方法一，0 - 9 的平方數:")
    for e in gen:
        print(e, end="\t")
    print()

    print("方法二，斐波那契數列:")
    fib = fibonacci(10)
    for n in fib:
        print(n, end="\t")
    print()

    print("內置容器的 for 循環:")
    arr = [x * x for x in range(10)]
    for e in arr:
        print(e, end="\t")
    print()

    print()
    print(type(gen))
    print(type(fib))
    print(type(arr))

# testIterable()

from collections.abc import Iterable, Iterator

def testIsIterator():
    # 可以直接用於 for 迴圈地物件。
    print("是否為 Iterable 對象:")
    print(isinstance([], Iterable))
    print(isinstance({}, Iterable))
    print(isinstance((1, 2, 3), Iterable))
    print(isinstance(set([1, 2, 3]), Iterable))
    print(isinstance("string", Iterable))
    print(isinstance(gen, Iterable))
    print(isinstance(fibonacci(10), Iterable))

    # 可以被 next() 函式呼叫的物件。
    print("是否為 Iterator 對象:")
    print(isinstance([], Iterator))
    print(isinstance({}, Iterator))
    print(isinstance((1, 2, 3), Iterator))
    print(isinstance(set([1, 2, 3]), Iterator))
    print(isinstance("string", Iterator))
    print(isinstance(gen, Iterator))
    print(isinstance(fibonacci(10), Iterator))

# testIsIterator()

def testNextItem():
    print("將 Iterable 對象轉成 Iterator 對象:")
    l = [1, 2, 3]
    itrL = iter(l)
    print(next(itrL))
    print(next(itrL))
    print(next(itrL))

    print("next() 函數遍歷迭代器元素:")
    fib = fibonacci(4)
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))

# testNextItem()

class NumberSequence:
    def __init__(self, init, step, max = 100):
        self.__data = init
        self.__step = step
        self.__max = max

    def __iter__(self):
        return self

    def __next__(self):
        if(self.__data < self.__max):
            tmp = self.__data
            self.__data += self.__step
            return tmp
        else:
            raise StopIteration

def testNumberSequence():
    numSeq = NumberSequence(0, 5, 20)
    print(isinstance(numSeq, Iterable))
    print(isinstance(numSeq, Iterator))
    for n in numSeq:
        print(n, end="\t")

testNumberSequence()
