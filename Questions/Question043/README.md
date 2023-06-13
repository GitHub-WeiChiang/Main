Question043 - JS 中 ```<script>``` 標籤的 async 和 defer 屬性作用為何 ?
=====
```
<script src="demo_defer.js" defer></script>
```
* ### Definition and Usage
    * ### The ```defer``` attribute is a boolean attribute.
    * ### If the ```defer``` attribute is set, it specifies that the script is downloaded in parallel to parsing the page, and executed after the page has finished parsing.
* ### Note
    * ### The ```defer``` attribute is only for external scripts (should only be used if the ```src``` attribute is present).
* ### There are several ways an external script can be executed:
    * ### If ```async``` is present: The script is downloaded in parallel to parsing the page, and executed as soon as it is available (before parsing completes)
    * ### If ```defer``` is present (and not ```async```): The script is downloaded in parallel to parsing the page, and executed after the page has finished parsing
    * ### If neither ```async``` or ```defer``` is present: The script is downloaded and executed immediately, blocking parsing until the script is completed
* ### 總結
    ```
    # 當 JS 單純的與 HTML 寫在一起時 (非外部檔案)
    document.addEventListener("DOMContentLoaded", function() {
        // DOM Ready!
    });

    # 引入為外部檔案且依賴 DOM 載入完成時
    <script src="your-script.js" defer></script>

    # 引入為外部檔案但不依賴 DOM 載入時
    <script src="your-script.js" async></script>
    ```
    ```
    # 這是 jQuery 的 ready() 函數: 對於老舊瀏覽器的支援程度較為友善
    $(document).ready(function() {
        // DOM Ready!
    });

    # The load event is fired when the whole page has loaded,
    # including all dependent resources such as stylesheets,
    # scripts, iframes, and images.
    window.addEventListener("load", function(event) {
        // All resources finished loading!
    });
    ```
<br />
