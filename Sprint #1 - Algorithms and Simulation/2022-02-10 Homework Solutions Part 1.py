#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from mplturtle import *


# ![image.png](attachment:9e29cb2e-8eeb-4c40-af1d-9f1f39085ada.png)

# In[3]:


reset()

forward(100)
backward(100)
left(5)

forward(100)
backward(100)
left(5)

forward(100)
backward(100)
left(5)


# In[6]:


reset()

for i in range(91):
    forward(100)
    backward(100)
    left(1)


# In[7]:


reset()

for i in range(271):
    forward(100)
    backward(100)
    right(1)


# In[8]:


reset()

for i in range(91):
    forward(100)
    backward(100)
    left(1)

    
pencolor("red")

for i in range(91):
    forward(100)
    backward(100)
    left(1)

    
pencolor("green")

for i in range(91):
    forward(100)
    backward(100)
    left(1)

    
pencolor("blue")

for i in range(91):
    forward(100)
    backward(100)
    left(1)

    


# In[9]:


reset()


for color in ["black","red","green","blue"]:
    pencolor(color)

    for i in range(91):
        forward(100)
        backward(100)
        left(1)

    


# In[11]:


reset()

right(30)
for color in ["red","green","blue"]:
    pencolor(color)

    for i in range(120):
        forward(100)
        backward(100)
        left(1)

    


# ![image.png](attachment:7abbd127-1005-49d6-9db1-05a86b29787e.png)

# In[12]:


def square(size=50):
    
    for i in range(4):
        forward(size)
        right(90)
        
    


# In[13]:


reset()
square()


# In[14]:


animate()


# In[27]:


reset()

N=10

for N in range(10,0,-1):


    for i in range(N):
        square()
        forward(50)

    penup()
    left(90)
    forward(50)
    left(90)
    forward(50*N-25)
    left(180)
    pendown()



# ![image.png](attachment:333e2ca8-1a63-45f0-a1eb-3fb22a8210e2.png)

# In[28]:


def hexagon(size=50):
    
    for i in range(6):
        forward(size)
        right(60)
        
    


# In[29]:


reset()
hexagon()


# In[36]:


reset()



for i in range(80):
    penup()
    forward(200)
    pendown()
    hexagon()
    penup()
    backward(200)
    pendown()
    left(5)
    
    
pencolor("red")

for i in range(80):
    penup()
    forward(150)
    pendown()
    hexagon()
    penup()
    backward(150)
    pendown()
    left(5)
    
pencolor("green")

for i in range(80):
    penup()
    forward(100)
    pendown()
    hexagon()
    penup()
    backward(100)
    pendown()
    left(5)    


# In[ ]:




