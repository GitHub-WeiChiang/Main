APScheduler
=====
* ### 文檔 -> [click me](https://apscheduler.readthedocs.io/en/latest/index.html)
* ### 安裝 APScheduler
    ```
    pip install apscheduler
    ```
* ### 快速開始: quick_start.py
    ```
    from apscheduler.schedulers.blocking import BlockingScheduler
    
    scheduler = BlockingScheduler()
    
    
    # 指定每日的某一個時間點執行一次 (此示例代碼為每日 19:36 執行一次)
    @scheduler.scheduled_job('cron', hour=19, minute=36)
    def request_update_status():
        print('Doing job')
    
    
    scheduler.start()
    ```
* ### 基本概念 - APScheduler 四大組件
    * ### 觸發器 triggers: 用於設定觸發任務的條件。
    * ### 任務儲存器 job stores: 用於存放任務，把任務存放在內存或數據庫中。
    * ### 執行器 executors: 用於執行任務，可以設定執行模式爲單線程或線程池。
    * ### 調度器 schedulers: 把上方三個組件作爲參數，通過創建調度器實例來運行。
* ### 觸發器 triggers
    * ### 每一個任務都有自己的觸發器，觸發器用於決定任務下次運行的時間。
* ### 任務儲存器 job stores
    * ### 默認情況下，任務存放在內存中，也可以配置存放在不同類型的數據庫中。
    * ### 如果任務存放在數據庫中，那麼任務的存取有一個序列化和反序列化的過程，同時修改和搜索任務的功能也是由任務儲存器實現。
    * ### 一個任務儲存器不要共享給多個調度器，否則會導致狀態混亂。
* ### 執行器 executors
    * ### 任務會被執行器放入線程池或進程池去執行，執行完畢後，執行器會通知調度器。
* ### 調度器 schedulers
    * ### 一個調度器由上方三個組件構成，一般來說，一個程序只要有一個調度器就可以了。
    * ### 開發者也不必直接操作任務儲存器、執行器以及觸發器，因爲調度器提供了統一的接口，通過調度器就可以操作組件，比如任務的增刪改查。
* ### 調度器組件詳解
    * ### 根據開發需求選擇相應的組件，下面是不同的調度器組件:
        * ### BlockingScheduler (阻塞式調度器): 適用於只跑調度器的程序。
        * ### BackgroundScheduler (後臺調度器): 適用於非阻塞的情況，調度器會在後臺獨立運行。
        * ### AsyncIOScheduler (asyncio 調度器): 適用於應用使用 asyncio 的情況。
        * ### GeventScheduler (gevent 調度器): 適用於應用通過 gevent 的情況。
        * ### TornadoScheduler (Tornado 調度器): 適用於構建 Tornado 應用。
        * ### TwistedScheduler (Twisted 調度器): 適用於構建 Twisted 應用。
        * ### QtScheduler (Qt 調度器): 適用於構建 Qt 應用。
    * ### 任務儲存器的選擇，要看任務是否需要持久化，如果運行的任務是無狀態的，選擇默認任務儲存器 MemoryJobStore 就可以應付，但是如果需要在程序關閉或重啓時保存任務的狀態，那麼就要選擇持久化的任務儲存器 (推薦使用 SQLAlchemyJobStore 並搭配 PostgreSQL)。
    * ### 執行器的選擇，同樣視實際需求而定，默認的 ThreadPoolExecutor 線程池執行器方案可以滿足大部分需求，如果程序是計算密集型的，那麼最好用 ProcessPoolExecutor 進程池執行器方案來充分利用多核算力，也可以將 ProcessPoolExecutor 作爲第二執行器，混合使用兩種不同的執行器。
    * ### 配置一個任務，就要設置一個任務觸發器，觸發器可以設定任務運行的週期、次數和時間。
    * ### APScheduler 三種內置的觸發器:
        * ### date (日期): 觸發任務運行的具體日期。
        * ### interval (間隔): 觸發任務運行的時間間隔。
        * ### cron (週期): 觸發任務運行的週期。
    * ### 一個任務也可以設定多種觸發器 (複合觸發器)，例如可以設定同時滿足所有觸發器條件而觸發或者滿足一項即觸發。
* ### 觸發器詳解
    * ### date (在指定時間點觸發任務): data_demo.py
        ```
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
        ```
        * ### run_date: 可以是 date 類型、datetime 類型或文本類型。
            * ### datetime 類型 (用於精確時間)
                ```
                # 在 2024 年 1 月 1 日 00:00:00 執行
                aBlockingScheduler.add_job(
                    my_job,
                    'date',
                    run_date=datetime(2024, 1, 1, 00, 00, 00),
                    args=['text']
                )
                ```
            * ### 文本類型
                ```
                aBlockingScheduler.add_job(
                    my_job,
                    'date',
                    run_date='2023-01-01 00:00:00',
                    args=['text']
                )
                ```
            * ### 未指定時間 (立即執行)
                ```
                aBlockingScheduler.add_job(my_job, args=['text'])
                ```
    * ### interval (週期觸發任務): interval_demo_1.py
        ```
        from apscheduler.schedulers.blocking import BlockingScheduler
        
        
        def job_function():
            print("Hello World")
        
        
        aBlockingScheduler = BlockingScheduler()
        
        # 每 2 小時觸發
        aBlockingScheduler.add_job(job_function, 'interval', hours=2)
        
        aBlockingScheduler.start()
        ```
        * ### 可以框定週期開始時間 start_date 和結束時間 end_date。
            ```
            # 將週期觸發的時間範圍設定在 2024-01-01 00:00:00 至 2024-01-02 00:00:00
            aBlockingScheduler.add_job(
                job_function,
                'interval',
                hours=2,
                start_date='2024-01-01 00:00:00',
                end_date='2024-01-02 00:00:00'
            )
            ```
        * ### 可以通過 scheduled_job() 裝飾器實現: interval_demo_2.py
            ```
            from apscheduler.schedulers.blocking import BlockingScheduler
            
            aBlockingScheduler = BlockingScheduler()
            
            
            @aBlockingScheduler.scheduled_job('interval', id='my_job_id', hours=2)
            def job_function():
                print("Hello World")
            
            
            aBlockingScheduler.start()
            ```
        * ### jitter 振動參數: interval_demo_3.py
            * ### 給每次觸發添加一個隨機浮動秒數，適用於多服務器，避免同時運行造成服務擁堵。
            ```
            from apscheduler.schedulers.blocking import BlockingScheduler
            
            
            def job_function():
                print("Hello World")
            
            
            aBlockingScheduler = BlockingScheduler()
            
            # 每小時 (上下浮動 120 秒區間內) 運行 job_function
            aBlockingScheduler.add_job(job_function, 'interval', hours=1, jitter=120)
            
            aBlockingScheduler.start()
            ```
    * ### cron (強大的類 crontab 表達式): cron_demo.py
        ```
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
        ```
        ```
        class apscheduler.triggers.cron.CronTrigger(
            year=None,
            month=None,
            day=None,
            week=None,
            day_of_week=None,
            hour=None,
            minute=None,
            second=None,
            start_date=None,
            end_date=None,
            timezone=None,
            jitter=None
        )
        ```
        * ### 當省略時間參數時，在顯式指定參數之前的參數會被設定爲 "*"，之後的參數會被設定爲最小值。
        * ### week 和 day_of_week 的最小值爲 "*"。
        * ### 例: 設定 ```day=1, minute=20``` 等同於設定 ```year='*', month='*', day=1, week='*', day_of_week='*', hour='*', minute=20, second=0```，即每個月的第一天，且當分鐘到達 20 時就觸發。
        * ### 表達式類型
            | 表達式    | 參數類型 | 描述                           |
            |--------|------|------------------------------|
            | *      | 所有   | 通配符 (例: "minutes=*" 即每分鐘觸發)。 |
            | */a    | 所有   | 可被 a 整除的通配符。                 |
            | a-b    | 所有   | 範圍 a-b 觸發。                   |
            | a-b/c  | 所有   | 範圍 a-b 且可被 c 整除時觸發。          |
            | xth y  | 日    | 第幾個星期幾觸發 (x 爲第幾個，y 爲星期幾)。    |
            | last x | 日    | 一個月中最後個星期幾觸發。                |
            | last   | 日    | 一個月的最後一天觸發。                  |
            | x,y,z  | 所有   | 組合表達式，可以組合確定值或上方的表達式。        |
        * ### month 和 day_of_week 參數分別接受的是英語縮寫 "jan – dec" 和 "mon – sun"。
        * ### start_date 和 end_date 可以用於指定時間範圍:
            ```
            # 在 2014-05-30 00:00:00 前每週一到每週五 5:30 運行
            aBlockingScheduler.add_job(
                job_function,
                'cron',
                day_of_week='mon-fri',
                hour=5,
                minute=30,
                end_date='2014-05-30'
            )
            ```
        * ### 通過 scheduled_job() 裝飾器實現:
            ```
            @aBlockingScheduler.scheduled_job('cron', id='my_job_id', day='last sun')
            def some_decorated_task():
                print("I am printed at 00:00:00 on the last Sunday of every month!")
            ```
        * ### 使用標準 crontab 表達式:
            ```
            aBlockingScheduler.add_job(job_function, CronTrigger.from_crontab('0 0 1-15 may-aug *'))
            ```
        * ### 添加 jitter 振動參數:
            ```
            # 每小時上下浮動 120 秒觸發
            aBlockingScheduler.add_job(job_function, 'cron', hour='*', jitter=120)
            ```
        * ### 夏令時問題
            ```
            aBlockingScheduler.add_job(job_function, 'cron', hour=3, minute=30)
            ```
            * ### 當處於某些時區時，可能會面臨夏令時變更帶來的問題，這可能導致任務未執行或執行兩次的情況。
            * ### 為了避免這樣的問題，建議使用協調世界時 (UTC) 時間，因為它不受夏令時的影響。
            * ### 假設處於 Europe / Helsinki 時區，夏令時通常在三月的最後一個星期一開始，並在十月的最後一個星期一結束。
            * ### 上方示例代碼使用 aBlockingScheduler.add_job 安排一項任務，指定在每天的 3 點 30 分執行。
            * ### 然而在夏令時變更期間可能會出現問題，特別是在十月的最後一個星期一，可能會觸發兩次。
            * ### 為了解決這個問題，建議使用 UTC 時間來安排任務，因為它不受夏令時的影響。
            * ### 或者可以提前了解夏令時的變化，並相應調整任務的計劃，以確保在時區變更時仍能正確執行。
* ### 配置調度器
    * ### 文檔 -> [click me](https://apscheduler.readthedocs.io/en/latest/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler)
    * ### APScheduler 有多種不同的配置方法，可以選擇直接傳字典或傳參的方式創建調度器；也可以先實例一個調度器對象，再添加配置信息。
    * ### 一些調度器子類可能有它們自己特有的配置選項；獨立的任務儲存器和執行器也可能有自己特有的配置選項。
    * ### 創建一個使用默認任務儲存器和執行器的 BackgroundScheduler:
        ```
        from apscheduler.schedulers.background import BackgroundScheduler
        
        scheduler = BackgroundScheduler()
        
        # 因爲是非阻塞的後臺調度器，所以程序會繼續向下執行
        ```
        * ### 這樣就可以創建了一個後臺調度器，這個調度器有一個名稱爲 default 的 MemoryJobStore (內存任務儲存器) 和一個名稱是 default 且最大線程是 10 的 ThreadPoolExecutor (線程池執行器)。
    * ### 示例: 需求描述
        * ### 需要兩個任務儲存器並分別搭配兩個執行器。
        * ### 需要修改任務的默認參數。
        * ### 需要修改時區。
    * ### 示例: 需求規格
        * ### 名稱爲 "mongo" 的 MongoDBJobStore。
        * ### 名稱爲 "sql" 的 SQLAlchemyJobStore。
        * ### 名稱爲 "thread" 的 ThreadPoolExecutor (最大線程 20 個)。
        * ### 名稱爲 "process" 的 ProcessPoolExecutor (最大進程 5 個)。
        * ### UTC 時間作爲調度器的時區。
        * ### 默認爲新任務關閉合併模式。
        * ### 設置新任務的默認最大實例數爲 3。
    * ### 方法一
        ```
        from pytz import utc
        
        from apscheduler.schedulers.background import BackgroundScheduler
        from apscheduler.jobstores.mongodb import MongoDBJobStore
        from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
        from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
        
        
        jobstores = {
            'mongo': MongoDBJobStore(),
            'sql': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
        }
        
        executors = {
            'thread': ThreadPoolExecutor(20),
            'process': ProcessPoolExecutor(5)
        }
        
        job_defaults = {
            'coalesce': False,
            'max_instances': 3
        }
        
        aBackgroundScheduler = BackgroundScheduler(
            jobstores=jobstores,
            executors=executors,
            job_defaults=job_defaults,
            timezone=utc
        )
        ```
    * ### 方法二
        ```
        from apscheduler.schedulers.background import BackgroundScheduler
        
        
        # The "apscheduler." prefix is hard coded
        aBackgroundScheduler = BackgroundScheduler({
            'apscheduler.jobstores.mongo': {
                 'type': 'mongodb'
            },
            'apscheduler.jobstores.sql': {
                'type': 'sqlalchemy',
                'url': 'sqlite:///jobs.sqlite'
            },
            'apscheduler.executors.thread': {
                'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
                'max_workers': '20'
            },
            'apscheduler.executors.process': {
                'type': 'processpool',
                'max_workers': '5'
            },
            'apscheduler.job_defaults.coalesce': 'false',
            'apscheduler.job_defaults.max_instances': '3',
            'apscheduler.timezone': 'UTC',
        })
        ```
    * ### 方法三
        ```
        from pytz import utc
        
        from apscheduler.schedulers.background import BackgroundScheduler
        from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
        from apscheduler.executors.pool import ProcessPoolExecutor
        
        
        jobstores = {
            'mongo': {'type': 'mongodb'},
            'sql': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
        }
        
        executors = {
            'thread': {'type': 'threadpool', 'max_workers': 20},
            'process': ProcessPoolExecutor(max_workers=5)
        }
        
        job_defaults = {
            'coalesce': False,
            'max_instances': 3
        }
        
        aBackgroundScheduler = BackgroundScheduler()
        
        # 這裏可以添加任務...
        
        aBackgroundScheduler.configure(
            jobstores=jobstores,
            executors=executors,
            job_defaults=job_defaults,
            timezone=utc
        )
        ```
* ### 啓動調度器
    * ### 啓動調度器僅需調用 start() 即可。
    * ### 除了 BlockingScheduler，非阻塞調度器都會立即返回，可以繼續運行之後的代碼，比如添加任務等。
    * ### 對於 BlockingScheduler，程序則會阻塞在 start() 位置，所以，要運行的代碼必須寫在 start() 之前。
    * ### 調度器啓動後配置將無法修改。
* ### 添加任務
    * ### 添加任務的方法
        * ### 調用 add_job() 方法
        * ### 使用 scheduled_job() 裝飾器
    * ### 第一種方法是最常用的；第二種方法是最方便的，但缺點就是運行時不能修改任務。
    * ### add_job() 方法會返回一個 apscheduler.job.Job 實例，可以在運行時修改或刪除任務。
    * ### 任何時候都能配置任務，但若調度器尚未啓動，此時添加任務，其會處於一個暫存的狀態，只有當調度器啓動時才會開始計算下次運行時間。
    * ### 如果執行器或任務儲存器會將任務序列化，那麼這些任務就必須符合下方兩點:
        * ### 回調函數必須全局可用。
        * ### 回調函數參數必須也是可以被序列化的。
        * ### MemoryJobStore 不會序列化任務；ProcessPoolExecutor 會序列化任務。
    * ### 在程序初始化時，若任務是從數據庫讀取，那麼必須爲每個任務定義一個明確的 ID，並且使用 ```replace_existing=True```，否則每次重啓程序，都會得到一份新的任務拷貝，也就意味着任務的狀態不會保存。
    * ### 若想要立刻運行任務，可以在添加任務時省略 trigger 參數。
* ### 移除任務
    * ### 如果想從調度器移除一個任務，需從相應的任務儲存器中移除它。
    * ### 移除任務的方法
        * ### 調用 remove_job() 方法，參數爲任務 ID。
        * ### 在通過 add_job() 創建的任務實例上調用 remove() 方法。
    * ### 第二種方法較方便，但必須在創建任務實例時將其保存在變量中。
    * ### 對於通過 scheduled_job() 創建的任務則只能選擇第一種方式。
    * ### 當任務調度結束時 (例如某個任務的觸發器不再產生下次運行的時間)，該任務就會自動移除。
    ```
    job = scheduler.add_job(myfunc, 'interval', minutes=2)
    job.remove()
    ```
    ```
    scheduler.add_job(myfunc, 'interval', minutes=2, id='my_job_id')
    scheduler.remove_job('my_job_id')
    ```
* ### 暫停和恢復任務
    * ### 通過任務實例或調度器，就能暫停和恢復任務。
    * ### 如果一個任務被暫停了，那麼該任務的下一次運行時間就會被移除。
    * ### 在恢復任務前，運行次數計數也不會被統計。
    * ### 暫停任務的方法
        ```
        apscheduler.job.Job.pause()
        ```
        ```
        apscheduler.schedulers.base.BaseScheduler.pause_job()
        ```
    * ### 恢復任務的方法
        ```
        apscheduler.job.Job.resume()
        ```
        ```
        apscheduler.schedulers.base.BaseScheduler.resume_job()
        ```
* ### 獲取任務列表
    * ### 通過 get_jobs() 方法可以獲得一個可修改的任務列表。
    * ### get_jobs() 方法的第二個參數可以指定任務儲存器的名稱以獲得對應任務儲存器的任務列表。
    * ### print_jobs() 方法可以快速打印格式化的任務列表 (含觸發器與下次運行時間等信息)。
* ### 關閉調度器
    ```
    scheduler.shutdown()
    ```
    * ### 默認情況下調度器會先把正在執行的任務處理完才關閉任務儲存器和執行器。
    * ### 若想強制關閉調度器可以透過指定 wait 參數值為 False 達成。
        ```
        scheduler.shutdown(wait=False)
        ```
* ### 暫停與恢復任務進程
    * ### 調度器暫停正在執行的任務
        ```
        scheduler.pause()
        ```
    * ### 調度器恢復已被暫停的任務
        ```
        scheduler.resume()
        ```
    * ### 也可以在調度器啓動時默認所有任務設爲暫停狀態
        ```
        scheduler.start(paused=True)
        ```
* ### 限制任務執行的實例並行數
    * ### 默認情況下，在同一時間，一個任務只允許一個執行中的實例在運行。
    * ### 比如說，一個任務是每 5 秒執行一次，但是這個任務在第一次執行的時候花了6秒，也就是說前一次任務還沒執行完，後一次任務又觸發了，由於默認一次只允許一個實例執行，所以第二次就丟失了。
    * ### 爲了杜絕這種情況，可以在添加任務時，設置 max_instances 參數，爲指定任務設置最大實例並行數。
* ### 丟失任務的執行與合併
    * ### 有時，任務會由於一些問題沒有被執行。
    * ### 最常見的情況就是，在數據庫裏的任務到了該執行的時間，但調度器被關閉了，那麼這個任務就成了 "啞彈任務"。
    * ### 錯過執行時間後，調度器纔打開了，這時，調度器會檢查每個任務的 misfire_grace_time 參數 int 值，即啞彈上限，來確定是否還執行啞彈任務 (這個參數可以全局設定的或者是爲每個任務單獨設定)。
    * ### 此時，一個啞彈任務，就可能會被連續執行多次。
    * ### 但這就可能導致一個問題，有些啞彈任務實際上並不需要被執行多次。
    * ### coalescing 合併參數就能把一個多次的啞彈任務揉成一個一次的啞彈任務。
    * ### 也就是說，coalescing 爲 True 能把多個排隊執行的同一個啞彈任務，變成一個，而不會觸發啞彈事件。
    * ### 如果是由於線程池 or 進程池滿了導致的任務延遲，執行器就會跳過執行。
    * ### 要避免這個問題，可以添加進程或線程數來實現或把 misfire_grace_time 值調高。
* ### 調度器事件
    * ### 文檔 -> [click me](https://apscheduler.readthedocs.io/en/latest/modules/events.html#module-apscheduler.events)
    * ### 調度器允許添加事件偵聽器。
    * ### 部分事件會有特有的信息，比如當前運行次數等。
    * ### add_listener(callback, mask) 中，第一個參數是回調對象，mask 是指定偵聽事件類型，mask 參數也可以是邏輯組合。
    * ### 回調對象會有一個參數就是觸發的事件。
    ```
    def my_listener(event):
        if event.exception:
            print("The job crashed :(")
        else:
            print("The job worked :)")
    
    # 當任務執行完或任務出錯時調用 my_listener
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    ```
* ### 異常捕獲
    * ### 通過 logging 模塊，可以添加 apscheduler 日誌至 DEBUG 級別，這樣就能捕獲異常信息。
    ```
    import logging
    
    logging.basicConfig()
    logging.getLogger('apscheduler').setLevel(logging.DEBUG)
    ```
<br />
