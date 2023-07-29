Chapter04 深入瞭解 Django 的 MVC 架構
=====
* ### 初始化步驟 ("VENV_NAME" here is "Chapter04")
    ```
    conda create --name VENV_NAME python=3.10

    conda activate VENV_NAME

    pip install django

    django-admin startproject PROJECT_NAME

    cd PROJECT_NAME

    python manage.py startapp APP_NAME
    ```
    ```
    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = [
        ...,
        'APP_NAME',
    ]

    LANGUAGE_CODE = 'zh-hant'

    TIME_ZONE = 'Asia/Taipei'
    ```
    ```
    python manage.py makemigrations

    python manage.py migrate

    python manage.py createsuperuser
    ```
    ```
    from APP_NAME.models import MODELS_NAME

    admin.site.register(MODELS_NAME)
    ```
    ```
    pip list --format=freeze > requirements.txt
    ```
    ```
    mkdir static
    mkdir templates
    ```
    ```
    TEMPLATES = [
        {
            ...,
            'DIRS': [BASE_DIR / 'templates'],
            ...,
        },
    ]

    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
    ```
    ```
    python manage.py runserver
    ```
    ```
    conda deactivate
    ```
* ### models.Model 中常用的資料欄位格式說明
    | 欄位資料型態 | 常用參數 | 說明 |
    | - | - | - |
    | BigIntegerField |  | 64 位元的大整數 |
    | BooleanField |  | 布林值 |
    | CharField | max_length: 指定長度上限 | 短字串，單行文字 |
    | DateField | auto_now: 被修改時自動填入當前日期<br/>auto_now_add: 插入時自動填入當前日期 | 日期格式: datetime.date |
    | DateTimeField | 同上 | 日期時間格式: datetime.datetime |
    | DecimalField | max_digits: 可接受最大位數<br/>decimal_places: 小數所佔位數 | 定點小數數值: Python 的 Decimal 模組實例 |
    | EmailField | max_length: 最長字數 | 電子郵件格式 |
    | FloatField |  | 浮點數 |
    | IntegerField |  | 整數 |
    | PostiveIntegerField |  | 正整數 |
    | SlugField | max_length: 最大字元長度 | 與 CharField 相似，用於表示部份網址 |
    | TextField |  | 長文字格式，常用於 HTML 表單 Textarea 輸入項目 |
    | URLField | max_length: 最大字元長度 | 與 CharField 相似，用於表示完整網址 |
* ### models.Model 各欄位常用的屬性說明
    | 欄位選項 | 說明 |
    | - | - |
    | null | 是否接受儲存空值 NULL: 預設為 False |
    | blank | 是否接受儲存空白內容: 預設為 False |
    | choices | 以選項方式儲存，僅可存入候選值 |
    | default | 預設值 |
    | help_text | 求助訊息 |
    | primary_key | 是否為主鍵: 預設為 False |
    | unique | 是否為唯一值: 預設為 False |
* ### 透過指令生成檔案 xxxx_initial.py 對應的 SQL 語句
    ```
    python manage.py sqlmigrate APP_NAME SERIAL_NUM
    ```
* ### 透過 Python Shell 操作資料表
    ```
    python manage.py shell

    from mysite.models import TABLE

    table = TABLE.objects.create(...)

    exit()
    ```
* ### Django ORM 常用的函式以及條件設定參數
    | 函式名稱或條件設定 | 說明 |
    | - | - |
    | create() | 創建模型實例的同時將其保存到資料庫 (快捷方式: 創建 + 儲存 !) |
    | save() | 將對象的更改實際保存到資料庫中 |
    | raw() | 執行自定義的 SQL 查詢並返回結果集 (在實現分頁時會需要它的 !) |
    | filter() | 傳回符合指定條件的 QuerySet |
    | exclude() | 傳回不符合指定條件的 QuerySet |
    | order_by() | 針對所接收的 QuerySet 進行排序 |
    | all() | 取得該表所有資料 |
    | get() | 取得符合條件唯一紀錄 (沒有或是超過一筆都會引發 Exception !) |
    | first() / last() | 取的第一個或是最後一個元素 |
    | aggregate() | 計算所接收 QuerySet 指定欄位的聚合函數 |
    | exists() | 是否存在指定條件之紀錄 (通常附加於 filter 方法) |
    | update() | 快速更新資料紀錄中的欄位內容 (無需調用 save 方法) |
    | delete() | 刪除指定紀錄 (無需調用 save 方法) |
    | iexact | 不區分大小寫的條件設定 |
    | contains / icontains | 如同 SQL 中的 like 與 ILIKE |
    | in | 提供一個串列，僅需符合該串列中任一項目即可 |
    | gt / gte / lt / lte | 大於 / 大於等於 / 小於 / 小於等於 |
    * ### Sample Code 1
        ```
        # Equal
        TABLE.objects.filter(COLUMN_NAME=VALUE)

        # Less Than
        TABLE.objects.filter(COLUMN_NAME__lt=VALUE)

        # Order By: ASC
        TABLE.objects.all().order_by("COLUMN_NAME")

        # Order By: DESC
        TABLE.objects.all().order_by("-COLUMN_NAME")
        ```
    * ### Sample Code 2
        ```
        # All Data
        TABLE.objects.all()

        # Not Equal
        TABLE.objects.exclude(COLUMN_NAME=VALUE)

        # Less Than Or Equal To
        TABLE.objects.filter(COLUMN_NAME__lte=VALUE)

        # Count
        from django.db.models import Count
        TABLE.objects.aggregate(Count('COLUMN_NAME'))

        # Sum
        from django.db.models import Sum
        TABLE.objects.aggregate(Sum('COLUMN_NAME'))

        # Not Case Sensitive
        TABLE.objects.filter(COLUMN_NAME__icontains=VALUE)

        # Or
        TABLE.objects.filter(COLUMN_NAME__in=[..., ..., ...])

        # Is Exist
        TABLE.objects.filter(COLUMN_NAME=VALUE).exists()
        ```
* ### 找不到網頁的回應
    ```
    from django.http import Http404

    raise Http404("msg")
    ```
* ### Path Parameters
    ```
    def VIEW_FUNC(request, PARAM_NAME):
        pass


    urlpatterns = [
        ...,
        path('.../<PARAM_TYPE:PARAM_NAME>/', VIEW_FUNC),
        ...,
    ]
    ```
<br />
