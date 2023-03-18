PythonInterview
=====
* ### 高潔篇: Functools (高階函數和可調用對像上的操作)
* ### 線程篇: 詳解 threading 模塊
* ### 進程篇: 詳解 multiprocessing 模塊
* ### Chapter01 Python 面試基礎
<br />

高潔篇: Functools (高階函數和可調用對像上的操作)
=====
* ### partial
    * ### 用於建立一個偏函數，將預設引數包裝一個可呼叫物件，返回結果也是可呼叫物件。
    * ### 偏函數可以固定住原函數的部分引數，從而在呼叫時更簡單。
    ```
    from functools import partial

    int2 = partial(int, base=8)
    print(int2('123'))
    # 83
    ```
* ### update_wrapper
    * ### 使用 partial 包裝的函數是沒有 \_\_name\_\_ 和 \_\_doc\_\_ 屬性的。
    * ### 將被包裝函數的 \_\_name\_\_ 等屬性，拷貝到新的函數中去。
    ```
    from functools import update_wrapper


    def wrap2(func):
        def inner(*args):
            return func(*args)
        return update_wrapper(inner, func)


    @wrap2
    def demo():
        print('hello world')


    print(demo.__name__)
    # demo
    ```
* ### wraps
    * ### warps 函數是為了在裝飾器拷貝被裝飾函數的 \_\_name\_\_。
    * ### 在 update_wrapper 上進行一個包裝。
    ```
    from functools import wraps


    def wrap1(func):
        # 去掉就會返回 inner
        @wraps(func)
        def inner(*args):
            print(func.__name__)
            return func(*args)
        return inner


    @wrap1
    def demo():
        print('hello world')


    print(demo.__name__)
    # demo
    ```
* ### reduce
    * ### 將一個序列歸納為一個輸出。
    ```
    from functools import reduce

    arr = range(1, 50)

    print(reduce(lambda x, y: x + y, arr))
    # 1225
    ```
* ### cmp_to_key
    * ### 在 list.sort 和內建函數 sorted 中都有一個 key 引數。
    ```
    x = ['aaaaa', 'bbbb', 'ccc']

    x.sort(key=len)

    print(x)
    # ['ccc', 'bbbb', 'aaaaa']
    ```
* ### lru_cache
    * ### 允許將一個函數的返回值快速地快取或取消快取。
    * ### 該裝飾器用於快取函數的呼叫結果，對於需要多次呼叫的函數，而且每次呼叫引數都相同，則可以用該裝飾器快取呼叫結果，從而加快程式執行。
    * ### 該裝飾器會將不同的呼叫結果快取在記憶體中，因此需要注意記憶體佔用問題。
    ```
    from functools import lru_cache


    # maxsize 引數指定 lru_cache 快取最近多少個返回值
    @lru_cache(maxsize=30)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)


    print([fib(n) for n in range(10)])

    # 清空快取
    fib.cache_clear()
    ```
* ### singledispatch
    * ### 單分發器，Python 3.4 新增，用於實現泛型函數。
    * ### 根據單一引數的型別來判斷呼叫哪個函數。
    ```
    from functools import singledispatch


    @singledispatch
    def fun(text):
        print('String：' + text)


    @fun.register(int)
    def _(text):
        print(text)


    @fun.register(list)
    def _(text):
        for k, v in enumerate(text):
            print(k, v)


    @fun.register(float)
    @fun.register(tuple)
    def _(text):
        print(text)
        print('float, tuple')


    fun('Save water. Shower with your girlfriend.')
    fun(123)
    fun(['a', 'b', 'c'])
    fun(1.23)
    # 所有的泛型函數
    print(fun.registry)
    # 獲取 int 的泛型函數
    print(fun.registry[int])
    # String：Save water. Shower with your girlfriend.
    # 123
    # 0 a
    # 1 b
    # 2 c
    # 1.23
    # float, tuple
    # {<class 'object'>: <function fun at 0x104920040>, <class 'int'>: <function _ at 0x104aa64d0>, <class 'list'>: <function _ at 0x104aa6560>, <class 'tuple'>: <function _ at 0x104aa6680>, <class 'float'>: <function _ at 0x104aa6680>}
    # <function _ at 0x104aa64d0>
    ```
<br />

線程篇: 詳解 threading 模塊
=====
* ### 多进程和多线程都可以执行多个任务，线程是进程的一部分。线程的特点是线程之间可以共享内存和变量，资源消耗少，缺点是线程之间的同步和加锁比较麻烦。
* ### ![image]()
<br />

進程篇: 詳解 multiprocessing 模塊
=====
<br />

Reference
=====
* ### Python 程序員面試筆試通關攻略
<br />
