#!/usr/bin/Python3
class Person:
  name = ‘’
  age = 0
  def __init__(self,name,age):
    self.name = name
    self.age = age
    return
    
  def print_vals()
    print(‘Name: {}\nAge: {}’.format(self.name,self.age))

class Employee(Person):
  def __init__(self, name, age, department):
    Person.__init__(self, name, age)
    self.department = department
    
def extended_print_vals(self)
  print(‘Name: {}\nAge: {}’.format(self.name,self.age, self.department))
  
  
emp = Employee(‘Joe’, 25, ‘Research’)
emp.extended_print_vals()
