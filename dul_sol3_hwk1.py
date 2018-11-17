# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 22:08:04 2018

@author: duldu
"""


#### Question 3 solution ####
def sentence(s):
    ss=s.split(' ') #split words into a list
    m=sorted(ss, key=len) #sort list by word length
    mylist =[(m[i], len(m[i])) for i in range(0,len(m))] 
    print(mylist)
# Define the variable s as a string variable and run function sentence() to get solution     
s=('Mexico is a great country') 
sentence(s)
