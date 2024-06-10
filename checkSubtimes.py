#!/usr/bin/env python
# coding: utf-8

# In[11]:


def count_substring(a,b):
    index = 0
    word = len(a)#3  
    times = 0
    for x in range(len(b)):
        if b[index:word] == a:# if find a is sub of b ,leave loop
            times = times + 1
        index += 1
        word += 1
        if len(b) < word:
            return times#find sub times 
count_substring('AA', 'AAAA')
#count_substring("love", "love, love, love, all you need is love")


# In[ ]:




