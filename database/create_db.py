import mysql.connector

try:

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    with db:
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE native_crud")

        print("Create database native_crud success")

except mysql.connector.Error as error:
    print(f"Create database native_crud failed: {error}")

finally:
    if db.is_connected():
        db.close()
        print("MySQL connection is closed")