__author__ = "ChiangWei"
__date__ = "2022/04/25"

'''
@ 為 Python 的語法糖。

@ 的功用就是將 printWorld 丟到 printHello 函式中，
而 printHello 函式就是將丟進來的參數包裝後傳出，
最外面的 printWorld 所接收到的東西就是包裝後的 wrapper()，
呼叫 printWorld 時其實是呼叫 wrapper()，
所以會先印出 Hello 在執行方法 printWorld。

裝飾器實現的單例模式，
不適用於以 multiprocessing 進行的多執行緒環境，
因 multiprocessing 庫雖實現了類似 thread 的 API 接口，
但其透過 pickle 序列化部分地實現了變量共享，
被裝飾器裝飾後的類別 (不一定要是實現單例的裝飾器) 或函式，
將無法順利進行序列化，
會引發 _pickle.PicklingError: Can't pickle <class 'xxx'>: it's not the same object as xxx 例外。

*args 與 **kwargs，可以接受任何參數。
'''

def printHello(func):
    def wrapper():
        print('Hello')
        return func()
    return wrapper

@printHello
def printWorld():
    print('World')

printWorld()

print()

# 當裝飾器所裝的函式需要輸入參數
def printHelloArg(func):
    def wrapper(arg):
        print('Hello')
        return func(arg)
    return wrapper

@printHelloArg
def printArg(arg):
    print(arg)

printArg('World')
printArg('Kitty')

print()

# 複雜的函式參數
def printHelloCompArg(func):
    def wrapper(*args, **kwargs):
        print('Hello')
        return func(*args, **kwargs)
    return wrapper

@printHelloCompArg
def printCompArg1(arg):
    print(arg)

@printHelloCompArg
def printCompArg2(arg1, arg2):
    print(arg1)
    print(arg2)

printCompArg1('World')
printCompArg2('Kitty', 'Danny')

print()

# 加上參數的裝飾器
def printArgArg(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(arg)
            return func(*args, **kwargs)

        return wrapper

    return decorator

@printArgArg('Hi')
def sayHiAndPrintArg(arg):
    print(arg)

sayHiAndPrintArg('World')

print()

# 裝飾器修飾類別
class ClassDecorator:
    def __init__(self, func):
        self._numOfCall = 0
        self._func = func

    def __call__(self, *args, **kwargs):
        self._numOfCall += 1
        obj = self._func(*args, **kwargs)
        print("創建 %s 的第 %d 個實例: %s" % (self._func.__name__, self._numOfCall, id(obj)))
        return obj

@ClassDecorator
class MyClass:
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

tony = MyClass("Tony")
karry = MyClass("Karry")
print(id(tony))
print(id(karry))
