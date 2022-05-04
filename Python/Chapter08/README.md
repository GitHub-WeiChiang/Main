Chapter08
=====
* ### readline() 或 readlines() 讀到的每一行，換行字元都一律換為 '\n'。
* ### 文字模式在寫入的情況下，任何 '\n' 都會備置換為 os.linesep 的值 (windows 就是 '\r\n')。
* ### open() 傳回的檔案物件，都實作了 \_\_iter\_\_() 方法，可以直接使用 for in 進行迭代。
* ### Python 的檔案讀取風格: 讀取一個檔案最好的方式，就是不要去 read!
* ### tell() 方法告知目前在檔案中的位移值，單位是位元組值，開頭位元值為 0。
* ### seek() 方法可以指定跳到哪個位移值。
* ### 執行 flush() 方法，將緩衝內容出清。
* ### 二進位模式時的檔案物件，擁有一個 readinto() 方法接受 bytearray 實例，可以直接將讀取到的資料傳入。
* ### open() 的參數
    * ### file: 第一個參數。
    * ### mode: 第二個參數，r (預設)、w、x (檔案須不存在，存在引發 FileExistsError)、a (附加)、b (二進)、t (預設值，文字模式)、+ (更新模式，讀取與寫入)。
    * ### buffering: 設置緩衝策略，預設自行決定大小 (通常為 4096 或 8192 位元組)，或隊互動文字檔案 (isatty() 為 True 時，例如 Windows 命令提示字元) 採用行緩衝 (line buffering)，設為 0 表示關閉緩衝，則不需要 flush() 方法。
    * ### encoding: 指定檔案文字編碼。
    * ### errors: Specifies different error handling scheme，預設回傳 ，如: ignore。
    * ### newline: Controls how universal newlines mode works.
    * ### closefd: Keeps the underlying file descriptor open when the file is closed.
    * ### opener: A custom opener used for low-level I/O operations.
* ### 如果資料的讀取來源或寫入目的地，並不是檔案而是記憶體中某個物件，可以使用 BytesIO 或 StringIO (可透過 getvalue() 取的寫入資料)。
