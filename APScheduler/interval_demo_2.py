from apscheduler.schedulers.blocking import BlockingScheduler

aBlockingScheduler = BlockingScheduler()


@aBlockingScheduler.scheduled_job('interval', id='my_job_id', hours=2)
def job_function():
    print("Hello World")


aBlockingScheduler.start()
