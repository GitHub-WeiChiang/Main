Sched
=====
* ### 延迟 2 秒钟之后执行 say_hello() 函数
    ```
    import sched
    import time


    def say_hello(name):
        print(f"Hello, world, {name}")


    # 实例化一个定时器
    scheduler = sched.scheduler(time.time, time.sleep)

    # 执行定时任务的操作，需傳入:
    # 延迟的时间、任务的优先级、具体的执行函数和执行函数中的参数
    scheduler.enter(2, 1, say_hello, ("张三",))

    # 執行
    scheduler.run()
    ```
* ### 若有特殊需求，需设置任务执行的优先级来指定函数运行的顺序。
    ```
    import sched
    import time


    def say_hello_1(name):
        print(f"say_hello_1, {name}")


    def say_hello_2(name):
        print(f"say_hello_2, {name}")


    scheduler = sched.scheduler(time.time, time.sleep)

    scheduled_time = time.time() + 1

    scheduler.enterabs(scheduled_time, 2, say_hello_1, ("张三",))
    scheduler.enterabs(scheduled_time, 1, say_hello_2, ("李四",))
    scheduler.run()
    ```
* ### 重复执行
    ```
    import sched
    import time


    def say_hello():
        print("Hello, world!")


    scheduler = sched.scheduler(time.time, time.sleep)


    def repeat_task():
        scheduler.enter(2, 1, say_hello, ())
        scheduler.enter(2, 1, repeat_task, ())


    repeat_task()
    scheduler.run()
    ```
* ### 定时任务加上取消方法
    ```
    import sched
    import time


    def task_one():
        print("Task One - Hello, world!")


    def task_two():
        print("Task Two - Hello, world!")


    scheduler = sched.scheduler(time.time, time.sleep)

    # 任务一在 1 秒钟之后运行
    task_one_event = scheduler.enter(1, 1, task_one, ())

    # 任务二在 2 秒钟之后运行
    task_two_event = scheduler.enter(2, 1, task_two, ())

    # 取消执行 task_one
    scheduler.cancel(task_one_event)

    scheduler.run()
    ```
* ### 指定特殊時間執行
    ```
    import sched
    import time
    import datetime


    def special_task():
        print("執行")


    def schedule_backup():
        # 创建新的定时器
        scheduler = sched.scheduler(time.time, time.sleep)

        # 指定特殊時間
        scheduled_time = datetime.datetime(2023, 4, 24, 18, 53)
        scheduled_timestamp = time.mktime(scheduled_time.timetuple())
        scheduler.enterabs(scheduled_timestamp, 1, special_task, ())

        # 开启定时任务
        scheduler.run()


    schedule_backup()
    ```
* ### "迴圈搭配 delay" vs. "Sched 模組"
    * ### "迴圈搭配 delay"
        * ### 實現簡單。
        * ### 可以方便地根據時間間隔執行任務。
        * ### 會阻塞主線程，導致無法同時處理其他任務。
        * ### 如果定時不準確，可能會出現延遲。
    * ### "Sched 模組"
        * ### 可以非常準確地控制任務的執行時間，避免了上述的延遲問題。
        * ### 不會阻塞主線程，可以同時處理其他任務。
        * ### 可能需要額外的學習成本。
        * ### 如果有大量任務需要執行，可能需要手動設置多個 sched，造成程式碼複雜度上升。
    * ### 如果只需要簡單地執行重複任務，並且不需要同時處理其他任務，使用第一種方法可以滿足需求。
    * ### 如果需要精確控制任務執行時間，或者需要同時處理多個任務，建議使用第二種方法。
* ### 結論: 不要把困難的程式搞得更困難，人生苦短，既用 Python，迴圈 delay !
<br />
