Chapter06 Template 深入探討
=====
* ### settings.py 設定
    ```
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```
    * ### ```BACKEND```: 指定使用的模板引擎。
    * ### ```DIRS```: 指定 templates 網頁檔案放置位置。
    * ### ```APP_DIRS```: 設為 True 表示先在當前 App 的 templates 資料夾尋找對應模板，沒找到再至 DIRS 設定的路徑尋找，還是沒找到則引發 TemplateDoesNotExist 例外。
* ### render(): Template Engine(變數 (views.py) + 網頁模版 (index.html)) = 實際網頁 (HTML)。
    ```
    return render(request, 'index.html', {'msg': 'Hello', 'now': now})
    ```
* ### 渲染器符號識別
    * ### {{ var_name }}: 顯示 var_name 實際值。
    * ### {% cmd %}: 執行命令 (決策、迴圈、模板繼承與模板管理等指令)。
* ### CDN (Content Delivery Network) links 的引入位置
    * ### 引入 Bootstrap 的 CDN 通常放在 ```<head>``` 標籤中，因為 Bootstrap 包含了許多 CSS 樣式和組件，這些資源需要在頁面的內容之前被下載和解析，將其引入放在 ```<head>``` 標籤中，可以確保在頁面渲染前已經下載並準備好使用 Bootstrap 的相關樣式。
    * ### jQuery 的 CDN 引入通常放在 ```<body>``` 標籤的最後，是因為其是一個 JS 函式庫，主要用於操作和處理網頁的 DOM (Document Object Model)，也就是頁面的元素，將其 ```<body>``` 標籤的最後可以確保在頁面的 DOM 元素已經完全載入之後再加載 jQuery 函式庫，這是因為如果在 jQuery 加載之前使用了某些需要 jQuery 支持的 JavaScript 代碼，可能會導致錯誤或未定義的行為，因為此時 jQuery 尚未被加載和初始化。
    * ### 總結來說，Bootstrap 的 CDN 引入放在 ```<head>``` 標籤中，是為了確保頁面的樣式能夠正確顯示；而 jQuery 的 CDN 引入放在 ```<body>``` 標籤的最後，是為了確保在頁面的 DOM 加載完成後再加載 jQuery 函式庫，避免可能的錯誤。
    * ### 理解更多 -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/Questions/Question043)
* ### 文件物件模型 (Document Object Model, DOM)
    * ### 是 HTML、XML 和 SVG 文件的程式介面。
    * ### 它提供了一個文件 (樹) 的結構化表示法，並定義讓程式可以存取並改變文件架構、風格和內容的方法。
    * ### DOM 提供了文件以擁有屬性與函式的節點與物件組成的結構化表示。
    * ### 節點也可以附加事件處理程序，一旦觸發事件就會執行處理程序。
    * ### 本質上，它將網頁與腳本或程式語言連結在一起。
    * ### 雖然常常使用 JavaScript 來存取 DOM，但它本身並不是 JavaScript 語言的一部分，而且它也可以被其它語言存取 (不過不太常見就是了)。
    * ### 理解更多 -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/Questions/Question042)
* ### 在 template 中使用 static 檔案
    ```
    # 指定在網址中以 "static/" 為開頭的網址為靜態檔案的讀取:
    # 表示用于访问静态文件的 URL 前缀。
    STATIC_URL = 'static/'

    # 設定執行靜態檔案收集時其實際被複製並取用的位置:
    # 表示在运行 collectstatic 命令时将收集到的静态文件的存储位置。
    STATIC_ROOT = BASE_DIR / 'staticfiles'

    # 設定靜態檔案在執行時要搜尋的檔案位置:
    # 包含路径的列表，用于指定额外的静态文件目录。
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
    ```
* ### 将项目中的静态文件从各个应用收集到一个统一的位置，以便在生产环境中提供服务:
    ```
    python manage.py collectstatic
    ```
* ### 加载静态文件
    ```
    {% load static %}
    ```
<br />
