Question015 - threading 和 multiprocessing 有差嗎 ?
=====
* ### threading 重點摘要
    * ### 透過 context-switch 的方式實現。
    * ### 透過 CPU 的不斷切換 (context-switch)，實現平行的功能。
    * ### 大量使用 threading 執行平行的功能時，會因為大量的 context-switch，「實現了程式平行的功能，但也因為大量的 context-switch，使得程式執行速度更慢」。
* ### multiprocessing 重點摘要
    * ### multiprocessing 在資料傳遞上，會因為需要將資料轉移至其他 CPU 上進行運算; 因此會需要考慮資料搬運的時間，而多核心真正的實現「平行運算的功能」，當任務較為複雜時，效率一定比較好。
    * ### 使用 multiprocessing 時盡可能不要讓核心相互進行數據交換與溝通。
<br />
