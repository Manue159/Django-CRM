import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Manue123@mysql'
)


# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE db_crm")

print('All Done!')

