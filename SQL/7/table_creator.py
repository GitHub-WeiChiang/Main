import mysql.connector

mysql_connection = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database="PythonDB"
)

cursor = mysql_connection.cursor()

cursor.execute(
    "CREATE TABLE Students (StudentID int PRIMARY KEY, Name VARCHAR(255), City VARCHAR(255))"
)
