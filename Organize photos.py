#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
def extract_place(frame):
    return frame.split("_")[1]

def make_place_directories(places):#make directory to save photo
    for place in places:
        os.mkdir(place)
        
def orginize_plotos(directory):
    #extract place name.
    os.chdir(directory)
    originals = os.listdir()#list all directory 
    places = []#make a new list
    for filename in originals: #loop all directory 
        place = extract_place(filename)#each directory extract 
        if place not in places: #if places not include place, add place to list places.
            places.append(place)
    #use list to create new directory for each one
    make_place_directories(places)
    #move file to directories
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename,os.path.join(place, filename))


# In[ ]:




