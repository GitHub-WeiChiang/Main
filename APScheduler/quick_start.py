from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


# 指定每日的某一個時間點執行一次 (此示例代碼為每日 19:36 執行一次)
@scheduler.scheduled_job('cron', hour=19, minute=36)
def request_update_status():
    print('Doing job')


scheduler.start()
