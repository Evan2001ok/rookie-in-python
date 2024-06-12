#!/usr/bin/env python
# coding: utf-8

# In[8]:


def extract_place(filename):
    first = filename.find("_")
    result = filename[first + 1:]
    second = result.find("_")
    result = result[:second]
    return result
    

        
extract_place("2018-06-06_MountainView_16:20:00.jpg")   


# In[ ]:




