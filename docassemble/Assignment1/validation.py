import re
from docassemble.base.util import * 

def validate_nric(string):
  if not re.match(r'[STFG][0-9]{7}[A-Z]', string):
    validation_error('Invalid NRIC format.')
  else:
    if string[0] == "S": 
      x = 0
      d = (x + int(string[1])*2 + int(string[2])*7 + int(string[3])*6 + int(string[4])*5 + int(string[5])*4 + int(string[6])*3 + int(string[7])*2) % 11
      digitarr = "JZIHGFEDCBA"
      digit = digitarr[d]
      if string[8] == digit:
        return True
      else:
         validation_error('Invalid NRIC.')                     
    if string[0] == "T": 
      x = 4
      d = (x + int(string[1])*2 + int(string[2])*7 + int(string[3])*6 + int(string[4])*5 + int(string[5])*4 + int(string[6])*3 + int(string[7])*2) % 11
      digitarr = "JZIHGFEDCBA"
      digit = digitarr[d]               
      if string[8] == digit:
        return True
      else:
         validation_error('Invalid NRIC.')   
    if string[0] == "F":
      x = 0
      d = (x + int(string[1])*2 + int(string[2])*7 + int(string[3])*6 + int(string[4])*5 + int(string[5])*4 + int(string[6])*3 + int(string[7])*2) % 11
      digitarr = "XWUTRQPNMLK"
      digit = digitarr[d]     
      if string[8] == digit:
        return True
      else:
         validation_error('Invalid NRIC.')
    if string[0] == "G":
      x = 4
      d = (x + int(string[1])*2 + int(string[2])*7 + int(string[3])*6 + int(string[4])*5 + int(string[5])*4 + int(string[6])*3 + int(string[7])*2) % 11                                     
      digitarr = "XWUTRQPNMLK"
      digit = digitarr[d]              
      if string[8] == digit:
        return True
      else:
         validation_error('Invalid NRIC.')