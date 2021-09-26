# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:10:13 2021

@author: victorf
"""

import math, cmath

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
    

def get_discriminant(a,b,c):
    discriminant = b**2 - (4*a*c)
    print(f'\ndiscriminant = {discriminant}:')
    return discriminant
    

def quadratic_equation_root(a,b,c):
    print('\nreal-number solutions:')
    discriminant = get_discriminant(a,b,c)    
    
    if discriminant < 0:
        # such as a=3, b=4, c=2
        print('neither of the solutions are real numbers')        
        return
    
    discriminant_root = math.sqrt(discriminant)
    
    if discriminant > 0:        
        # such as a=6, b=10, c=-1
        x_minus = (-b - discriminant_root) / (2 * a)
        x_plus = (-b + discriminant_root) / (2 * a)        
        print(f'there are two real number solutions: {x_plus} and {x_minus}')
    else:        
        # such as a=9, b=12, c=4
        x = -b / (2 * a)
        print(f'there is a repeated real number solution: {x}') 


# imported the cmath module to perform complex square root
def quadratic_equation_root_complex(a,b,c):  
    print('\ncomplex-number solutions:')
    discriminant = get_discriminant(a,b,c)    
    
    x_minus = (-b - cmath.sqrt(discriminant)) / (2 * a)
    x_plus = (-b + cmath.sqrt(discriminant)) / (2 * a)
    
    print(f'solutions are {x_minus} and {x_plus}')
    
    
    
# demo    
any_number = int(input('Enter a integer: '))

is_odd(any_number)
is_negative(any_number)
is_negative_obscure_way(any_number)

print('\n\nRoot of a Quadratic Equation:')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

quadratic_equation_root(a,b,c)
quadratic_equation_root_complex(a,b,c)
    