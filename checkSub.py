#!/usr/bin/env python
# coding: utf-8

# In[5]:


def is_substring(a,b):
    index = 0
    word = len(a)#3  
    for x in b:
        if b[index:word] == a:# if find a is sub of b ,leave loop
            return True
        else:
            index += 1
            word += 1
            if len(b) < word:#check length to leave loop
                return False
is_substring('balloon', 'ssssssssss')


# In[ ]:




