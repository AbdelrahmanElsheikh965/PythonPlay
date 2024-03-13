import sys, User, re, datetime

# main.py = Driver Code

# Validate user inputs
def checkRegex(field, pattern, rules):
  if field and re.match(fr'{pattern}', field):  # formatted raw string
      return True
  else:
    raise Exception(f'value you entered violates the following rules: {rules}')

# validate start & end dates of the projects.
def checkDate(dateString):
  try:
    dateObject = datetime.datetime.strptime(dateString, '%Y-%m-%d')
    return True
  except ValueError:
    raise Exception("Incorrect data format, should be YYYY-MM-DD")

# prepare the user data
user = None

while True:
  
  # Main user menu
  print("""
        1- View all projects
        2- Login
        3- Register
        4- Search for a project (coming soon)
        ---> Protected  (Requires login) Options <---
        5- Create a project fund raise campaign
        6- Delete your project
        7- Edit a specific project
        9- To Exit/Terminate the program
        """)
    
  decision = input("Hi, Choose:  ")
  
  # Main program switch case
  match decision:
    case '1':    
      User.viewAllProjects()
    
    case '2':
      email    = input("Enter your email: ")
      password = input("What about your password ?: ")
      try:
        user = User.login(email=email, password=password)
        print(user)
      except Exception as errorMessage:
        print(f"{errorMessage}")
      
    case '3':
      txt_fields_rules = """ -> first name should not left blank
                            -> first name should only contains alphabets
                        """
      email_field_rules = """ -> email should be validated as an email address """
      mobile_field_rules = """ -> phone should be egypt-coded one """
      try:
        first_name    = input("Ok, enter your first name ?: ")
        checkRegex(first_name, "^[a-zA-Z]+$", txt_fields_rules)
        
        last_name    = input("Lastname !!: ")
        checkRegex(last_name, "^[a-zA-Z]+$", txt_fields_rules)
        
        email    = input("EMail now ?:?=> ")
        checkRegex(email, "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_field_rules)
      
        password    = input(" 1st-pass ?: ")
        cnfm_password = input(" 1st-pass again ?: ")
        checkRegex(cnfm_password, "^(.{8,})$", "password min length is 8")
        
        if password == cnfm_password:
          mobile_phone    = input("What about your mobile phone number ?: ")
          checkRegex(mobile_phone, "^01[0-2,5]{1}[0-9]{8}$", mobile_field_rules)
          User.register(first_name, last_name, email, password, mobile_phone)
        else:
          print("Passwords DOES NOT MATCH")
      
      except Exception as errorMessage:
        print(f"{errorMessage}")
    
    case '5':
      if user is not None:
        title = input("Title of the project: ")
        details = input("Details of the project: ")
        totalTarget = float(input("Total-Target of the project: "))
        startDate = input("Start date of the project: ")
        try:
          checkDate(startDate)
          endDate = input("End date of the project: ")
          checkDate(endDate)
          User.createProject(title, details, totalTarget, startDate, endDate, user[0])
        except Exception as excMessage:
          print(f'{excMessage}')
      else:
        print("You must login first as mentioned before 😠")
    
    case '6':
      if user is not None:
        pTitle = input("Enter the title of the target project: ")
        User.deleteProject(pTitle, user[0])
      else:
        print("You must login first as mentioned before 😠")
    
    case '7':
      # column, valueToBeUpdated, project_title, uId
      if user is not None:
        column = input("Enter the column you wanna update its values: ")
        newValue = input("I am wondering what the new value is? ")
        project_title = input("guessing the project title ...?! ")
        User.editProject(column, newValue, project_title, user[0])
      else:
        print("You must login first as mentioned before 😠")
        
    case '9':
      exit()
        
    case _:
      print("WRONG INPUT, CHOOSE ONLY FROM THE MENU !")
  
