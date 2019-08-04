#!/usr/bin/Python3
#takes an arbitrary input and stores it in a file

def main():
  file_name = input(‘Filename: ‘)
  f.open(file_name,’w’)
  f.write(input(‘Insert data to store: ‘))
  f.close()
  return
  
main()
