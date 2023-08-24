import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Rtw36-bird'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("All done!")