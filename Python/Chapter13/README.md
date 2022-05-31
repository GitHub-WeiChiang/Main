Chapter13
=====
* ### 並行 -> threading。
* ### threading 模組可以運用執行緒在主流程以外獨立運行流程。
* ### 當 Thread 實例的 start() 方法執行時，指定的函式就會獨立地運行各自流程，而且「像是同時執行」。
* ### 必要時可繼承 threading.Thread，在 \_\_init\_\_() 中呼叫 super().\_\_init\_\_()，並在類別中定義 run() 方法來實作執行緒功能，但不建議，因其會使得流程與 threading.Thread 產生相依性。
* ### 實際上是否真的「同時」，要看處理器的數量，以及使用的實作品而定。
* ### 若只有一個處理器，在特定時間點上，處裡器只允許執行一個執行緒。
* ### 阻斷: 執行緒適用的場合之一，就是輸入輸出密集的場合，因為與其等待某個阻斷作業完成，不如趁著等待時間來進行其它的執行緒。
* ### 對於計算密集地任務，使用執行緒不見得會提高處裡效率，反而容易因為直譯器必須切換執行緒而耗費不必要的成本，使得效率變差。
* ### 執行緒預設要完全執行完畢才會結束，若希望執行緒隨著 main 執行緒結束而結束 (無論該執行緒是否執行完畢)，可透過設定 daemon 達成。
```
thread = Thread(target=xxx) 
thread.setDaemon(True)	
thread.start()
```
* ### 使用 join() 安插執行緒，待安插執行緒執行完畢才接續執行原本代碼。
* ### thread.join([timeout])，timeout 參數為可選參數，可指定 thread 線程最多可以霸占 CPU 資源的時間(以秒為單位)，默認直到 thread 執行結束 (進入死亡狀態) 才釋放 CPU 資源。
* ### 若要停止執行緒，需自行實作，讓執行緒跑完應有的流程。
* ### 執行緒的暫停與重啟也需視需求實作。
* ### 競速 (Race condition): 若執行緒之間需要共享的是可變動狀態的資料，就會有可能發生競速的狀況。
* ### 鎖定: 若要避免競速的情況發生，可以對資源被變更與取用時的關鍵程式碼進行鎖定。
* ### 死結 (Dead Lock): 因執行緒無法取得鎖定時會造成阻斷，若不正確使用 Lock 有可能造成效能低落與死結問題。
* ### threading.RLock 實現了可重入鎖 (Reentrant lock)，用於特殊需求。
* ### wait() 方法會先釋放鎖定，等待通知後再去爭取鎖定，成功爭取後繼續執行。
* ### notify() 會通知正在等待的執行緒，但無法預期哪一個執行緒會被通知，即便透過 notify_all()，也是所有等待的執行緒一同爭取鎖定。
* ### wait() 可以設定浮點數指定逾時，若等待超過指定時間，就自動嘗試取得鎖定並執行。
* ### notify() 可指定通知的執行緒數量，可能通知指定數量 (含) 以上的執行緒。
* ### 透過 queue.Queue 配合 threading.Thread 可以達到一進一出 (wait / notify) 的效果。
* ### queue 模塊實現了多生產者、多消費者隊列。這特別適用於消息必須安全地在多線程間交換的線程編程。模塊中的 Queue 類實現了所有所需的鎖定語義。
* ### class threading.Semaphore(value=1): A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release() call. The counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting until some other thread calls release().
* ### class threading.Barrier(parties, action=None, timeout=None): 可以設定一個柵欄並指定數量，如果有執行緒先來到這個柵欄，必須等待其它執行緒也來到這個柵欄，直到達到指定執行緒數量，才能繼續往下執行。
```
import threading

b = threading.Barrier(2, timeout=5)

def server():
    print("server")
    b.wait()
    print("__server")

def client():
    print("client")
    b.wait()
    print("__client")

if __name__ == "__main__":
    threading.Thread(target=server).start()
    threading.Thread(target=client).start()
```
