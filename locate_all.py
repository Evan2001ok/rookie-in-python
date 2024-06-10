#!/usr/bin/env python
# coding: utf-8

# In[25]:


def locate_all(a,b):
    index = 0
    word = len(b)#3
    Strs = []
    for x in range(len(a)):
        if a[index:word] == b:# if find a is sub of b ,leave loop
            Strs.append(index)
        index += 1
        word += 1
        if len(a) < word:#check length to leave loop
            return Strs
locate_all('the upside down', 'barb')


# In[ ]:




