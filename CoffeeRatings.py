## Dependencies
import mysql.connector
##

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="yourpassword"
)

print(mydb)