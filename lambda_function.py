#!/usr/bin/env python
# coding: utf-8

# In[4]:


def lambda_function():
    numbers = [
                  [34, 63, 88, 71, 29],
                  [90, 78, 51, 27, 45],
                  [63, 37, 85, 46, 22],
                  [51, 22, 34, 11, 18]
               ]

    averages = list(map(lambda x: sum(x) / len(x) , numbers))
    print(averages)
lambda_function()


# In[ ]:




