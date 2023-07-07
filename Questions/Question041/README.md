Question041 - 什麼是 Call Stack ?
=====
* ### 每當函式在執行且還沒結束時，都會在記憶體上生成 Call Stack，Call Stack 會決定現在應該執行哪一個副函式 (Call Stack 會先執行 Stack 最上面的函式)。
```
def main():
    print("start")
    func()
    print("end")

def func():
    print("func()")

if __name__ == '__main__':
    main()
```
* ### 程式一開始會遇到 main() 函式，所以會在 Call Stack 上生成並且執行它。
* ### 執行完 print("start") 後遇到 func() 函式，由於 main() 函式還沒結束所以 Call Stack 不會將它移除，而是將 func() 函式加到 main() 函式上 (加入 Call Stack) 面並且執行 func() 函式。
* ### 執行完 print("func()") 後可以發現 func() 函式已經執行完了，所以它會從 Call Stack 上被移除。
* ### 然後回來繼續執行 main() 函式直到它結束，後再從 Call Stack 將其移除移除。
<br />
