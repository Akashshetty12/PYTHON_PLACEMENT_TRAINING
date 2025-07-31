import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "h9k8j7p0",
    database = "BATCH5",
)
if mydb.is_connected():
    print("Connected to MySQL database")
    c = mydb.cursor()
    c.execute("SELECT * FROM STUDENTS")
    rows = c.fetchall()
    for row in rows:
        print(row)
else:
    print("Connection to MySQL database failed")