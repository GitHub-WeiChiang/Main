PythonInterview
=====
* ### 高潔篇: Functools (高階函數和可調用對像上的操作)
* ### 通信篇: 進程間的通信 (Queue 與 Pipe)
* ### 垃圾篇: 一文讀懂 Python 垃圾回收與內存管理機制 (在座的各位都是...)
* ### 蒙圈篇: for in if in for else try except else (洗勒公啥)
* ### Chapter02 Python 面試基礎
* ### Chapter03 Python 中函數的應用
* ### Chapter04 Python 序列
* ### Chapter05 字符串和正則表達式
* ### Chapter07 異常處理
* ### Chapter08 進程與線程
* ### Chapter09 Python 操作數據庫
* ### Chapter10 Web 應用入門
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

通信篇: 進程間的通信 (Queue 與 Pipe)
=====
* ### 当使用多个进程时，通常使用消息传递来进行进程之间的通信，并避免必须使用任何同步原语 (如锁)。
* ### 对于传递消息，可以使用 Pipe (用于两个进程之间的连接) 或队列 Queue (允许多个生产者和消费者)。
* ### multiprocessing 通常使用 queue.Empty 和 queue.Full 异常来发出超时信号，它们在 multiprocessing 命名空间中不可用，因此需要从中导入它们 queue。
* ### Queue 用来在多个进程间通信 (get 和 put)
    * ### put: 放数据，Queue.put() 默认有 block = True 和 timeout 两个参数。
    * ### 当 block = True 时，写入是阻塞式的，阻塞时间由 timeout 确定。
    * ### 当队列 q 被 (其他线程) 写满后，这段代码就会阻塞，直至其他线程取走数据。
    * ### Queue.put() 方法加上 block = False 的参数，即可解决这个隐蔽的问题。
    * ### 但要注意，非阻塞方式写队列，当队列满时会抛出 exception Queue.Full 的异常。
    * ### get: 取数据 (默认阻塞)，```Queue.get([block[, timeout]])```获取队列 (timeout 為等待时间)。
    ```
    import os, time, random
    from multiprocessing import Process, Queue
    
    # 写数据进程执行的代码:
    def _write(q,urls):
        print('Process(%s) is writing...' % os.getpid())
        for url in urls:
            q.put(url)
            print('Put %s to queue...' % url)
            time.sleep(random.random())
    
    # 读数据进程执行的代码:
    def _read(q):
        print('Process(%s) is reading...' % os.getpid())
        while True:
            url = q.get(True)
            print('Get %s from queue.' % url)
    
    if __name__=='__main__':
        # 父进程创建Queue，并传给各个子进程：
        q = Queue()

        _writer1 = Process(target=_write, args=(q,['url_1', 'url_2', 'url_3']))
        _writer2 = Process(target=_write, args=(q,['url_4','url_5','url_6']))

        _reader = Process(target=_read, args=(q,))

        # 启动子进程_writer，写入:
        _writer1.start()
        _writer2.start()

        # 启动子进程_reader，读取:
        _reader.start()

        # 等待_writer结束:
        _writer1.join()
        _writer2.join()

        # _reader进程里是死循环，无法等待其结束，只能强行终止:
        _reader.terminate()

    '''
    Process(7460) is writing...
    Put url_1 to queue...
    Process(13764) is writing...
    Put url_4 to queue...
    Process(13236) is reading...
    Get url_1 from queue.
    Get url_4 from queue.
    Put url_2 to queue...
    Get url_2 from queue.
    Put url_5 to queue...
    Get url_5 from queue.
    Put url_6 to queue...
    Get url_6 from queue.
    Put url_3 to queue...
    Get url_3 from queue.
    '''
    ```
* ### Pipe 常用来在两个进程间通信，两个进程分别位于管道的两端。
    ```
    multiprocessing.Pipe([duplex])
    (con1, con2) = Pipe()
    ```
    * ### con1 管道的一端，负责存储，也可以理解为发送信息。
    * ### con2 管道的另一端，负责读取，也可以理解为接受信息。
    ```
    from multiprocessing import Process, Pipe

    def send(pipe):
        pipe.send(['spam'] + [42, 'egg'])   # send 传输一个列表
        pipe.close()

    if __name__ == '__main__':
        # 创建两个 Pipe 实例
        (con1, con2) = Pipe()

        # 函数的参数，args 一定是实例化之后的 Pipe 变量，不能直接写 args=(Pip(),)
        sender = Process(target=send, args=(con1,))

        # Process 类启动进程
        sender.start()

        # 管道的另一端 con2 从 send 收到消息
        print("con2 got: %s" % con2.recv())

        # 关闭管道
        con2.close()
    ```
    * ### 管道是可以同时发送和接受消息的:
    ```
    from multiprocessing import Process, Pipe

    def talk(pipe):
        # 传输一个字典
        pipe.send(dict(name='Bob', spam=42))

        # 接收传输的数据
        reply = pipe.recv()
        
        print('talker got:', reply)

    if __name__ == '__main__':
        # 创建两个 Pipe() 实例，也可以改成 (conf1, conf2)
        (parentEnd, childEnd) = Pipe()

        # 创建一个 Process 进程，名称为 child
        child = Process(target=talk, args=(childEnd,))

        # 启动进程
        child.start()

        # parentEnd 是一个 Pip() 管道，可以接收 child Process 进程传输的数据
        print('parent got:', parentEnd.recv())

        # parentEnd 是一个 Pip() 管道，可以使用 send 方法来传输数据
        parentEnd.send({x * 2 for x in 'spam'})

        # 传输的数据被 talk 函数内的 pip 管道接收，并赋值给 reply
        child.join()

        print('parent exit')

    '''
    parent got: {'name': 'Bob', 'spam': 42}
    talker got: {'ss', 'mm', 'pp', 'aa'}
    parent exit
    '''
    ```
* ### Queue 與 Pipe 的比較
    * ### Queue 使用 put 與 get 维护队列，Pipe 使用 send 與 recv 维护队列 。
    * ### Pipe 只提供两个端点，而 Queue 没有限制。
        * ### 这意味着在使用 Pipe 时，只能同时启动两个进程，一个生产者和一个消费者在这两个端点上操作 (由 Pipe() 返回的两个值)，这两个端点一起维护一个队列。
        * ### 如果多个进程同时在管道的同一个端点上操作，就会出现错误 (因为没有锁，类似于线程不安全)。
        * ### 因此，两个端点相当于只为流程提供两个安全操作位置，从而将流程数量限制为只有 2 个。
    * ### Queue 的封装比较好，Queue 只提供一个结果，可以被多个进程同时调用；Pipe 返回两个结果，分别由两个进程调用。
    * ### Queue 的实现基于 Pipe，所以 Pipe 的运行速度比 Queue 快很多。
    * ### 当只需要两个进程时，管道更快，当需要多个进程同时操作队列时，使用队列。
<br />

垃圾篇: 一文讀懂 Python 垃圾回收與內存管理機制 (在座的各位都是...)
=====
內存管理機制
-----
* ### 什么是内存管理器
    * ### Python 作为一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言，与大多数编程语言不同，Python 中的变量无需事先申明，变量无需指定类型，程序员无需关心内存管理。
    * ### Python 解释器具備自动回收，开发人员不用过多的关心内存管理机制，这一切全部由 Python 内存管理器承担了复杂的内存管理工作。
* ### 为什么要引入内存池
    * ### 当创建大量消耗小内存的对象时，频繁调用 new / malloc 会导致大量的内存碎片，致使效率降低。
    * ### 内存池的作用就是预先在内存中申请一定数量的，大小相等的内存块留作备用，当有新的内存需求时，就先从内存池中分配内存给这个需求，不够之后再申请新的内存。
    * ### Python 中的内存管理机制为 Pymalloc，这样做最显著的优势就是能够减少内存碎片，提升效率。
* ### 内存池是如果工作的
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/PythonInterview/CPython.png)
    * ### Python 的对象管理主要位于 Level +1 ~ Level +3 层。
    * ### Level +3 层: 对于 Python 内置的对象 (比如 int、dict 等) 都有独立的私有内存池，对象之间的内存池不共享，即 int 释放的内存，不会被分配给 float 使用。
    * ### Level +2 层: 当申请的内存大小小于 256 KB 时，内存分配主要由 Python 对象分配器 (Python’s object allocator) 实施。
    * ### Level +1 层: 当申请的内存大小大于 256 KB 时，由 Python 原生的内存分配器进行分配，本质上是调用 C 标准库中的 malloc / realloc 等函数。
    * ### 关于释放内存方面，当一个对象的引用计数变为 0 时，Python 就会调用它的析构函数 (解構子)。
    * ### 调用析构函数并不意味着最终一定会调用 free 来释放内存空间，如果真是这样的话，那频繁地申请、释放内存空间会使 Python 的执行效率大打折扣。
    * ### 因此在析构时也采用了内存池机制，从内存池申请到的内存会被归还到内存池中，以避免频繁地申请和释放动作。
垃圾回收機制
-----
* ### 得益于 Python 的自动垃圾回收机制，在 Python 中创建对象时无须手动释放。
* ### 这对开发者非常友好，让开发者无须关注低层内存管理。
* ### 但如果对其垃圾回收机制不了解，很多时候写出的 Python 代码会非常低效。
* ### 垃圾回收算法有很多，主要有: 引用计数、标记 - 清除、分代收集等。
* ### 在 Python 中，垃圾回收算法以引用计数为主，标记 - 清除和分代收集两种机制为辅。
* ### 引用计数
    * ### 引用计数算法原理
        * ### 每个对象有一个整型的引用计数属性，用于记录对象被引用的次数。
        * ### 例如对象 A，如果有一个对象引用了 A，则 A 的引用计数 +1。
        * ### 当引用删除时，A 的引用计数 -1。
        * ### 当 A 的引用计数为 0 时，即表示对象 A 不可能再被使用，直接回收。
    * ### 在 Python 中，可以通过 sys 模块的 getrefcount 函数获取指定对象的引用计数器的值。
    ```
    import sys

    class A():
        def __init__(self):
            pass
            
    a = A()

    print(sys.getrefcount(a))
    # 2
    ```
    * ### 计数器增减条件: 上述範例，创建一个 A 对象，并将对象赋值给 a 变量后，对象的引用计数器值为 2。
        * ### 引用计数 +1 的条件
            * ### 对象被创建，如 A()。
            * ### 对象被引用，如 a = A()。
            * ### 对象作为函数的参数，如 func(a)。
            * ### 对象作为容器的元素，如 arr = [a, a]。
        * ### 引用计数 -1 的条件
            * ### 对象被显式销毁，如 del a。
            * ### 变量重新赋予新的对象，例如 a = 0。
            * ### 对象离开它的作用域，如 func 函数执行完毕时，func 函数中的局部变量 (全局变量不会)。
            * ### 对象所在的容器被销毁，或从容器中删除对象。
    ```
    import sys


    class A:
        def __init__(self):
            pass


    print("创建对象 0 + 1 = ", sys.getrefcount(A()))

    a = A()
    print("创建对象并赋值 0 + 1 + 1 = ", sys.getrefcount(a))

    b = a
    c = a
    print("赋给 2 个变量 2 + 1 + 1 = ", sys.getrefcount(a))

    b = None
    print("变量重新赋值 4 - 1 = ", sys.getrefcount(a))

    del c
    print("del 对象 3 - 1 = ", sys.getrefcount(a))

    d = [a, a, a]
    print("3 次加入列表 2 + 3 = ", sys.getrefcount(a))


    def func(var):
        # 神奇吧，為什麼這裡會是 3 呢 ? 原因是:
        # 除了外部的實例化與作為函數參數各自所造成的 +1，
        # 实际上另一个引用 (另一个 +1) 是函数栈保存了入参对形参的引用。

        print('传入函数 1 + 2 = ', sys.getrefcount(var))


    func(A())

    '''
    创建对象 0 + 1 =  1
    创建对象并赋值 0 + 1 + 1 =  2
    赋给 2 个变量 2 + 1 + 1 =  4
    变量重新赋值 4 - 1 =  3
    del 对象 3 - 1 =  2
    3 次加入列表 2 + 3 =  5
    传入函数 1 + 2 =  3
    '''
    ```
    * ### 引用计数优点
        * ### 高效、逻辑简单，只需根据规则对计数器做加减法。
        * ### 实时性: 一旦对象的计数器为零，就说明对象永远不可能再被用到，无须等待特定时机，直接释放内存。
    * ### 缺点
        * ### 需要为对象分配引用计数空间，增大了内存消耗。
        * ### 当需要释放的对象比较大时，如字典对象，需要对引用的所有对象循环嵌套调用，可能耗时比较长。
        * ### 循环引用: 这是引用计数的致命伤，引用计数对此是无解的，因此必须要使用其它的垃圾回收算法对其进行补充。
        * ### 註: 孤島參照法 (lsolating a Reference) 會造成 "循环引用" 現象。
        * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/PythonInterview/CircularReference.png)
* ### 标记 - 清除
    * ### 引用计数算法无法解决循环引用问题，循环引用的对象会导致大家的计数器永远都不会等于 0，带来无法回收的问题。
    * ### 标记 - 清除算法主要用于潜在的循环引用问题，该算法分为 2 步:
        * ### 标记阶段: 将所有的对象看成图的节点，根据对象的引用关系构造图结构，从图的根节点遍历所有的对象，所有访问到的对象被打上标记，表明对象是 "可达" 的。
        * ### 清除阶段: 遍历所有对象，如果发现某个对象没有标记为 "可达" 则回收。
    ```
    class A:
        def __init__(self):
            self.obj = None


    def func():
        a = A()
        b = A()
        c = A()
        d = A()

        # 函數結束後將形成 "孤島參照"
        a.obj = b
        b.obj = a

        return [c, d]


    e = func()
    ```
    * ### 上述範例，a 和 b 相互引用，e 引用了 c 和 d。
    * ### 如果采用引用计数器算法，那么 a 和 b 两个对象将无法被回收。
    * ### 而采用标记清除法，从根节点 (即 e 对象) 开始遍历，c、d、e 三个对象都会被标记为可达，而 a 和 b 无法被标记，因此 a 和 b 会被回收。
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/PythonInterview/MarkAndSweep.png)
    * ### 什么样的对象会被看成是根节点
        * ### 当前栈帧中的本地变量表中引用的对象，如各个线程被调用的方法堆栈中使用到的参数、局部变量、临时变量等。
        * ### 全局静态变量
        * ### 註: "栈帧" 也叫 "过程活动记录"，是编译器用来实现过程 / 函数调用的一种数据结构。
    * ### 标记 - 清除的缺點
        * ### STW 问题 (Stop The World)。因为算法在标记时必须暂停整个程序，否则其它线程的代码可能会改变对象状态，从而可能把不应该回收的对象当做垃圾收集掉。
        * ### 当程序中的对象逐渐增多时，递归遍历整个对象树会消耗很多的时间，在大型程序中这个时间可能会是毫秒级别的。
        * ### 让所有的用户等待几百毫秒的 GC 时间这是不能容忍的。
* ### 分代收集
    * ### 在执行垃圾回收过程中，程序会被暂停，即 stop-the-world。
    * ### 为了减少程序的暂停时间，采用分代回收 (Generational Collection) 降低垃圾收集耗时。
    * ### 分代回收基于以下法则
        * ### 大部分对象的生命周期非常短，朝生夕灭；还有一些对象，它們的生命周期很长，有的甚至长生不老，于是就有了分代的概念。
        * ### 经历越多次数的垃圾收集且活下来的对象，说明该对象越不可能是垃圾，应该越少去收集。
    * ### Python 中，对象一共有 3 种世代: G0、G1 與 G2
        * ### 对象刚创建时为 G0。
        * ### 如果在一轮 GC 扫描中存活下来，则移至 G1，处于 G1 的对象被扫描次数会减少。
        * ### 如果再次在扫描中活下来，则进入 G2，处于 G1 的对象被扫描次数将会更少。
    * ### 触发 GC 时机
        * ### 当某世代中分配的对象数量与被释放的对象之差达到某个阈值的时，将触发对该代的扫描。当某世代触发扫描时，比该世代年轻的世代也会触发扫描。
        * ### 阈值 4 多少
        ```
        import gc
        threshold = gc.get_threshold()
        print("各世代的阈值:", threshold)

        # 设置各世代阈值
        # gc.set_threshold(threshold0[, threshold1[, threshold2]])
        gc.set_threshold(800, 20, 20)

        '''
        各世代的阈值: (700, 10, 10)
        '''
        ```
        * ### 每新增 700 个需要 GC 的对象，Python 就执行一次 G0 的 GC 操作。
        * ### 每执行 10 次 G0 的 GC，触发一次 G1 的 GC。
        * ### 每执行 10 次 G1 的 GC，触发一次 G2 的 GC (其實頻率更低)。
<br />

蒙圈篇: for in if in for else try except else (洗勒公啥)
=====
```
>>> newList = []
>>> for x in a:
... if x % 2 == 0:
...    newList.append(x)
>>> newList
[12, 4, 6]

# vs.

>>> a = [12, 3, 4, 6, 7, 13, 21]
>>> newList = [x for x in a if x % 2 == 0]
>>> newList
[12, 4, 6]
```
```
>>> a = [12, 3, 4, 6, 7, 13, 21]
>>> b = ['a', 'b', 'x']
>>> newList = [(x, y) for x in a for y in b]
>>> newList
[(12, 'a'), (12, 'b'), (12, 'x'), (3, 'a'), (3, 'b'), (3, 'x'), (4, 'a'), (4, 'b'), (4, 'x'), (6, 'a'), (6, 'b'), (6, 'x'), (7, 'a'), (7, 'b'), (7, 'x'), (13, 'a'), (13, 'b'), (13, 'x'), (21, 'a'), (21, 'b'), (21, 'x')]
>>> newList2 = [(x, y) for x in a for y in b if x % 2 == 0 and y < 'x']
>>> newList2
[(12, 'a'), (12, 'b'), (4, 'a'), (4, 'b'), (6, 'a'), (6, 'b')]

# 前面的 for 语句是外层的循环，後面的 for 语句是內层的循环
```
```
def print_prime(n):
    for i in range(2, n):
        found = True
        for j in range(2, i):
            if i % j == 0:
                found = False
                break
        if found:
            print("{} it's a prime number".format(i))

# vs.

def print_prime(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        # 循环正常结束时 (非 return 或 break 等)，else 子句的逻辑就会被执行到
        else:
            print("{} it's a prime number".format(i))
```
```
def demo(str_param):
    try:
        # Do something here
        pass
    except Exception:
        print("有錯就執行")
    else:
        print("沒錯才執行")
    finally:
        print("無論如何都執行")
```
<br />

Reference
=====
* ### Python 程序員面試筆試通關攻略
<br />
