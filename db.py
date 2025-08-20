from mysql.connector import connect, Error

try:
    with connect(host ="localhost",user= "morata001",password="Chidera123#" ,  port=3307,  database="library_db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            print(row)

    pass
except Error as e:
    print(e)