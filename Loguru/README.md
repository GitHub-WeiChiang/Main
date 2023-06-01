Loguru: 更爲優雅、簡潔的 Python 日誌管理模塊
=====
* ### Sample Code
    ```
    pip3 install loguru
    ```
    ```
    from loguru import logger

    if __name__ == '__main__':
        # 刪除預設處理程序
        logger.remove(handler_id=None)

        # 日誌文件的配置
        logger.add(
            # 文件路徑: 路徑 + 檔案名稱
            "./Log/{time}.log",
            # 文件編碼: utf-8
            encoding="utf-8",
            # 啟用多進程安全隊列: 使日誌調用非阻塞
            enqueue=True,
            # 分隔日誌文件: 每日 00:00 生成新文件
            rotation="00:00",
            # 日誌的最長保留時間: 僅保留兩個月內日誌檔案 (過期則刪除)
            retention="2 months",
            # 發送到接收器的最低嚴重級別: INFO
            level="INFO",
            # 啟用接收器處理日誌消息時發生錯誤的自動捕獲 (異常不會傳播到調用者，可防止應用程序崩潰)
            catch=True
        )
    ```
* ### 日誌級別
    | 級別 | 層級 | 使用 |
    |-----------|-----|--------------------|
    | TRACE | 5 | logger.trace() |
    | DEBUG | 10 | logger.debug() |
    | INFO | 20 | logger.info() |
    | SUCCESS | 25 | logger.success() |
    | WARNING | 30 | logger.warning() |
    | ERROR | 40 | logger.error() |
    | CRITICAL | 50 | logger.critical() |
* ### 快速裝逼: basic.py
* ### logger 默認採用 sys.stderr 標準錯誤輸出將日誌輸出到控制檯中。
* ### 將日誌同時輸出到其它的位置 (日誌文件): log_file.py
* ### 日誌內容的字符串格式化: log_format.py
* ### loguru 日誌常用參數配置解析
    * ### sink: 可以傳入 file、string、pathlib.Path、方法、logging 模塊 Handler。
    * ### level: 已記錄消息發送到接收器的最低嚴重級別。
    * ### format: 對記錄的消息進行格式化。
    * ### filter: 決定每個記錄的消息是否應該發送到接收器。
    * ### colorize: 是否應將格式化消息中包含的顏色標記轉換爲用於終端着色的 Ansi 代碼。
    * ### serialize: 發送到接收器之前，記錄的消息及其記錄是否應該首先轉換爲 JSON 字符串。
    * ### backtrace: 格式化的異常跟蹤是否應該向上擴展，超出捕獲點，以顯示生成錯誤的完整堆棧跟蹤。
    * ### diagnose: 異常跟蹤是否應該顯示變量值以簡化調試 (在 PRD 中應為 False)。
    * ### enqueue: 要記錄的消息在到達接收器之前是否應該首先通過多進程安全隊列 (日誌非阻塞調用)。
    * ### catch: 是否應該自動捕獲接收器處理日誌消息時發生的錯誤。
* ### 接收器 (sink) 為 "文件路徑" 時，可使用下列參數，且 add() 會返回該接收器的標識符。
    * ### rotation: 分隔日誌文件，何時關閉當前日誌文件並啓動一個新文件的條件。
    * ### retention: 可配置舊日誌的最長保留時間。
    * ### compression: 日誌文件在關閉時應轉換爲的壓縮或歸檔格式。
    * ### delay: 是否應該在配置了接收器之後立即創建文件，或者延遲到第一個記錄的消息 (默認爲 "False")。
    * ### mode: 與內置 open() 函數一樣的打開模式 (默認爲 a 附加模式)。
    * ### buffering: 內置 open() 函數的緩衝策略 (默認爲 1 行緩衝文件)。
    * ### encoding: 文件編碼與內置的 open() 函數相同。
* ### loguru 日誌常用方式
    * ### 動態啟用與停止日誌記錄: dynamic_log.py
    * ### 只輸出到文本，不輸出在 console: only_file.py
    * ### filter 配置日誌過濾規則: filter.py
    * ### format 配置日誌記錄格式化模板: format.py
* ### 其它格式化模板屬性
    * ### elapsed: 從程序開始經過時間差。
    * ### exception: 格式化異常。
    * ### extra: 用戶綁定屬性字典。
    * ### file: 日誌記錄調用文件。
    * ### function: 日誌記錄調用函數。
    * ### level: 記錄消息嚴重程度。
    * ### line: 源代碼行號。
    * ### message: 記錄消息 (未格式化)。
    * ### module: 日誌寄戶調用模塊。
    * ### name: 日誌記錄調用 __name__。
    * ### process: 日誌記錄調用進程名。
    * ### thread: 日誌記錄調用線程名。
    * ### time: 發出日誌調用的可感知本地時間。
* ### 通過 extra bind() 添加額外屬性: extra_bind.py
* ### level 配置日誌最低日誌級別: level.py
* ### rotation 配置日誌滾動記錄的機制
    ```
    # 每 200 MB 創建一個日誌文件，避免每個 log 文件過大
    from loguru import logger
    trace = logger.add('sample.log', rotation="200 MB")

    # 每天 6 點創建一個日誌文件
    from loguru import logger
    trace = logger.add('sample.log', rotation='06:00')

    # 每隔 2 周創建一個日誌文件
    from loguru import logger
    trace = logger.add('sample.log', rotation='2 week')
    ```
* ### retention 配置日誌保留機制
    ```
    # 設置日誌文件最長保留 7 天
    from loguru import logger
    trace = logger.add('sample.log', retention='7 days')
    ```
* ### compression 配置日誌壓縮格式
    ```
    # 使用 zip 文件格式保存
    from loguru import logger
    trace = logger.add('sample.log', compression='zip')
    ```
* ### serialize 日誌序列化: serialize.py
* ### Traceback 記錄 (異常追溯): catch.py
* ### logger.exception 實現異常的捕獲與記錄: exception.py
<br />
