#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# ## Exponential growth

# In[13]:


# initial values of variables
po=1
p=po
t=0

# values of parameters
a=2

dt=0.01

S=Storage()
S+=t,p

while t<3:
    
    dp=a*p*dt
    
    # update variables for a small time step dt
    
    p=p+dp
    t=t+dt
    
    S+=t,p

t,p=S.arrays()


# In[14]:


plot(t,p)
ylabel('population')
xlabel('time')


# $$
# \frac{dp}{dt}=a\cdot p
# $$

# $$
# p(t) = p_o e^{at}
# $$

# In[15]:


plot(t,p)

p_analysis=po*exp(a*t)
plot(t,p_analysis)
ylabel('population')
xlabel('time')


# In[18]:


plot(t,p,color='cyan')

p_analysis=po*exp(a*t)
plot(t,p_analysis,color='#871cc9')
ylabel('population')
xlabel('time')


# In[ ]:




