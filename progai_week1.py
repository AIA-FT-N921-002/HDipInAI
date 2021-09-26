# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:10:13 2021

@author: victorf
"""

def is_odd(your_favorite_number):
    print(your_favorite_number % 2 == 0)
    
any_number = int(input('Enter a integer: '))
print(is_odd(any_number))