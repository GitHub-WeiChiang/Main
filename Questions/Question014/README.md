Question014 - CPU 密集型和 IO 密集型的應對策略建議是什麼 ?
=====
* ### CPU 密集型 (CPU - bound): 可以使用 ProcessPoolExecutor，灑下去讓我們強大的 CPU 去執行，Process 建議使用預設值，也就是與核心同等數量的 Process。
* ### IO 密集型 (I/O - bound): 可以使用 ThreadPoolExecutor，通常 Thread 數量會是核心數量的數倍，可以透過公式計算 (阻塞系数 = 阻塞时间 / (阻塞时间 + 计算时间))。
* ### 如果不想使用 Thread 來進行任務
    * ### CPU 密集型建議使用 multiprocessing
    * ### IO 密集型建議使用 multiprocessing.dummy。
* ### Python 所支援的多協程 Coroutine (asycio) 適用於 IO 密集型任務。
* ### Numba 庫適用於 CPU 密集型任務。
<br />
