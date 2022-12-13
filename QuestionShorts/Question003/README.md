synchronized 和 lock
=====
* ### 在 Java 中有兩種鎖，一種是內置鎖 synchronized，一種是顯示鎖 Lock，其中 Lock 鎖是可中斷鎖，而 synchronized 則爲不可中斷鎖。
* ### 所謂的中斷鎖指的是鎖在執行時可被中斷，也就是在執行時可以接收 interrupt 的通知，從而中斷鎖執行。
* ### 使用了 lockInterruptibly 方法就可以在一段時間之後，判斷它是否還在阻塞等待，如果結果爲真，就可以直接將它中斷 (透過 interrupt)。
```
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

publicclass InterruptiblyExample {
    public static void main(String[] args) throws InterruptedException {
        Lock lock = new ReentrantLock();

        // 創建線程 1
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    // 加鎖操作
                    lock.lock();
                    System.out.println("線程 1:獲取到鎖.");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                // 線程 1 未釋放鎖
            }
        });
        t1.start();

        // 創建線程 2
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                // 先休眠 0.5s，讓線程 1 先執行
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                // 獲取鎖
                try {
                    System.out.println("線程 2:嘗試獲取鎖.");
                    lock.lockInterruptibly(); // 可中斷鎖
                    System.out.println("線程 2:獲取鎖成功.");
                } catch (InterruptedException e) {
                    System.out.println("線程 2:執行已被中斷.");
                }
            }
        });
        t2.start();

        // 等待 2s 後,終止線程 2
        Thread.sleep(2000);
        if (t2.isAlive()) { // 線程 2 還在執行
            System.out.println("執行線程的中斷.");
            t2.interrupt();
        } else {
            System.out.println("線程 2:執行完成.");
        }
    }
}
```
```
線程 1:獲取到鎖.
線程 2:嘗試獲取鎖.
"執行線程的中斷.
線程 2:執行已被中斷.
```
* ### 但當我們嘗試將 lockInterruptibly 方法換成 lock 方法之後（其他代碼都不變），執行的結果就完全不一樣了。
```
線程 1:獲取到鎖.
線程 2:嘗試獲取鎖.
"執行線程的中斷.
```
* ### 通過顯示鎖 Lock 的 lockInterruptibly 方法來完成，它和 lock 方法作用類似，但 lockInterruptibly 可以優先接收到中斷的通知，而 lock 方法只能 “死等” 鎖資源的釋放。
* ### Thread.interrupt 的作用其实也不是中断线程，而是「通知线程应该中断了」。
* ### lock(): 若 lock 被 thread 取得，其它 thread 会进入 lock pool 状态，直到取得 lock；
* ### tryLock(): 若当下不能取得 lock，thread 就会放弃，可以设置一个超时时间参数，等待多久获取不到锁就放弃。
* ### lockInterruptibly(): 跟 lock() 情況一下，但是 thread 可以被 interrupt 通知中断，放弃继续等待锁。
<br />

synchronized 和 lock 的區別
=====
* ### lock 是一個接口 (介面)，synchronized 是關鍵字。
* ### synchronized 作用于代码块，反編譯後多了两个指令 monitorenter 與 monitorexit。即 JVM 使用 monitorenter 和 monitorexit 两个指令实现同步。
* ### synchronized 作用于方法，多了 ACC_SYNCHRONIZED 标记。即 JVM 通过在方法访问标识符 (flags) 中加入 ACC_SYNCHRONIZED 来实现同步功能。
* ### 遇到異常
    * ### synchronized 自動釋放佔有的鎖。
    * ### lock 需要手動在 finally 釋放避免死鎖。
* ### 中斷響應
    * ### lock 可以透過 interrupt 中斷等待。
    * ### synchronized 只能等待鎖的釋放。
* ### 是否知道獲取鎖
    * ### lock 透過 trylock 得知。
    * ### synchronized 無法得知。
* ### lock 可以提高多線程操作效率 (readwritelock)。
* ### lock 透過 condition 實現 synchronized 的 wait、notify、notifyAll 機制。
<br />
