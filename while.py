#!/usr/bin/env python
# coding: utf-8

# In[4]:


def unit_dot(word):
    index = 0
    while index < len(word) and word[index] != ".":
        index += 1 
    return word[0:index]
unit_dot("This is a sentence. This is another.")


# In[ ]:




