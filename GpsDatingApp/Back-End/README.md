Back-End
=====
* ### python manage.py makemigrations
* ### python manage.py migrate
<br />

* ### online modify / git push
	* ### domain suffix
	* ### debug
	* ### CORS_ALLOWED_ORIGINS
	* ### db
	* ### static file
	* ### ASGI
	* ### ----------
	* ### python manage.py collectstatic
	* ### GameFlow().start()
	* ### index.html in templates and static folder
<br />

***
<br />

* ### pip freeze > requirements.txt
* ### pip install -r ../requirements.txt
<br />

* ### python manage.py runserver 0.0.0.0:80
* ### python manage.py runserver_plus --cert server.crt 0.0.0.0:8000
<br />

* ### daphne -e ssl:8443:privateKey=key.pem:certKey=crt.pem project.asgi:application
* ### daphne -b 0.0.0.0 -p 8443 project.asgi:application
<br />

* ### pip install openpyxl
* ### pip install mod_wsgi
<br />

* ### TRUNCATE TABLE table_name
<br />

* ### Get-Content ./log.log -Wait
<br />

* ### daphne need restart every time
<br />

* ### note redis RDB persistence problem -> dump.rdb
* ### delete dump.rdb file restart every time
* ### if needed redis only for cache  -> modify block [save ""] and delete dump.rdb file
<br />

* ### do not delete folder admin and django_extensions
<br />
