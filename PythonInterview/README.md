PythonInterview
=====
* ### 高潔篇: Functools (高階函數和可調用對像上的操作)
* ### 通信篇: 進程間的通信 (Queue 與 Pipe)
* ### Chapter02 Python 面試基礎
* ### Chapter03 Python 中函數的應用
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
<br />

Reference
=====
* ### Python 程序員面試筆試通關攻略
<br />
