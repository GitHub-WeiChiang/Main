Chapter16 神兵利器 -- optimizer trace 的神奇功效
=====
```
SHOW VARIABLES LIKE 'optimizer_trace'
```
* ### 透過上述指令查詢 optimizer trace
    * ### enable 為 off 表示此功能預設為關閉。
    * ### one_line 為 off 表示適合人類觀看。
* ### 開啟 optimizer trace 功能
    ```
    SET optimizer_trace="enable=on";
    ```
* ### optimizer trace 的列
    * ### QUERY: 輸入的查詢敘述。
    * ### TRACE: 最佳化過程 JSON 格式文字。
    * ### MISSING_BYTES_BEYOND_MAX_MEN_SIZE: 要顯示的字太多，跟我想抱怨人生的話一樣多，此處顯示忽略了多少位元組的字在輸出。
    * ### INSUFFICIENT_PRIVILEGES: 是否有權查看執行計畫生成過程，預設為 0，有權，某些情況下會是 1，無權查看，嘿嘿。
* ### optimizer trace 使用步驟
    ```
    # 把這個功能給它打開
    SET optimizer_trace="enable=on";

    # 輸入查詢敘述
    SELECT ... FROM ...

    # 開始偷窺
    SELECT * FROM information_schema.OPTIMIZER_TRACE;

    # 可以重複上述兩步驟

    # 停止偷窺
    SET optimizer_trace="enable=off";
    ```
* ### 透過 optimizer trace 分析查詢最佳化工具的具體工作過程 (請查閱書籍 16-3 頁)。
* ### 最佳化過程 3 大階段
    * ### prepare 階段
    * ### optimize 階段 (基於成本的最佳化主要集中在此階段，這個過程深入分析了針對表單查詢的各種執行方案的成本)
    * ### execute  階段
<br />
