import mysql.connector

conn = mysql.connector.connect(
    host="your-rds-endpoint",
    user="admin",
    password="password",
    database="studentdb"
)

print("Connected Successfully")
