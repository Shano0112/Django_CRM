import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Human00@"
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS dcrm_db")

print("All Done")