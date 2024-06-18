#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Dog:
    def speak(self):
        print("woof!")

    def __init__(self, name):
        self.name = name

    def hear(self, words):#when dog hear some one call it, dog speak
        if self.name in words:
            self.speak()


# In[ ]:




