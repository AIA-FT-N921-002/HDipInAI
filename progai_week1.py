# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:10:13 2021

@author: victorf
"""

def is_odd(your_favorite_number):
    if your_favorite_number % 2 == 0:
        print('even')
    else: 
        print('odd')
    
    

def is_negative(your_number):  
    response = 'negative' if your_number < 0 else 'positive'
    print(response)    
    

def is_negative_obscure_way(your_number):  
    response = ('negative[2]', 'positive[2]')[your_number >= 0]
    print(response)        
    
    
# demo
    
any_number = int(input('Enter a integer: '))
is_odd(any_number)
is_negative(any_number)
is_negative_obscure_way(any_number)
    