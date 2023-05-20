Question039 - Apache 出現 WSGI: Truncated or oversized response headers received from daemon process 如何解決 ?
=====
* ### Add the below line to your httpd.conf.
    ```
    # In my case the file was /etc/apache2/sites-available/default-ssl.conf

    WSGIApplicationGroup %{GLOBAL}
    ```
<br />
