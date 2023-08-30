import mysql.connector

mysql_connection = mysql.connector.connect(
    user='root', password='', host='localhost'
)

cursor = mysql_connection.cursor()

cursor.execute("CREATE DATABASE PythonDB")
