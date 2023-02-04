Question021 - 先佔式多工與非先佔式多工的差異為何 ?
=====
* ### 先佔式多工 (Preemptive Multitasking): 作業系統可以讓系統正在執行中的行程公平使用電腦系統的 CPU 以及其它資源。只要執行中的行程超過作業系統所配置給此行程的 CPU 時段時，作業系統會立刻中斷這個行程並將控制權交給另一個正在等待的行程。　
* ### 非先佔式多工 (Non - Preemptive Multitasking): 又稱為協同式多工 (Cooperative Multitasking)，在此作業系統下，CPU 的控制權有可能被一個行程所佔用，除非該行程主動交出 CPU 的控制權，否則別的行程是沒有機會取得 CPU 的控制權。
<br />
