07 - 地理位置查詢
=====
* ### ".geojson" 檔案匯入 (以 taiwan.geojson 縣市行政界線資料為例)
    ```
    $ mongoimport FILE_NAME.geojson -c=COLLECTION_NAME
    ```
    * ### ```-c```: 指定資料匯入 test 資料庫中的資料表。
* ### geojson.io -> [click me](https://geojson.io/)
<br />

範例程式
=====
* ### 7_2.py: 查詢使用者目前所在縣市。
* ### 7_3.py: 查詢被某範圍完全涵蓋的區域。
* ### 7_4.py: 查詢某範圍內有哪些資料。
<br />
