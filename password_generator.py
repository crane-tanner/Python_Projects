# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 14:59:43 2023

@author: HP


Password Generator
-------------------------------------------------
"""

import secrets 
import string


def create_pw(pw_length=15):
   letters = string.ascii_letters
   digits = string.digits
   special_chars = string.punctuation

   alphabet = letters + digits + special_chars
   pwd = ''
   pw_strong = False

   while not pw_strong:
       pwd = ''
       for i in range(pw_length):
           pwd += ''.join(secrets.choice(alphabet))

       if (any(char in special_chars for char in pwd) and
               sum(char in digits for char in pwd) >= 1):
           pw_strong = True

   return pwd


if __name__ == '__main__':
   print(create_pw())