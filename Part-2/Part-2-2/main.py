'''

Create a Python function that reads a file containing student names and their grades,
calculates the average grade, and identifies students who have failed.

'''

studentsFile = open("students.txt", "r")

students = studentsFile.readlines()

# ['Alice 90\n', 'Bob 78\n', 'Charlie 65\n', 'David 92\n', 'Eva 56\n', 'Frank 80\n']

failedStudentsList = []
sumValue = 0
counter = 0

for oneStudent in students:
  
  # remove spaces
  oneStudent.strip()
  
  # split stirng away from spaces
  sumValue += int(oneStudent.split()[1])
  
  # check for a specified value
  if int(oneStudent.split()[1]) < 50:
    failedStudentsList.append(oneStudent.split())
    
  counter += 1
  
print("Avergage: " + str(sumValue / counter))
print(failedStudentsList)