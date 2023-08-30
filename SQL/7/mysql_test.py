import mysql.connector

mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

print(mysql_connection)
