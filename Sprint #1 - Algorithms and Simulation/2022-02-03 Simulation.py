#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# - markdown syntax
# - to format equations, it uses LaTeX format
# 
# $$
# \frac{dx}{dt} = 5
# $$

# In[6]:


# initial conditions
xo=2
to=0


# In[4]:


# parameters

# none!


# In[5]:


dt=0.1


# In[9]:


x=xo
t=to
for i in range(20):
    dx=5*dt
    x=x+dx
    t=t+dt
    
    print(t,x)


# In[11]:


S=Storage()

x=xo
t=to

S+=t,x

for i in range(20):
    dx=5*dt
    x=x+dx
    t=t+dt
    
    S+=t,x


t,x=S.arrays()
t,x


# In[12]:


plot(t,x)


# if for some reason your sci378 is not working,

# In[19]:


S=[]

x=xo
t=to

S+=[(t,x)]

for i in range(20):
    dx=5*dt
    x=x+dx
    t=t+dt
    
    S+=[(t,x)]

t,x=zip(*S)


# In[21]:


plot(t,x)


# $$
# \frac{dx}{dt}=v
# $$
# 
# $$
# \frac{dv}{dt}=a
# $$
# 
# $$
# a=-10
# $$
# 

# In[23]:


S=Storage()

a=-10  # parameter

x=20  # initial conditions for each variable
v=0
t=0

S+=t,x,v
for i in range(20):
    
    # calculate change for each variable
    dx=v*dt
    dv=a*dt
    
    
    # uodate each variable
    x=x+dx
    v=v+dv
    t=t+dt
    
    # store the calculations
    S+=t,x,v

t,x,v=S.arrays()


# In[24]:


plot(t,x)
xlabel('time')
ylabel('position')


# In[25]:


plot(t,v)
xlabel('time')
ylabel('speed')


# In[ ]:




