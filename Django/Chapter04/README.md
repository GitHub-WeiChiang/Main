Chapter04 深入瞭解 Django 的 MVC 架構
=====
* ### 初始化步驟
    ```
    conda create --name Chapter04 python=3.10

    conda activate Chapter04

    pip install django

    django-admin startproject chapter04

    cd chapter04

    python manage.py startapp mysite
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
<br />
