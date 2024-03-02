# 1- Ask the user to input a number and print whether the number is within the specified range (20-50)

'''

randomNumber = input("Enter a random number")
if int(randomNumber) in range(20, 50):
    print('yes in range')
else:
    print('no not in range')
'''

# 2- Write a two functions to calculate the area and the perimeter of a rectangle given its length and width.
'''
def calculateArea(length, width):
  return length * width

def calculatePerimeter(length, width):
  return (length + width) * 2 

print("Area = ", calculateArea(4, 6))
print("Perimeter = ", calculatePerimeter(3, 9))
'''

# 3- Write a function receive two strings and concatenate them with two different methods.

'''
def concatenateTwoStrings(firstString, secondString):
  print(" ".join([firstString, secondString]))

concatenateTwoStrings("test", "word")


def concatenateTwoStrings_2(string1 ,string2):
  return "{text1} {text2}".format(text1=string1, text2=string2)

print(concatenateTwoStrings_2("test", "word"))
'''

# 4- Write a function receive list of values, square each element in a given list and return the squared list.

'''
def square(numericalValues):
  squaredList = []
  for i in numericalValues:
    squaredList.append(i*i)
  print(squaredList)

square([4, 7, 6])
'''

# 5- Implement a program to merge two dictionaries and return the result
'''
def mergeTwoDictionaries(dict1, dict2):
  return dict2.update(dict1)
  
# spread operator
# ** spread

# keys must be different
first_dict = dict(name="ali", age=45)
second_dict = {'newName': "ahmeed", 'newAge': 30}
mergeTwoDictionaries(first_dict, second_dict)
print the second one as the first
print(second_dict)
'''

# 6- Write a function receive two lists and merge them.

'''
def listsMerger(list1, list2):
  for i in list2:
    list1.append(i)
  return list1

print(listsMerger([1, 4], [6, 9]))
'''
  
# 7- Write a function to check if these keys (job, card_number)
# exists in this dictionary {"name": "jone", "email": "jane@outlook.com", "age": 25,
# "job": "engineer", "address": "cairo, Egypt"}.  

''' 
def checkKeysExistence(dictionary):
  resultList = []
  jobFlag = False
  card_numberFlag = False
  for key in dictionary:
    if key == 'job':
      jobFlag = True
    if key == 'card_number':
      card_numberFlag = True
  
  resultList.append("job is found") if jobFlag else resultList.append("job is NOT found")      
  resultList.append("card_number is found") if card_numberFlag else resultList.append("card_number is NOT found")      
  print(resultList)
      
      
sampleDict = {"name": "jone", "email": "jane@outlook.com", "age": 25, "job": "engineer", "address": "cairo, Egypt"}
checkKeysExistence(sampleDict)
'''

# 8- Write a program that calculates the sum of numbers from 1 to 100 using a loop and print the result

'''
sum = 0
for number in range(1, 100):
  sum += number
print(sum)
''' 

# 9- Write a function to check if a given number is even or odd.
'''
def checkNum(number):
  print('Even' if(number % 2 == 0) else 'Odd')

checkNum(9)
'''

# 10- Write a function to reverse a given string.
'''
def reverseString(string):
  print(string[::-1])

reverseString("Hello")
'''

# 11- Write a function to check if a given string is a palindrome (reads the same backward as forward).

'''
def checkPalindrome(string):
  i = 0
  j = len(string)-1
  
  while i < len(string):
    if string[i] != string[j]:
      return 'Not palindrome'
    j -= 1
    i += 1
    
  return 'Palindrome'

print(checkPalindrome("iti"))
'''

# 12- Write a function that removes even numbers from a list and squares the remaining odd numbers.

'''
def removeEvensAndSquareOthers(list):
  # we cannot modify in the run time as the length is getting changed, but save in a new one instead
  newList = []
  for i in list:
    if i % 2 != 0:
      newList.append(i*i)
  print(newList)
removeEvensAndSquareOthers([4, 8, 9 ,6, 3 ,1 ,13])
'''

# 13- Implement a function to check if a number is prime or not.

'''
def checkPrime(number):
  isPrime = True

  if number == 1:
    print('1 is NOT a prime')
    return
  
  else:
    for i in range(2, number):
      if number % i == 0:
        isPrime = False
  
  if isPrime == True:
    print(number, "is a prime number")
  else:  
    print(number, "is NOT a prime number")
    
checkPrime(1)
'''

# 14- Write a function to calculate the factorial of a given number.
'''
def factorial(number):
  if number == 0:
    return 0
  if number == 1:
    return number
  return number * factorial(number-1)
print(factorial(4))
'''

# 15- Create a Python function that takes a list of numbers,
# performs various operations (sum, minimum, maximum, squared list),
# and returns a new list containing the results

'''
def listOperations(list):
  newList = []
  squaredList = []
  newSum = sum(list)
  newMin = min(list)
  newMax = max(list)
  for i in list:
    squaredList.append(i * i)
    
  newList.append([newSum, newMin, newMax])
  newList.append(squaredList)
  return newList

print(listOperations([4, 8, 9, 6, 3, 1 ,2, 7]))  
'''