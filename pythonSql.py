import mysql.connector as con
from mysql.connector import Error

try:
    connection = con.connect(
        host="localhost",            # Host name (e.g., localhost)
        user="root",        # MySQL username
        password="Michael@18",    # MySQL password
        database="tutorial",     # Database name
        port = 3306
    )
    def createTbl():
        query = "CREATE TABLE attendance (id PRIMARY KEY AUTO_INCREMENT,name VARCHAR(200), email VARCHAR(60),phone VARCHAR(20))"

        con.cursor().execute(query)
        return True
    createTbl()
    def addData(name,phone):
        insert_query = "INSERT INTO test (name, phone) VALUES (%s, %s)"
        data = (name, phone)

        # Execute the query
        cursor.execute(insert_query, data)

        # Commit the transaction
        connection.commit()
        return cursor.rowcount
    # Check if the connection was successful
    if connection.is_connected():
        # print("Connected to MySQL database.")
        cursor = connection.cursor(dictionary=True)
        try:
            rows = addData("Timothy","080345665")
            if(rows>0):
                print(f"{cursor.rowcount} row(s) inserted.")
            else:
                print(f"No record was added")
        except Exception as e:
            print("An error occured",e)
        # if(createTbl()):
        #     print("Table has been created successfully")
        # cursor = connection.cursor(dictionary=True)
        # cursor.execute("SELECT * FROM customers")
        # results = cursor.fetchall()
    else:
        print("Failed to connect to database.")
        exit()
except Error as e:
    print("An error as occured",e)