Chapter11
=====
* ### time 模組提供一層介面，用於呼叫各平台上的 C 程式庫函式。
* ### UNIX 時間，或稱 POSIX 時間是 UNIX 系統使用的時間表示方式: 從 UTC 1970 年 1 月 1 0 時 0 分 0 秒起至現在的總秒數，不考慮閏秒修正 (epoch 的一種)。 
* ### time 模組提供低階機器時間觀點，也就是從 epoch 起經過的秒數。
* ### datetime 模組提供以人類觀點表達的時間。
* ### datetime 預設沒有時區資訊，可透過 timezone (tzinfo 的子類) 提供基本 UTC 偏移時區實作。
* ### 通常以 UTC 進行時間儲存，因其為絕對時間，不考量日光節約時間等問題。
* ### 夏令時間 (daylight time)，又稱夏令時、日光節約時間 (daylight saving time，DST)，是一種在夏季月份犧牲正常的日出時間，而將時間調快的做法。通常使用夏令時間的地區，會在接近春季開始的時候，將時間調快一小時，並在秋季調回正常時間。實際上，夏令時間會造成在春季轉換當日的睡眠時間減少一小時，而在秋季轉換當日則會多出一小時的睡眠時間。
* ### 通常一個模組只需要一個 Logger 實例，雖然可以直接建構 Logger 實例，但建議透過 logging.getLogging() 取得 Logger 實例。
* ### 呼叫 getLogger() 時，可以指定名稱，相同名稱下取得的 Logger 會是同一個實例。
* ### 日誌等級與其值 (預設為大於 30 才輸出)
    * ### NOTSET = 0
    * ### DEBUG = 10
    * ### INFO = 20
    * ### WARNING = 30
    * ### ERROR = 40
    * ### CRITICAL = 50
* ### setLevel() 可以調整日誌層級，logging.basicConfig() 可以調整根 Logger 的組態 (日誌層級)。
* ### 透過 debug()、info()、warning()、error() 與 critical() 等方法直接指定日誌等級。
* ### 透過 logging.basicConfig(filename = "") 指定輸出檔案。
* ### 透過 logging.Formatter() 建立 Formatter 實例，再透過 setFormatter() 自訂 log 格式。
* ### 可以使用函式作為 Logger 的過濾器。
* ### 使用 logging.config.dictConfig() 設定組態資訊 (組態資訊中必須要有 version)。
* ### re 模組用於 regular expression。
* ### 字串前加上 r，表示此為原始字串 (Raw string)，不對任何 \ 進行轉義 (Escape Character)。
* ### 跳脫字元 = 轉義字元。
* ### 撰寫正則表達式建議使用原始字串。
* ### 字面字元 (Literals) 指按照字面意義比對的字元。
* ### 詮譯字元 (Metacharacters) 不按照字面比對，在不同情境有不同意義的字元。
* ### 若要比對詮譯字元需加上轉義符號。
* ### 多字元可以歸類為字元類 (Character class)，規則表達式中被放在 [] 中的字元就是一個字元類。
* ### | 在字元類中只是普通字元，不會被當成 or 表示。
* ### 字元類中可以使用 - 表示一段文字範圍。
* ### [^] 為反字元類 (Negated character class)。
* ### 字元類縮寫 = 預定義字元類 (Predefined character class)
    * ### . 任一字元。
    * ### \d 任一數字。
    * ### \D 任一非數字。
    * ### \s 任一空白字元。
    * ### \S 任一非空白字元。
    * ### \w 任一 ASCII 字元。
    * ### \W 任一非 ASCII 字元。
* ### 貪婪量詞 (Greedy quantifier)
    * ### ? 出現一次或沒有。
    * * ### 出現零次或多次。
    * ### + 出現一次或多次。
    * ### {n} 出現 n 次。
    * ### {n,} 至少出現 n 次。
    * ### {n, m} 出現 n 次但不超過 m 次。
* ### 貪婪量詞會盡可能地找出長度最長的符合文字。
* ### 貪婪量詞後加上 ? 將會成為逐步量詞 (Reluctant quantifier)，又稱為懶惰量詞或非貪婪 (non-greedy) 量詞。
* ### 逐步量詞會盡可能地找出長度最短的符合文字。
* ### 邊界比對需透過錨點 (Anchor)。
    * ### ^ 一行開頭。
    * ### $ 一行結尾。
    * ### \b 單字邊界。
    * ### \B 非單字邊界。
    * ### \A 輸入開頭。
    * ### \G 前一個符合項目結尾。
    * ### \Z 比對必須發生在字串結尾，或發生在字串結尾的 \n 之前。
    * ### \z 比對只能發生在字串結尾。 
* ### 分組回頭參考 (Back reference)，是在 \ 後加上分組計數，表示參考第幾個分組的比對結果。
* ### 擴充標記 (Extension notation)，使用 (?:...) 表示不捕捉分組。
* ### 剖析、驗證正則表達式非常耗時，當頻繁使用時，重複使用可以提高效能，透過 re.compile() 建立正則表達式物件。
* ### 可以在正則表達式中使用嵌入旗標表示法 (Embedded Flag Expression)。
* ### re.compile() 中的方法:
    * ### finditer() 函數取得符合後的進一步資訊。
    * ### search() 函數找尋字串中第一個符合字串。
    * ### match() 函數指在開頭判斷接下來字串是否符合。
    * ### findall() 函數以清單傳回各分組。
    * ### sub() 函數用於字串取代。
* ### os.path 模組支援路徑組合、相對路徑轉絕對路徑與取得檔案所在目錄路徑等，避免應用程式與作業系統相依問題。
* ### URL (Uniform Resource Locator)，路徑。
* ### URI (Uniform Resource Identifier)，資源實際位置。
