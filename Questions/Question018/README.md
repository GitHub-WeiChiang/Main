Question018 - 如何在 Python 中實現 AOP ?
=====
* ### 剖面導向程式設計（AOP, Aspect Oriented Programming)。
* ### 簡單的說就是在程式的前或後執行其它的程式，再更白話一點，就是可以在不更改別人的程式的情況下，可以加入並執行自己的程式 (快、低風險、方便)。
* ### 在動態語言中，因為程式的流程並不是在編譯時期就被決定了，而是可以動態更改的，所以通常原生語法就支持了 AOP 功能。
* ### Python 內建的 decorator 修飾詞可以將被切入的函式直接傳入別的函式，並且藉由回傳另一個已經被修飾完成的函式物件來實現 AOP。
```
def decorator(func):
    def wrapper():
        # 執行前的關注切面, 
        func()
        # 執行後的關注切面
    return wrapper

@decorator
def decorated():
    # 核心業務邏輯
```
* ### 如果不希望被裝飾的函數其元數據被改變成裝飾其的函數，可以透過 Python 內置的 wraps 裝飾器達成，wraps 的作用主要是保持原有函数的元數據。
```
from functools import wraps

def c(func):
    @wraps(func)
    def b(*args, **kwargs):
        print('在函數執行前，做一些操作')
        result = func(*args, **kwargs)
        print("在函數執行後，做一些操作")
        return result
    return b

@c
def a(name, age):
    print('函數執行中。。。')
    return "我是 {}, 今年{}歲 ".format(name, age)
```
<br />
