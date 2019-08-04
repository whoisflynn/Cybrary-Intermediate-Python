#!/usr/bin/Python3
#interpreter.py is a script which takes input of arbitrary length, separated by a delimiter and identifies the number and type of tokens

#delimiter: |
def main():
  num_token = []
  str_tokens = []
  user_data = input(‘Insert Delimited Data: ‘)
  split_data = user_data.split(sep=’|’)
  for i in split_tokens:
    if i.strip().isnumeric():
      num_tokens.append(i)
    else:
      str_tokens.append(i)
  print(‘String tokens: {}\nNumeric Tokens: {}’.format(len(str_tokens),len(num_tokens)))
  return

main()
