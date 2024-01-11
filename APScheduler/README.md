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
<br />
