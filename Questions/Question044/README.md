Question044 - Python 的 yield 產生器是什麼 ?
=====
* ### 示例代碼
    ```
    def xrange(n):
        x = 0
        while x != n:
            yield x
            x += 1

    for n in xrange(10):
        print(n)
    ```
    * ### xrange() 函式首次執行時，使用 yield 產生 x。
    * ### 回到主流程使用 print() 顯示值，接著流程重回 xrange 函式。
    * ### 執行 yield 之後代碼，迴圈中再次使用 yield 產生 x。
    * ### 回到主流程使用 print() 顯示值，反覆直至 xrange() 的迴圈結束。
* ### 實際上當函式中使用 yield 產生值時，呼叫該函式會傳回產生器 (generator) 物件，此物件具有 __next__() 方法，用於取出下個產生值，若無法產生下一個值則會引發 StopIteration 例外。
    ```
    >>> g = xrange(2)
    >>> type(g)
    <class 'generator'>
    >>> next(g)
    0
    >>> next(g)
    1
    >>> next(g)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration
    >>>
    ```
    * ### 因此 for 迴圈實際上是對 xrange 傳回的產生器進行迭代，若物件具有 __next__() 方法，for 迴圈會呼叫 __next__() 方法取得值，並在遇到 StopIteration 時結束。
* ### 每次呼叫產生器的 __next__() 時，產生器才會運算並傳回下個產生值，因此其具有惰性求值的效果。
* ### send() 方法
    * ### yield 是個運算式，除了可以呼叫產生器的 __next__() 方法，取得 yield 右方的值，還可以透過 send() 方法指定值，令其成為 yield 運算結果。
    * ### 也就是產生器可以給呼叫者值，呼叫者也可以指定值給產生器，形成了一種溝通機制。
    ```
    import sys
    import random


    def producer():
        while True:
            data = random.randint(0, 9)
            print('生產了：', data)
            yield data


    def consumer():
        while True:
            data = yield
            print('消費了：', data)


    def clerk(jobs, prod, cons):
        print('執行 {} 次生產與消費'.format(jobs))
        p = prod()
        c = cons()
        next(c)  
        for i in range(jobs):
            data = next(p)
            c.send(data)


    if __name__ == '__main__':
        clerk(2, producer, consumer)

    
    # 執行 2 次生產與消費
    # 生產了： 8
    # 消費了： 8
    # 生產了： 9
    # 消費了： 9
    ```
    * ### send() 方法的引數會是 yield 的運算結果。
    * ### 因此 clerk() 流程中必須先使用 next，使得流程首次執行至 consumer 函式中的 data = yield 處 (此處會執行 yield)。
    * ### 後會令流程回到 clerk() 函式，之後執行至 next()，使得流程進行至 producer() 函式的 yield data。
    * ### 在 clerk 取得 data 之後，執行 c.send(data)，這時流程回到 consumer() 先前 data = yield 處。
    * ### send() 方法的引數此時成為 yield 的結果。
    * ### 結語: Python 沒那麼困難，是工程師們讓 Python 變得複雜了，其實，Python 非常單純。
    * ### 所以沒事別這樣寫程式 !
* ### yield from
    * ### 若想建立一個產生器函式，而資料來源是另一個產生器。
    * ### 例如 range() 函式將傳回產生器，而目標為建立一個 np_range() 函式，可以產生指定數字的正負範圍 (不包含 0)。
    ```
    def np_range(n):
        for i in range(0 - n, 0):
            yield i

        for i in range(1, n + 1):
            yield i


    print(list(np_range(2)))
    # [-2, -1, 1, 2]
    ```
    * ### 因為 np_range() 必須是產生器，結果就是得逐一從來源產生器取得資料，再將之 yield。
    * ### 在 Python 3.3 中新增了 yield from 語法:
        ```
        def np_range(n):
            yield from range(0 - n, 0)
            yield from range(1, n + 1)


        print(list(np_range(2)))
        # [-2, -1, 1, 2]
        ```
<br />
