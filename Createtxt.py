#!/usr/bin/env python
# coding: utf-8
strs = []
for even in range(0,31,2):
    strs.append(str(even))
    
with open("sure.txt","w") as f:
    f.write("if you feel good, just relax")
    f.write("".join(strs))
    #add more words you like