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
    Hello! The time is: 2024-01-10 19:59:58.202513
    Hello! The time is: 2024-01-10 20:00:01.200105
    Hello! The time is: 2024-01-10 20:00:04.201309
    ```
    * ### BlockingScheduler 是阻塞性的调度器，调用 start 方法会阻塞当前进程。
    * ### my_clock 函数是需要定时调度的任务代码。
    * ### 上方代碼实例化了一个 BlockingScheduler 对象，并把 my_clock 添加到任务调度中。
    * ### interval 参数表示使用间隔的方式来调度。
    * ### 调度频率 seconds 設定為 3 也就是每 3 秒执行一次。
* ### 四个基本对象
<br />