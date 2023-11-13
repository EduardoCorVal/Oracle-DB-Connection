import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT"))
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")

connection = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

query = "SELECT VERSION()"
cursor.execute(query)

result = cursor.fetchone()

print("MySQL Server Version:", result[0])

cursor.close()
connection.close()
