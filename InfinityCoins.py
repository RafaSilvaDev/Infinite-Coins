n = 12
change = []
set = []

'''
* The function below will...
* - Obtain the input
* - Divide the input by 25
* - Append the result in 'change' array
* - Divide the input by 10
* - Append the result in 'change' array
* - Divide the input by 5
* - Append the result in 'change' array
* - Divide the input by 1
* - Append the result in 'change' array
* - Append the final 'change' array in 'set' array
* - Return the final 'set' array
'''

def makeChange(num):
  change.append(int(num / 25))
  num = num % 25
  
  change.append(int(num / 10))
  num = num % 10

  change.append(int(num / 5))
  num = num % 5

  change.append(int(num / 1))
  
  set.append(change)

  return set

print(makeChange(n))