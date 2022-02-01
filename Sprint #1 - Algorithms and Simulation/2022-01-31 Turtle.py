#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


sin(radians(90))


# In[3]:


from mplturtle import *


# In[6]:


pwd


# In[7]:


ls


# In[13]:


reset()

# draw a square
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)

# move to the next square
penup()
forward(100)
pendown()

# draw a square
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)


# In[9]:


animate()


# In[14]:


reset()

for i in range(10):

    # draw a square
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)


    # move to the next square
    penup()
    forward(100)
    pendown()


# In[16]:


reset()

# draw a square
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)

# move to the next square
penup()
forward(100)
pendown()
pencolor("red")

# draw a square
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)


# In[17]:


def draw_square():
    # draw a square
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)


# In[18]:


reset()
draw_square()


# In[19]:


reset()

for i in range(10):

    draw_square()


    # move to the next square
    penup()
    forward(100)
    pendown()


# In[20]:


def draw_square(size=50):
    # draw a square
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)


# In[26]:


reset()

for i in range(10):

    draw_square(80)


    # move to the next square
    penup()
    forward(100)
    pendown()

    print(i)

    if i>5:
        print("red")
        pencolor("red")


# In[ ]:




