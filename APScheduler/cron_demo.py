from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print("Hello World")


aBlockingScheduler = BlockingScheduler()

# 任務會在 6、7、8、11 和 12 月的第 3 個週五 00:00、01:00、02:00 和 03:00 觸發
aBlockingScheduler.add_job(
    job_function,
    'cron',
    month='6-8,11-12',
    day='3rd fri',
    hour='0-3'
)

aBlockingScheduler.start()
