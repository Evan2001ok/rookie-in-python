#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

def make_place_directories(places):#create several directorys for pc 
    Strs = []
    lists = os.listdir()
    for x in places:
        for y in lists:
            if x == y:
                places.remove(x)
    
    for place in places:
        os.mkdir(place)
    
make_place_directories(["ok","son","no"])

