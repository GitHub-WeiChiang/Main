Question042 - 網頁架構 DOM 是什麼 ?
=====
* ### 文件物件模型 (Document Object Model, DOM): 將一份 HTML 文件內的各個標籤 (包括文字與圖片等等) 定義成物件，而這些物件最終會形成一個樹狀結構。
* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/Questions/Question042/DOM.png)
* ### DOM 將每個 element、文字 (text) 等等都視為一個節點 (Node)，通常有以下四種:
    * ### Document (Root Node): 該份文件，也就是 HTML 檔。
    * ### Element: 文件內的各個標籤，如 ```<div>``` 與 ```<p>``` 等 HTML Tag 都被歸類於此。
    * ### Text: 被標籤所涵括的文字，如 ```<h1>Hello World</h1>``` 中 "Hello World" 被 ```<h1>``` 這個 Element 所涵括，因此 "Hello World" 就是該 Element 的 Text。
    * ### Attribute: 各個標籤內的相關屬性。
* ### Example
    ```
    <html>
        <head>
            <title>example</title>
        </head>
        <body>
            <h1 class="txt">hello world</h1>
        </body>
    </html>
    ```
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/Questions/Question042/DomTree.png)
* ### DOM 的關係
    * ### 父子關係 (Parent And Child)
    * ### 兄弟關係 (Siblings)
* ### DOM 的操作
    * ### document.getElementById('ID_NAME'): 找尋 DOM 中符合此 ID_NAME 的元素，並回傳相對應的 element 。
    * ### document.getElementsBytagName('TAG_NAME'): 找尋 DOM 中符合此 TAG_NAME 的所有元素，並回傳相對應的 element 集合，集合為 HTMLCollection。
    * ### document.getElementsByClassName('CLASS_NAME'): 找尋 DOM 中符合此 CLASS_NAME 的所有元素，並回傳相對應的 element 集合，集合為 HTMLCollection。
    * ### document.querySelector('SELECTOR'): 利用 SELECTOR 來找尋 DOM 中的元素，並回傳相對應的第一個 element。
    * ### document.querySelectorAll('SELECTOR'): 利用 SELECTOR 來找尋 DOM 中的所有元素，取得所有符合條件的 HTML 元素集合 (NodeList)。
* ### HTMLCollection vs. NodeList
    * ### HTMLCollection: 集合內元素為 HTML element，因此 Node type 只能是 Element。
    * ### NodeList: 集合內元素為 Node，因此可以接受所有的 Node。
<br />
