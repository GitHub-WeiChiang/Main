from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

aBlockingScheduler = BlockingScheduler()


def my_job(text):
    print(text)


# run at: 2024-01-15 00:00:00
aBlockingScheduler.add_job(
    my_job,
    'date',
    run_date=date(2024, 1, 15),
    args=['text']
)

aBlockingScheduler.start()
