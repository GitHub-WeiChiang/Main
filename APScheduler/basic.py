from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def clock():
    print("Hello! The time is: %s" % datetime.now())


if __name__ == '__main__':
    aScheduler = BlockingScheduler()
    aScheduler.add_job(clock, "interval", seconds=3)
    aScheduler.start()
