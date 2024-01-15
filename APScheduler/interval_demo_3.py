from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print("Hello World")


aBlockingScheduler = BlockingScheduler()

# 每小時 (上下浮動 120 秒區間內) 運行 job_function
aBlockingScheduler.add_job(job_function, 'interval', hours=1, jitter=120)

aBlockingScheduler.start()
