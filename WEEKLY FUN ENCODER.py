#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re


a = re.sub(" ","",input('Paste hier your enconde fun. Then where and when you offer us:'))
    

while True:
    b = re.sub(" ","",input('Tell me please about your fun. Then when and where your looking for:')) # Typ one word per input
    if  re.research(b,a):
        print('Something happen let you know!')
    else:
        print('Notting happen around the world.') 



# In[ ]:




