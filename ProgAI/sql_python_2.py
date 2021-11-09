# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:52:45 2021

@author: victorf
"""

import mysql.connector as sql

#cnx = sql.connect(
#    host='localhost', 
#    port='33060', 
#    user='homestead', 
#    password='secret')

cnx = sql.connect(
    host='52.50.23.197', 
    port='3306', 
    user='student', 
    password='student')

cursor = cnx.cursor()

query = "SELECT * FROM wonderful_learners.learners;"

cursor.execute(query)

results = cursor.fetchall()

avg_age = sum([x[3] for x in results]) 

print(avg_age / len(results))

# cnx.commit()

cnx.close()


