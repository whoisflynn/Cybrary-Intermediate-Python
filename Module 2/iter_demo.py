#!/usr/bin/Python3

class IterDemo:
  def __init__(self):
    self.alphabet = ‘abcdefghijklmnopqrstuvwxyz’
    self.i = 0
    
  def __iter__(self):
    return self

  def __next__(self):
    if self.i >= 25:
      raise StopIteration
    letter = self.alphabet[self.i]
    self.i = self.i +1
    return letter
    
ID = IterDemo()
for i in ID:
  print(i)
