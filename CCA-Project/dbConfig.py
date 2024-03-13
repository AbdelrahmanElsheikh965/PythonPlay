import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Getting environment variables
dbHost = os.getenv('db_host')
dbUserName = os.getenv('db_user_name')
dbPassword = os.getenv('db_password')
dbName = os.getenv('db_name')

# Establishing Database (Mysql) connection
mysqlConnection = mysql.connector.connect(
  host=dbHost,
  user=dbUserName,
  password=dbPassword,
  database=dbName
)

# Obtaining the value of the cursor to perform operations i.e.(CRUD) on MySQL server.
dbCursor = mysqlConnection.cursor()
