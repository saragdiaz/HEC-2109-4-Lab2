#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[9]:


def COUNTFUNCTIONONFILE(input_filename):
    
    with open(input_filename,'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            lines = content.splitlines()
            characters = len(content)
            return len(words), characters, len(lines)

file = "ObamaFirstInagural.tex"
words,characters, lines =COUNTFUNCTIONONFILE("ObamaFirstInagural.tex")

print("Number of words, characters and lines in the file", file,"are ", words,",", characters,",",",and", lines, "accordingly")


# In[ ]:




