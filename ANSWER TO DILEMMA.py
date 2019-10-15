#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re


a = input('Paste hier the answer to dilemma:')
    

while True:
    b = input('Ask me for dilemma:')
    if re.findall(b,a,re.VERBOSE):
        (z)= 1
    else:
        (z)= 0 

    if 0<(z):
        print('Maybe!')
    
    else:
        print('Not idea.')


# In[ ]:





# In[ ]:




