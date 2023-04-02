Chapter01 簡介 Asyncio
=====
* ### Python 3 的 Asyncio: 可以在一個程式中執行多個並行 (concurrent) 的 HTTP 請求。
* ### Asyncio 的重點著重在，涉及到等待作業時，等待某作業完成的當下，可以去執行其它作業。
* ### 現代的電腦程式運行時，CPU 的運作效率會比網路訊息傳輸快上幾十萬倍，因此，很高機率會有一段時間都在等等等。
* ### Asyncio 可理解為明確要求 CPU 轉換作業，運用等待的空閒時間，除了可以用較少的 CPU 達到不錯的效能，還能避免競速 (race condition) 問題。
* ### 對於 I/O 密集式作業不使用執行緒而使用 Asyncio 的原因
    * ### 相較於先佔式多工 (preemptive multitasking)，也就是執行緒，Asyncio 更為安全，可以避免複雜執行緒應用程式上常見的臭壞蟲蟲、競速與其它風險。
    * ### Asyncio 提供簡明的 socket 連線支援方式，類似處理多個 WebSocket 長時連線或是 IoT (Internet of Things) 應用程式的 MQTT。
* ### 不正確的認知
    * ### Asyncio 可以讓程式碼快到飛起來
        * ### 基本上執行緒地執行速度應該還是會快於 Asyncio，但 Asyncio 在建立大量並行任務時相對輕量，且透過協程 (coroutine) 能避免環境切換 (context switching) 成本。
        * ### 本質上不要認為 Asyncio 是一個速度效率上的提升方案。
        * ### 在現在硬體上的 Linux 中，一次的執行緒環境切換大約是 50 微秒，一千個執行緒環境切換的總成本約為 50 毫秒，這確實是個負擔，但也不致於毀滅...
    * ### Asyncio 讓執行緒顯得多餘: 在 CPU 密集式的作業上，執行緒永遠是最佳的選擇方案。
    * ### Asyncio 避免了 GIL 的問題
        * ### Asyncio 確實不受 GIL 影響，因為 Asyncio 在定義上是單執行緒的。
        * ### GIL 是阻礙了真正的多核平行 (paralleism)。
    * ### Asyncio 可以避免競速: 與其說 Asyncio 避免了多執行緒所遇到的競速問題，不如說因為其可以看出在 coroutine 間執行權的轉換 (拜 await 所賜)，所以更加容易推導出共享資源的存取方式。
    * ### Asyncio 簡化了並行程式設計: 並行永遠是複雜的。
* ### 記住，Asyncio 在定義上是單執行緒的 !
* ### 如果各項作業很短暫，也就是至少或只會執行一小段時間，Asyncio 會很有效率，但若有作業持續長時間佔用 Asyncio，就會影響到整體的運行。
* ### 全局解譯器鎖 (Global Interpreter Lock, GIL): 藉由鎖定每個操作碼 (opcode)，確保 Python 解譯器的程式碼 (不是開發者的程式碼) 是執行緒安全，帶來的負面效應是，解譯器會被釘在單一 CPU 上執行，因而阻礙了多核平行化。
<br />
