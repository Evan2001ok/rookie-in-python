#!/usr/bin/env python
# coding: utf-8

# In[10]:


def ListIndex():
    month = 8
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    # use list indexing to determine the number of days in month

    num_days = days_in_month[month-1:month]
    print(num_days)
ListIndex()


# In[ ]:




