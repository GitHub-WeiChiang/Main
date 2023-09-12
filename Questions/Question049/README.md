Question049 - 有沒有什麼通用的高效序列化模組 ? JIT 是什麼概念 ?
=====
* ### 基於 JIT 的高性能多語言原生序列化框架 FURY。
* ### 理解更多 -> [click me](https://github.com/alipay/fury)
* ### 安裝
    ```
    pip install pyfury --pre
    ```
* ### Quickstart
    ```
    import pyfury

    from typing import Dict

    class SomeClass:
        f1: "SomeClass"
        f2: Dict[str, str]
        f3: Dict[str, str]

    fury = pyfury.Fury(ref_tracking=True)
    fury.register_class(SomeClass, "example.SomeClass")

    obj = SomeClass()
    obj.f2 = {"k1": "v1", "k2": "v2"}
    obj.f1, obj.f3 = obj, obj.f2

    data = fury.serialize(obj)

    print(fury.deserialize(data))
    ```
* ### 即時編譯 (JIT, Just-In-Time Compilation)
    * ### 直譯 (Interpretation): 直譯器逐行讀取並執行程式碼，一次只處理一行程式碼，執行速度相對較慢，因每次運行都需要解釋和執行程式碼。
    * ### 編譯 (Compilation): 編譯器會將整個程式碼轉換為機械碼或其他低階語言的二進制表示形式，然後執行這個二進制檔案，通常會提高執行速度，但編譯過程需要額外的時間。
    * ### JIT 編譯是一種結合了這兩種方法的技術，程式碼首先被直譯器解釋和執行，但同時也被動態編譯成機械碼或本機語言，這些編譯後的程式碼片段被存儲在記憶體中，以供未來的執行使用，當同一段程式碼需要再次執行時，不需要再次解釋，而是直接使用已編譯的機械碼，從而提高了執行速度。
    * ### JIT 編譯通常用於動態語言 (如 Java、C# 與 Python 等) 的執行環境中，因為這些語言的程式碼在執行時才被解釋和執行。
    * ### JIT 編譯可以幫助提高這些語言的執行效率，減少了每次執行時的解釋成本，同時也允許針對特定硬體和優化機會進行優化。
<br />
