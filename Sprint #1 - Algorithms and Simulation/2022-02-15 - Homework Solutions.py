#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[3]:


from sci378 import *


# $$\frac{dx}{dt}= v$$
# 
# $$
# \frac{dv}{dt}= -k\cdot x/m
# $$
# 
# $$dx= v \cdot dt$$
# 
# $$
# dv= (-k\cdot x/m) \cdot dt
# $$
# 
# 
# 
# (suggested values k = 2 and m = 1, initial position x = 3 and speed v = 0)

# In[4]:


# initial values of variables
x=3
v=0
t=0

# values of parameters
k=2
m=1

dt=0.1

S=Storage()
S+=t,x,v

while t<20:
    
    dx=v*dt
    dv=-k*x/m*dt
    
    # update variables for a small time step dt
    
    x=x+dx
    v=v+dv
    t=t+dt
    
    S+=t,x,v

t,x,v=S.arrays()


# In[5]:


plot(t,x)


# In[6]:


plot(t,v)


# In[14]:


for k in [2,4,6]:
    # initial values of variables
    x=3
    v=0
    t=0

    # values of parameters
    #k=2
    m=1

    dt=0.001

    S=Storage()
    S+=t,x,v

    while t<20:

        dx=v*dt
        dv=-k*x/m*dt

        # update variables for a small time step dt

        x=x+dx
        v=v+dv
        t=t+dt

        S+=t,x,v

    t,x,v=S.arrays()



    plot(t,v,label=f"k={k}")

legend()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Another diff-eq

# $$
# \frac{dy}{dt} =  \frac{1}{2}{{\bf{e}}^{\frac{t}{2}}}\sin \left( {5t} \right) + 5{{\bf{e}}^{\frac{t}{2}}}\cos \left( {5t} \right)\hspace{0.25in}y\left( 0 \right) = 0$$

# Solution
# $$
# y\left( t \right) = {{\bf{e}}^{\frac{t}{2}}}\sin \left( {5t} \right)
# $$

# In[15]:


# initial values of variables
y=0
t=0

# values of parameters
# none!

dt=0.01

S=Storage()
S+=t,y

while t<20:
    
    dy=(0.5*exp(t/2)*sin(5*t) + 5*exp(t/2)*cos(5*t))*dt
    
    # update variables for a small time step dt
    
    y=y+dy
    t=t+dt
    
    S+=t,y

t,y=S.arrays()


# In[22]:


plot(t,y,linewidth=3)

y_analysis=exp(t/2)*sin(5*t)

plot(t,y_analysis,'-')


# In[ ]:




