#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from mplturtle import *


# - draw a pyramid
# 
# 
# - draw a square
# 
# - draw a number of squares in a row
# 
# - start a new row (up and left)
# 
# - draw a number of squares in a row, but fewer than the previous row
# 

# In[3]:


def square(size=50):
    for i in range(4):
        forward(size)
        right(90)


# In[4]:


reset()
square()


# In[8]:


reset()
square()
forward(50)
square()
forward(50)
square()


# In[10]:


reset()
square()
forward(50)
square()
forward(50)
square()
forward(50)
square()
forward(50)
square()
forward(50)
square()
forward(50)
square()
forward(50)









# In[23]:


reset()

N=5


for i in range(N):
    square()
    forward(50)

pencolor("red")
left(90)
forward(50)
left(90)
forward(225)
left(180)

for i in range(N-1):
    square()
    forward(50)


# In[19]:


animate()


# In[ ]:




