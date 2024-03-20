import dbConfig
from datetime import datetime

c = dbConfig.dbCursor
conn = dbConfig.mysqlConnection

def register(fName, lName, email, password, mobile_phone):
  sql = "INSERT INTO users (first_name, last_name, email, password, mobile_phone) VALUES (%s, %s, %s, %s, %s)"
  val = (fName, lName, email, password, mobile_phone)
  c.execute(sql, val)
  conn.commit()
  print(c.rowcount, "record inserted.")


def login(email, password):
  sql = "SELECT * FROM users WHERE email = %s AND password = %s"
  val = (email, password)
  c.execute(sql, val)
  user = c.fetchone()
  if user is not None:
    print("Login is Successful ✅")
    return user
  else:
    raise Exception("Bad data you entered huh!")

# user can create a project | project title should be unique
def createProject(title,	details,	total_target,	start_date,	end_date, user_id):
  sql = "INSERT INTO projects (title,	details,	total_target,	start_date,	end_date, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
  val = (title,	details,	total_target,	start_date,	end_date, user_id)
  c.execute(sql, val)
  conn.commit() # required when changes are made to the table/db
  print(c.rowcount, "record inserted.")
  print("Last Row Id", c.lastrowid)
  
# User can view all projects
def viewAllProjects():
  sql = "SELECT * FROM projects"
  c.execute(sql)
  pros = c.fetchall()
  
  for p in pros:
    print(p)

# User can delete his own project
def deleteProject(pTitle, uId):
  sql = "DELETE FROM projects WHERE title = %s AND user_id = %s"
  val = (pTitle, uId)
  c.execute(sql, val)
  conn.commit()
  print(c.rowcount, "record deleted.")
  
'''
The names of MySQL schema objects - tables, columns etc - 
can be interpolated using string formatting, 
by surrounding the placeholder with backticks ('`', ASCII 0x96). See MySQL Identifiers.
Using backticks prevents errors if the column name contains a space, or matches a keyword or reserved word.
--DB-API parameter substitution
 ''' 
# title of the project should be unique
def editProject(column, valueToBeUpdated, project_title, uId):
  sql = f"""UPDATE projects SET `{column}` = %s WHERE title = %s AND user_id = %s"""
  val = (valueToBeUpdated, project_title, uId)
  c.execute(sql, val)
  conn.commit()
  print(c.rowcount, "record updated.")
