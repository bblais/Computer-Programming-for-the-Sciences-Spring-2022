#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from mplturtle import *


# In[3]:


for i in range(3):
    forward(50)
    right(30)
    forward(60)
    left(30)
    
    penup()
    forward(100)
    pendown()


# In[4]:


def worms():
    for i in range(3):
        forward(50)
        right(30)
        forward(60)
        left(30)

        penup()
        forward(100)
        pendown()    


# In[5]:


reset()
worms()


# In[6]:


def worms2(N=3):
    for i in range(N):
        forward(50)
        right(30)
        forward(60)
        left(30)

        penup()
        forward(100)
        pendown()    


# In[9]:


reset()
worms2(5)


# In[ ]:




