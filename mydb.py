import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Infy@1239'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("Created!!!")