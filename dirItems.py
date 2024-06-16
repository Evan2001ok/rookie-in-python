#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
favorites = {'color':'purple', 'number':'42', 'animal':'turtle', 'language':'python'}
for key,value in favorites.items():
    print(f'my favorite {key} is {value}')

