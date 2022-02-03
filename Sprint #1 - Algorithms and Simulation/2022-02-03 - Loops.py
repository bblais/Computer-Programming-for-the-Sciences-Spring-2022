#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from mplturtle import *


# In[3]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)


# In[5]:


reset()
square(50)


# In[6]:


reset()
size=50
offset=20

for i in range(10):
    forward(offset)
    square(size)
    
    size=size+5
    offset=offset-2


# In[ ]:




