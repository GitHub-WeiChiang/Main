APScheduler
=====
* ### APScheduler 定时任务
    * ### Python 中定时任务的解决方案
        * ### crontab: 不适合多台服务器的配置。
        * ### scheduler: 太过于简单。
        * ### Celery: 依赖的软件较多较耗资源。
        * ### APScheduler: 最好的解决方案。
    * ### APScheduler
        * ### 使用方便。
        * ### 提供基于日期、固定时间间隔及 crontab 类型的任务。
        * ### 可以在程序运行过程中动态新增和删除任务。
        * ### 在任务运行过程中可以把任务存储起来，下次启动运行依然保留之前的状态。
        * ### 基于 Python 语言，可以跨平台，一段代码，处处运行。
* ### 安裝
    ```
    pip install apscheduler
    ```
* ### 基本使用: basic.py
    ```
    from apscheduler.schedulers.blocking import BlockingScheduler
    from datetime import datetime
    
    
    def clock():
        print("Hello! The time is: %s" % datetime.now())
    
    
    if __name__ == '__main__':
        aScheduler = BlockingScheduler()
        aScheduler.add_job(clock, "interval", seconds=3)
        aScheduler.start()
    ```
    ```
    Hello! The time is: 2024-01-10 20:07:21.513073
    Hello! The time is: 2024-01-10 20:07:24.512626
    Hello! The time is: 2024-01-10 20:07:27.512850
    Hello! The time is: 2024-01-10 20:07:30.512951
    Hello! The time is: 2024-01-10 20:07:33.513207
    ```
    * ### BlockingScheduler 是阻塞性的调度器，调用 start 方法会阻塞当前进程。
    * ### my_clock 函数是需要定时调度的任务代码。
    * ### 上方代碼实例化了一个 BlockingScheduler 对象，并把 my_clock 添加到任务调度中。
    * ### interval 参数表示使用间隔的方式来调度。
    * ### 调度频率 seconds 設定為 3 也就是每 3 秒执行一次。
* ### 四个基本对象
    * ### 触发器 (Triggers): 根据指定的触发方式，比如按照时间间隔或按照 crontab 触发，触发条件是什么等，每个任务都有自己的触发器。
    * ### 任务存储器 (Job Stores): 可以存储任务，默认將任务保存於内存，也可将任务保存在数据库，任务存储后会进行序列化，故可反序列化提取出任務继续执行。
    * ### 执行器 (Executors): 用於安排任务到线程池或者进程池中运行。
    * ### 调度器 (Schedulers): 整个调度的总指挥官，其会合理安排作业存储器、执行器、触发器进行工作，并进行添加和删除任务等，调度器通常只有一个，开发人员很少直接操作触发器、存储器、执行器等，因为这些都由调度器自动实现。
<br />
