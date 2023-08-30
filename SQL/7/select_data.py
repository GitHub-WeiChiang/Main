import mysql.connector

mysql_connection = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='PythonDB'
)

cursor = mysql_connection.cursor()
cursor.execute('SELECT * FROM Students')
students = cursor.fetchall()

for student in students:
    print(student)

mysql_connection.close()
