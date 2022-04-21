Chapter04
=====
* ### Python 惰性求值，函數式編程高效，原因之一是將計算推遲到需要的時候進行。惰性 (也稱 "非嚴格") 求值非常重要，Python 內置了對它的支持。
* ### Python 函式中可以定義函式，稱為區域函式 (Local function)。
* ### Python 語法上不直接支援函式重載 (Overload)，名稱相同的函數定義時，後覆蓋前。
* ### Python 中可以使用預設引數 (參數預設值)，有限度的模仿函式 Overload。
* ### 使用參數預設值時，要注意指定可變動物件的陷阱，避免方法為設定預設參數值為 None。
* ### 若函式擁有固定參數，而寫傳入序列 (list、tuple) 時，只要在傳入時加上 *，則 list 或 tuple 中的元素就會自動拆解給各參數。
* ### 無法預期傳入參數引數個數時，可以在定義函式參數時使用 *，傳入函式的引數，會被收集在一個 tuple 中。
* ### 依鍵名稱指定給對應的參數名稱，在 dict 前加上 **。
* ### 當函數傳入參數過多且各有意義，可以在宣告函數參數時加上 ** 定義，讓指定的關鍵字引數收集為一個 dict。
* ### Python 的函式為一級函式 (First - class function)。
* ### map(func, sequence)，定義一個 function，接著用這個 function來對一個 iterable 的物件內每一個元素做處理。
* ### Lambda 函式支援 IIFE (immediately invoked function expression) 語法，意思是利用 function expression 的方式來建立函式，並立即執行。
* ### Python 中的全域，實際上是以模組檔案為界。
* ### dir() 函是可以查詢指定物件上可取用名稱，Python 中可以直接使用的函示在 builitins 模組中。
* ### locals() 可以查詢區域變數的名稱與值。
* ### nonlocal 可指明變數非區域變數，讓直譯器依順序尋找使用。
* ### yield 產生器，似 return，但函式不會因為 yield 結束，只是將流程控制權讓給函式的呼叫者。
* ### 當使用 yield 指定一個值時，呼叫該函式會傳回一個 generator 物件，也就是一個產生器，此物件具有 \_\_next\_\_() 方法，因此也是個迭代器，通常會使用 next() 函是呼叫該方法取出下個產生值 (也就是 yield 指定值)。
* ### yield 除可透過 \_\_next\_\_() 方法取得右側指定值，還可透過 send() 方法指定值，令其成為 yield 的運算結果。
* ### 函數加入 yield 後不再是一般的函數，而被視作為生成器 (generator)，呼叫函數後，回傳的並非數值，而是函數的生成器物件。
* ### 回傳值可能為 None 的型態提示 typing 寫法 -> Union[type, None] 或是 -> Optional[int]。
