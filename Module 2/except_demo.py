#!/usr/bin/Python3

class CustomException(Exception):
  print(‘Exception found’)
  
def main():
  for i in range(10):
    if i % 3 == 0:
      raise CustomException:
      
‘’’
try:
  list_one = [1,2,3,4,5]
  for i in range(6):
    print(list_one[i])
    
except IndexError:
  print(‘Index out of range’)

print(‘Got past our error’)
‘’’
main()
