#!/usr/bin/env python
# coding: utf-8

# In[8]:


def is_substring(a,b):#use while to check a is sub of b
    index = 0
    word = len(a)#3  
    while a != b[index:word]:
        index += 1
        word += 1
        if word > len(b):
            return False
    return True
is_substring('balloon', '')


# In[ ]:




