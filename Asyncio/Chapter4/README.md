Chapter4 aioMySQL
=====
* ### connect_mariadb_with_aiomysql (搭建 MariaDB 數據庫環境)
* ### connect_mariadb_with_aiomysql_pool (搭建 MariaDB 數據庫環境並控制並發連接數量)
* ### aiomysql_crud (撰寫 SQL 操作數據庫)
* ### aiomysql_sqlalchemy (沒有 SQL 的數據庫操作)
* ### 註: 上述範例共用 "./connect_mariadb_with_aiomysql/docker-compose.yml" 建立 Docker 容器。
* ### 註: 運行完畢後可刪除 "mariadb_data" 資料夾。
* ### aiohttp_mysql (綜合實例)
  ```
  localhost inside your docker container != localhost of your host machine.
  Note 'db' which is name of your db service.
  Docker, internally will resolve that name into container ip address in docker network.
  ```
  ```
  just delete two line of code in aiomysql/sa/result.py,
  the code works fine! The code info:
  116: assert dialect.case_sensitive, \
  117: "Doesn't support case insensitive database connection"
  ```
<br />
