Django
=====
* ### Chapter01 網站開發環境建置
* ### Chapter02 Django 網站快速入門
* ### Chapter03 讓網站上線
* ### Chapter04 深入瞭解 Django 的 MVC 架構
* ### Chapter05 網址的對應與委派
<br />

Initial Configuration Sample Code
=====
```
conda env list

conda env remove --name VENV_NAME
```
```
# "VENV_NAME" here is "django"

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
# If necessary, you can add the following code to admin.py.

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
<br />

VS Code Extensions
=====
* ### Code Runner
* ### Django
* ### Django Template
* ### HTML CSS Support
* ### Python
<br />

Reference
=====
* ### 快速學會 Python 架站技術：活用 Django 4 建構動態網站的 16 堂課
<br />
