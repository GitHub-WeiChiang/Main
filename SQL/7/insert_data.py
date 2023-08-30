import mysql.connector

mysql_connection = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database="PythonDB"
)

sql = "INSERT INTO Students (StudentID, Name, City) VALUES (%s, %s, %s)"
val = [
    (1, 'Enoch', 'Los Angeles'),
    (2, 'David', 'New York City'),
    (3, 'Kevin', 'Shanghai'),
    (4, 'Frank', 'Beijing'),
    (5, 'Alice', 'Tokyo'),
]

cursor = mysql_connection.cursor()
for student in val:
    cursor.execute(sql, student)

mysql_connection.commit()
