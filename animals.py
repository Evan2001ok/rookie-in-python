#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Dog:
    def speak(self):
        print("woof!")

    def __init__(self, name):
        self.name = name
        self.times = 0

    def hear(self, words):#when dog hear some one call it, dog speak
        if self.name in words:
            self.speak()
    def count(self):#function of when count++ speak++
        self.times += 1
        for x in range(self.times):
            self.speak()

# In[ ]:




