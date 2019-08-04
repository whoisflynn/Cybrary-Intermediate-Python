#!/usr/bin/Python3

def custom_range(last):
  i = 0
  while i < last:
    yield i
    i += 1
    
for i in custom_range(10):
  print(i)
