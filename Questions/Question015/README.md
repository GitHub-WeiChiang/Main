Question015 - threading 和 multiprocessing 差在哪 ?
=====
* ### threading 重點摘要
    * ### 透過 context-switch 的方式實現。
    * ### 透過 CPU 的不斷切換 (context-switch)，實現平行的功能。
    * ### 大量使用 threading 執行並行的功能時，會因為大量的 context-switch，「實現了程式並行的功能，但也因為大量的 context-switch，使得程式執行速度更慢」。
    * ### 在現在硬體上的 Linux 中，一次的執行緒環境切換大約是 50 微秒，一千個執行緒環境切換的總成本約為 50 毫秒，這確實是個負擔，但也不致於毀滅...
* ### multiprocessing 重點摘要
    * ### multiprocessing 在資料傳遞上，會因為需要將資料轉移至其他 CPU 上進行運算; 因此會需要考慮資料搬運的時間，而多核心真正的實現「平行運算的功能」，當任務較為複雜時，效率一定比較好。
    * ### 使用 multiprocessing 時盡可能不要讓核心相互進行數據交換與溝通。
<br />
