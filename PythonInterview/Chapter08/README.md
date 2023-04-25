Chapter08 進程與線程
=====
* ### 在 Python 中保證多線程同步的五種方式
    * ### 鎖機制 Lock & RLock
        * ### Lock (互斥锁)
            * ### acquire([timeout]): 使线程进入同步阻塞状态，尝试获得锁定。
            * ### release(): 释放锁，使用前线程必须已获得锁定，否则将抛出异常。
            ```
            import threading

            lock = threading.Lock()

            lock.acquire()
            lock.release()
            ```
        * ### RLock (可重入锁)
            ```
            import threading

            lock = threading.RLock()
            num = 1


            def check():
                global num
                lock.acquire()
                if num < 0:
                    print('num < 0')
                else:
                    print('num > 1')
                lock.release()


            def add():
                global num
                lock.acquire()
                check()
                num += 1
                lock.release()


            t = threading.Thread(target=add)
            t.start()
            t.join()
            ```
        * ### Lock 获取的锁可以被其他任何线程直接释放。
        * ### RLock 获取的锁只有获取这个锁的线程自己才能释放。
    * ### 條件變量 Condition
        * ### acquire(*args): 用于获取隐性锁 (关联锁)，它调用隐性锁的 acquire() 方法，并返回其所返回的值。
        * ### release(): 同上，本方法无返回值。
        * ### wait(timeout=None): 本方法会释放隐性锁，然后阻塞直到被其他线程的调用此条件变量的 notify()、notify_all() 唤醒或超时。一旦被唤醒或超时，该线程将立即重新获取锁并返回。
        * ### notify(n=1): 本方法默认用于唤醒处于等待本条件变量的线程，至多可唤醒所有正在等待本条件变量的线程中的 n 个，如果调用时没有线程处于等待操作，那么本方法的调用是一个空操作。
        * ### notify_all(): 唤醒正在等待本条件变量的所有线程。
        * ### acquire 与 release 可以用 with 语句代替
            ```
            with lock_con:
                lock_con.wait()
            ```
        * ### 简单例子
            ```
            import threading
            import time


            def fun(cndition):
                # 确保先运行 t2
                time.sleep(1)
                # 获得锁
                cndition.acquire()
                print('thread1 acquires lock.')
                # 唤醒 t2
                cndition.notify()
                # 进入等待状态，等待其他线程唤醒
                cndition.wait()
                print('thread1 acquires lock again.')
                # 释放锁
                cndition.release()


            def fun2(cndition):
                # 获得锁
                cndition.acquire()
                print('thread2 acquires lock.')
                # 进入等待状态，等待其他线程唤醒
                cndition.wait()
                print('thread2 acquires lock again.')
                # 唤醒 t1
                cndition.notify()
                # 释放锁
                cndition.release()


            if __name__ == '__main__':
                cndition = threading.Condition()

                t1 = threading.Thread(target=fun, args=(cndition,))
                t2 = threading.Thread(target=fun2, args=(cndition,))
                
                t1.start()
                t2.start()

            
            '''
            thread2 acquires lock.
            thread1 acquires lock.
            thread2 acquires lock again.
            thread1 acquires lock again.
            '''
            ```
        * ### 实现生产与消费者模式
            ```
            import threading
            import time

            from random import randint


            class Producer(threading.Thread):
                def run(self):
                    global L

                    while True:
                        val = randint(0, 100)

                        with lock_con:
                            L.append(val)
                            print(f"生产者:{self.name}, Append:{val}, L = {L}")
                            lock_con.notify()

                        time.sleep(3)


            class Consumer(threading.Thread):
                def run(self):
                    global L

                    while True:
                        with lock_con:
                            if len(L) == 0:
                                print("队列为空，请等待。。。")
                                lock_con.wait()

                            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                            print(f"消费者: {self.name}, Delete: {L[0]}")

                            del L[0]
                        time.sleep(0.5)


            if __name__ == '__main__':
                # 消费物队列
                L = []
                lock_con = threading.Condition()
                threads = []

                # 若干个生产者线程
                for i in range(3):
                    threads.append(Producer())

                threads.append(Consumer())

                for t in threads:
                    t.start()
                for t in threads:
                    t.join()
            ```
    * ### 信號量 Semaphore & BoundedSemaphore
        * ### Semaphore
            * ### 信号量用来控制线程并发数的，信号量里面维护了一个计数器，这个计数器可以理解为锁的数量，线程通过 acquire 方法去申请锁，每申请到一个锁，计数器就减 1。
            * ### 线程通过 release 释放锁，每释放一个锁，计数器就加 1。
            * ### 当计数器为 0 的时候，通过 acquire 方法去申请锁会被阻塞，直到有其它的线程释放锁让计数器不为 0 才有可能申请到锁。
            ```
            import threading, time


            class myThread(threading.Thread):
                def run(self):
                    semaphore.acquire()
                    print(threading.current_thread().name + " 获得锁")
                    time.sleep(1)
                    print(threading.current_thread().name + " 释放锁")
                    semaphore.release()


            if __name__ == "__main__":
                semaphore = threading.Semaphore(2)
                for i in range(4):
                    myThread().start()


            '''
            Thread-1 获得锁
            Thread-2 获得锁
            Thread-1 释放锁
            Thread-2 释放锁
            Thread-3 获得锁
            Thread-4 获得锁
            Thread-4 释放锁
            Thread-3 释放锁
            '''
            ```
        * ### BoundedSemaphore
            * ### 任何一个线程都可以调用 release 方法，即使这个线程没有获取过锁，并且一个线程可以多次调用 release，任意一个线程调用 release 方法都是有效的。
            * ### 前面说过线程每调用一次 release 方法，信号量内部的计数器都会加 1，所以会出现由于线程调用 release 次数过多，导致计数器的值大于信号量计数器的初始值。
            * ### Semaphore 对内部的计数器是没有限制的，但是 BoundedSemaphore 有限制，BoundedSemaphore 内部的计数器大于初始值时会报错。
            ```
            import threading
            import time


            class MyThread(threading.Thread):
                def run(self):
                    print(threading.current_thread().name + " 释放锁")
                    # 连续释放三次锁
                    semaphore.release()
                    semaphore.release()
                    semaphore.release()


            class MyAcquire(threading.Thread):
                def run(self):
                    semaphore.acquire()
                    time.sleep(5)
                    print(threading.current_thread().name + " 获得锁")


            if __name__ == "__main__":
                # semaphore = threading.Semaphore(1)
                semaphore = threading.BoundedSemaphore(1)
                MyThread().start()

                for i in range(4):
                    MyAcquire().start()

            # ValueError: Semaphore released too many times
            ```
    * ### Event 對象
        * ### 透過 "事件" 的方式，讓不同的執行續之間彼此溝通，輕鬆做到 "等待 A 執行緒完成某件事後，B 執行緒再繼續" 的功能。
        * ### threading.Event(): 註冊一個事件。
        * ### 一个事件对象管理一个内部标示符。
        * ### set(): 觸發事件 (將标示符設為 True)。
        * ### wait(): 等待事件被觸發 (使线程一直处于阻塞状态直到标示符变为 True)。
        * ### clear(): 清除事件觸發，事件回到未被觸發的狀態 (將标示符設為 False)。
        * ### 示例 1: 註冊一個 event 事件，當 aa() 執行時使用 event.wait() 等待事件被觸發，接著設定 bb() 執行到 i 等於 30 的時候就會觸發事件，這時 aa() 才會開始運作。
            ```
            import threading
            import time


            def aa():
                event.wait()
                event.clear()
                for i in range(1, 6):
                    print('A:', i)
                    time.sleep(0.5)


            def bb():
                for i in range(10, 60, 10):
                    if i == 30:
                        event.set()
                    print('B:', i)
                    time.sleep(0.5)


            event = threading.Event()
            a = threading.Thread(target=aa)
            b = threading.Thread(target=bb)

            a.start()
            b.start()


            '''
            B: 10
            B: 20
            B: 30
            A: 1
            B: 40
            A: 2
            B: 50
            A: 3
            A: 4
            A: 5
            '''
            ```
        * ### 示例 2: 註冊兩個事件，event_a 會在輸入任意內容後觸發，觸發後就會印出 1 ~ 5 的數字，印出完成後會觸發 event_b，這時才又可以繼續輸入文字，不斷重複兩個事件的觸發與執行續的執行。
            ```
            import threading
            import time


            def aa():
                i = 0
                while True:
                    event_a.wait()
                    event_a.clear()
                    for i in range(1, 6):
                        print(i)
                        time.sleep(0.5)
                    event_b.set()


            def bb():
                while True:
                    input('輸入任意內容')
                    event_a.set()
                    event_b.wait()
                    event_b.clear()


            event_a = threading.Event()
            event_b = threading.Event()
            a = threading.Thread(target=aa)
            b = threading.Thread(target=bb)

            a.start()
            b.start()


            '''
            輸入任意內容a
            1
            2
            3
            4
            5
            輸入任意內容b
            1
            2
            3
            4
            5
            輸入任意內容
            '''
            ```
    * ### Queue 與 Pipe (通信篇) -> [click me](https://gitlab.com/ChiangWei/main/-/tree/master/PythonInterview)
* ### 什麼是全局解譯器鎖 (GIL)
    * ### Python 的全局解释器锁（Global Interpreter Lock，GIL）是一种机制，它确保同一时间只有一个线程能够执行 Python 字节码，也就是说，在多线程编程中，Python 的 GIL 会对多线程执行代码的效率产生影响。
    * ### 在 Python 中，所有线程都共享一个解释器，GIL 会在解释器级别上对多线程执行代码的进程进行协调，以保证在同一时刻只有一个线程能够执行 Python 字节码，这个机制的目的是确保线程安全，防止多线程访问共享资源时出现冲突。
    * ### 然而，由于 GIL 限制了同一时刻只能有一个线程执行 Python 代码，因此在多核 CPU 上，多线程执行 Python 代码的效率可能会受到影响，为了避免这种情况，可以嘗試使用多进程與协程。
    * ### Python 語言設計之初，計算機廣泛使用的還是單核 CPU，為解決多線程之間的數據完整與狀態同步，最簡單的方式就是加鎖，線程運行前要獲取鎖，保證同一時刻只能有一個線程運行，這就是全局解譯器鎖。
    * ### GIL 確保了一個進程中同一時刻只有一個線程運行，多線程在實際運行中只調用了一個 CPU 核心，無法使用多 CPU 核心，因此多線程不能在多個 CPU 核心上平行，面對計算密集型作業效率會非常低，但是對於單線程及 I/O 密集型的作業就沒有影響，反而說多執行緒適合用於 I/O 密集型作業。
    * ### Python 中每個進程都有自己的解譯器，因此多進程不受 GIL 限制，可以在多 CPU 核心上平行，適合計算密集型操作，但進程相對有較大的開銷。
    * ### GIL 不是缺陷，只是一種對解譯器的設計思想，使用 GIL 的有 CPython，未使用 GIL 的有 JPython。
* ### 多線程、多進程與協程
    * ### 先搞清楚以下的名詞 (個人認為是拜 GIL 所賜，所以有了這三種選擇):
        * ### Thread: "執行緒"，又稱 "線程"，可以實現 "Concurrent"，由 ```threading``` 模組實作。
        * ### Process: "行程"，又稱 "進程"，可以實現 "Parallel"，由 ```multiprocessing``` 模組實作。
        * ### Coroutine: "協程"，又稱 "異步" 與 "微線程"，可以實現 "Concurrent"，由 ```asyncio``` 模組實作。
            * ### A "coroutine" is a "concurrency" design pattern.
            * ### "Coroutines" are like threads executing work "concurrently".
        * ### ![image](https://gitlab.com/ChiangWei/main/-/raw/master/AsyncioPrinciples/Chapter02/ConcAndPara.jpg)
    * ### 名詞對照
        * ### Thread
            * ### 台灣: 執行緒
            * ### 中國: 線程
        * ### Process
            * ### 台灣: 行程
            * ### 中國: 進程
        * ### Concurrent
            * ### 台灣: 並行
            * ### 中國: 並發
        * ### Parallel
            * ### 台灣: 平行
            * ### 中國: 並行
    * ### 進程 Process
        * ### 具有一定獨立功能程序關於某數據集合上的一次運行活動。
        * ### 系統進行資源分配和調度的獨立單位。
        * ### 彼此間相互獨立，具有獨立的內存空間。
        * ### 多進程可於 CPU 多核心 Parallel。
        * ### 適用於計算密集型操作。
        * ### 創建過程所消耗資源較多。
    * ### 線程 Thread
        * ### 相較於進程為更小的獨立運行單位。
        * ### 不擁有系統資源只具備運行必要資源。
        * ### 同一進程下所有線程共享內存空間。
        * ### 多進程只能在 CPU 單核心上 Concurrent。
        * ### 適用於 I/O 密集型作業。
        * ### 創建過程所消耗資源較少。
    * ### 協程 Coroutine
        * ### 相較於線程為更小的執行單元。
        * ### 具有自身的寄存器上下文和棧。
        * ### 切換時可以恢復之前的寄存器上下文和棧。
        * ### 無需同進程與線程執行加鎖與解鎖操作。
        * ### 切換時間由程序自身進行調度。
<br />
