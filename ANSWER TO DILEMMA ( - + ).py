#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import re


a = input('+ values to dilemma:') # You can typ your values system as sentences
b = input('- values to dilemma:')

    

while True:
    c = input('Ask me for the dilemma:') # Typ one word per input
    if re.findall(c,a,re.VERBOSE):
        (z)= 1
    else:
        (z)= 0 
    if re.findall(c,b,re.VERBOSE):
        (z1)= 1
    else:
        (z1)= -1     

    if   0<(z)+(z1):
        print('Maybe yes!')
    elif 0>(z)+(z1):
        print('Maybe not!')
    elif 0==(z)+(z1):
        print('Not idea!')


# In[ ]:




