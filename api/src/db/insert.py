import mysql.connector

connection = mysql.connector.connect(
  host = "bridgeAppDb",
  user = "root",
  port = '3306',
  password = "pass",
  database = "boardDB"
)

query = "select * from matches where uuid = %s"
cursor = connection.cursor()

cursor.execute(query, ["a6cf9e51-543e-45c0-a246-19c71ae9382e"])
result = cursor.fetchone()
print(result)

cursor.close()
connection.close()