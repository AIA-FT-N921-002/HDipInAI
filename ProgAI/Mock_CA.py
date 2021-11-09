# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:44:11 2021

@author: victorf and Elvyra
"""


# How many members are fans of a particular sport
def count_member_by_sport(chosen_sport):
    file = open('members.csv')

    count = 0
    sports = dict()

    for i in file:
        row = i.split(',')
        sport_name = row[2]
    
        if sport_name != 'Sport':
            if sport_name in sports:
                sports[sport_name] = sports[sport_name] + 1
            else:
                sports[sport_name] = 1                
        
    return sports[chosen_sport]
    


print(count_member_by_sport('Basketball'))
    
    

    