import mysql.connector

connection = mysql.connector.connect(host = "127.0.0.1", database="test", user = "root", password = "m")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list;")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()

