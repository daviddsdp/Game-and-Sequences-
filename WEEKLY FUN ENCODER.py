#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re


a = input('Paste hier your enconde fun. Then where and when you offer us:')
    

while True:
    b = input('Tell me please about your fun. Then when and where your looking for:')
    if re.findall(b,a,re.VERBOSE):
        print('Something happen let you know!')
    else:
        print('Notting happen around the world.') 



# In[ ]:




