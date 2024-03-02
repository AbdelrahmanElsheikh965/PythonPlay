'''
given this list : numbers = [4, 9, 16, 25, 36],  Calculate square root of each number using lambda and map 
    and create dictionary contains numbers and sqrt_of_numbers and write it to json file.

'''

import json,  math

numbers = [4, 9, 16, 25, 36]

squared = map(lambda x:math.sqrt(x), numbers)
squared = list(map(int, squared))

dict = {}
counter = 0

while(counter < 5):
  dict[numbers[counter]] = squared[counter]  
  counter += 1
 
# Serializing (converting to JSON-formatted string) the dictionary
dict = json.dumps(dict, indent=4)
 
outfile = open("result.json", "w")
outfile.write(str(dict))