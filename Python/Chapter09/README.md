Chapter09
=====
* ### 一個物件被稱為 hashable，其必須有 hash 值，這個值在執行其不會有變化，且須可進行相等比較，即當一物件能被稱為 hashable，其必須實作 \_\_hash\_\_() 與 \_\_eq\_\_() 方法。
* ### 對於 Python 內建型態來說，建立後狀態無法變動 (Immutable) 的型態，其實例都是 hashable，而可變動 (Mutable) 的型態實例，都是 unhashable。
* ### 一個字定義類別建立實例，預設為 hashable，其 \_\_hash\_\_() 基本透過 id() 計算，而 \_\_eq\_\_() 預設使用 is 比較，因此兩個實例之 hash 值必然不同，相等性比較一定不成立。
* ### 當 set 判斷新加入物件已存在其中 (hash 相同且相等比較成立) 時，會將舊物件丟棄並加入新物件。
* ### 兩物件，若相等比較成立則 hash 必須相同，但 hash 相同時相等比較未必要成立。
* ### 迭代器具有 \_\_next\_\_() 方法，可以迭代出物件中資訊，若無法迭代會引發 StopIteration。
* ### 迭代器具有 \_\_iter\_\_() 方法，傳回迭代器本身，因此每一個迭代器也是一個 iterable 物件。
* ### Python 標準程式庫中提供 itertools 模組，可用於建立迭代器或產生器。
* ### list 才有 sort() 方法，其它 iterable 物件要進行排序則使用 sorted() 函式，但其不會變動到原本的物件，會傳回排序後的新物件。
* ### 若希望在自訂類別中使用排序方法 sorted() 或是 sort()，需預設排序定義，即為實作 \_\_lt\_\_() 方法。
* ### Python 中大致將集群分為三種型態，循序 (Sequences)、集合 (Set)、映射 (Mapping)。
* ### 不可變動的循序類型，具有預設的 hash() 實作，如: tuple、str 與 bytes。
* ### 集合類型是無序的，其元素必須為 hashable 物件且不會重複。
* ### set 本身是可變動的，若需要不可變動的集合類型，可使用 frozenset() 來建立。
* ### 對於佇列或雙向佇列來說，使用 list 實作效率並不好，建議使用 collections 模組中的 deque 類別。
* ### tuple 狀態不可變動，較省記憶體。
* ### 可透過 collections 模組中的 namedtuple() 函式建立擁有欄位名稱的實例。
* ### 應避免過度設計資料結構，Tuple 要比物件好 (namedtuple)，簡單的欄位會比 Getter / Setter 函式要好。
* ### 若需要在建立 dict 時保有最初鍵值加入的順序，可使用 collections 模組的 OrderedDict。
* ### defaultdict 的第一個參數為 default_factory 屬性提供初始值，默認為 None，可為一個不存在的鍵提供默認值，從而避免 KeyError 異常。
* ### 若想在自定義實作中實現 [] 取值，需實作 \_\_getitem\_\_()，實現 [] 設值則實作 \_\_setitem\_\_()，透過 del 與 [] 刪除實作 \_\_delitem\_\_()。
* ### 可自定義 \_\_len\_\_() 方法計算群集長度並傳回。
* ### collections.abc 模組提供實作群集的基礎類別，可用於繼承，且其提供一些基本的共用實作。
