#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re 



a = input('Paste your CVS hier')
    
b = re.sub(" ",",", a)

print(b)


# In[ ]:




