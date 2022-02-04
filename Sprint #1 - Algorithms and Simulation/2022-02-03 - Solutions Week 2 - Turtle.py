#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[3]:


from mplturtle import *


# ![image.png](attachment:bffdfd84-8910-4d65-a00d-0bc9d040e16c.png)

# In[4]:


def draw_square(size):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)    


# In[9]:


reset()
draw_square(50)

penup()
left(90)
forward(5)
left(90)
forward(5)
right(180)
pendown()

draw_square(60)


# In[10]:


animate()


# In[11]:


def move_up_and_left(distance):
    penup()
    left(90)
    forward(distance)
    left(90)
    forward(distance)
    right(180)
    pendown()    


# In[12]:


reset()
draw_square(50)

move_up_and_left(5)

draw_square(60)


# In[14]:


reset()

size=10
step=5

for i in range(10):

    draw_square(size)
    move_up_and_left(step)
    size=size+2*step


# In[ ]:





# In[15]:


reset()
circle(50)


# In[16]:


animate()


# In[22]:


radius=50

reset()
penup()
right(90)
forward(radius)
left(90)
pendown()

circle(radius*2)

penup()
left(90)
forward(radius)
right(90)
pendown()


# In[24]:


animate(.01)


# In[25]:


def mycircle(radius):
    penup()
    right(90)
    forward(radius)
    left(90)
    pendown()

    circle(radius*2)

    penup()
    left(90)
    forward(radius)
    right(90)
    pendown()    


# In[26]:


reset()
mycircle(50)


# In[28]:


reset()
radius=10
step=5

for i in range(10):
    mycircle(radius)
    radius=radius+step


# ![image.png](attachment:ebe38ce0-cd0c-4648-8e8c-08ded97adec0.png)

# In[30]:


reset()
draw_square(50)

left(60)
forward(50)
right(120)
forward(50)
left(60)


# In[31]:


animate()


# In[32]:


def house(size):
    draw_square(size)

    left(60)
    forward(size)
    right(120)
    forward(size)
    left(60)    


# In[34]:


reset()
house(10)


# In[35]:


reset()

for i in range(3):
    house(10)
    penup()
    forward(20)
    pendown()


# In[40]:


reset()
size=10
step=20

for i in range(4):
    house(size)
    penup()
    forward(step)
    pendown()

penup()
right(90)
forward(3*size)
right(90)
forward(4*size+4*step)
right(180)
pendown()

    
    
    
for i in range(4):
    
    if i==1 or i==2:  # second house or third in the row
        penup()
        
    house(10)
    penup()
    forward(20)
    pendown()
    
    
penup()
right(90)
forward(3*size)
right(90)
forward(4*size+4*step)
right(180)
pendown()

    
    
    
for i in range(4):
    house(10)
    penup()
    forward(20)
    pendown()
        
    


# In[ ]:





# ![image.png](attachment:50f4d602-e027-4b0a-9451-94373760af86.png)

# In[42]:


for r in range(5):
    for c in range(5):
        print(r,c)


# In[44]:


reset()
size=10
step=10

count=0
for r in range(5):
    for c in range(5):
        
        if count==0:
            pencolor("black")
            count=1
        else:
            pencolor("red")
            count=0
        
        draw_square(size)
        penup()
        forward(size+step)
        pendown()
        
        
    
    penup()
    right(90)
    forward(size+step)
    right(90)
    forward(5*size+5*step)
    right(180)
    pendown()        


# In[ ]:




