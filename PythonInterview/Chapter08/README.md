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
        * ### to be continued
    * ### 同步對列
        * ### to be continued
<br />
