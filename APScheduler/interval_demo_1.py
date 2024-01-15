from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print("Hello World")


aBlockingScheduler = BlockingScheduler()

# 每 2 小時觸發
aBlockingScheduler.add_job(job_function, 'interval', hours=2)

aBlockingScheduler.start()
