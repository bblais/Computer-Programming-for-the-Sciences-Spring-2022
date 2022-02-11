#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('pylab', 'inline')


# In[4]:


from sci378 import *


# $$\frac{dx}{dt}=ax\left(1-\frac{x}{K}\right)$$
# 
# $$dx=ax\left(1-\frac{x}{K}\right) \times dt$$
# 
# (suggested values a = 2 and K=50, initial x = 10)

# - What are the variables?   x
# - What are the parameters?  a, K

# In[7]:


# initial values of variables
x=10
t=0

# values of parameters
a=2
K=50

dt=0.1

S=Storage()
S+=t,x

while t<20:
    dx=a*x*(1-x/K)*dt
    
    # update variables for a small time step dt
    
    x=x+dx
    t=t+dt

    S+=t,x
    
t,x=S.arrays()
    


# In[8]:


plot(t,x)


# In[ ]:





# In[16]:


for a in [2,4,6]:
    # initial values of variables
    x=10
    t=0

    # values of parameters
    #a=2
    K=50

    dt=0.01

    S=Storage()
    S+=t,x

    while t<5:
        dx=a*x*(1-x/K)*dt

        # update variables for a small time step dt

        x=x+dx
        t=t+dt

        S+=t,x

    t,x=S.arrays()
    
    plot(t,x,label=f"a={a}")
    
    
xlabel('Time')
ylabel('Population')
legend()


# In[17]:


for K in [5,20,50]:
    # initial values of variables
    x=10
    t=0

    # values of parameters
    a=2
    #K=50

    dt=0.01

    S=Storage()
    S+=t,x

    while t<5:
        dx=a*x*(1-x/K)*dt

        # update variables for a small time step dt

        x=x+dx
        t=t+dt

        S+=t,x

    t,x=S.arrays()
    
    plot(t,x,label=f"K={K}")
    
    
xlabel('Time')
ylabel('Population')
legend()


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

# - What are the variables?   x,v
# - What are the parameters?  k, m

# In[9]:


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


# In[10]:


plot(t,x)


# In[11]:


plot(t,v)


# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


import pandas as pd
data=pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/boot/catsM.csv')
data.describe()


# From the doc https://vincentarelbundock.github.io/Rdatasets/doc/MASS/cats.html
# 
#     Anatomical Data from Domestic Cats
#     Description
#     The heart and body weights of samples of male and female cats used for digitalis experiments. The cats were all adult, over 2 kg body weight.
# 
#     Usage
#     cats
#     Format
#     This data frame contains the following columns:
# 
#     Sex
#     sex: Factor with levels "F" and "M".
# 
#     Bwt
#     body weight in kg.
# 
#     Hwt
#     heart weight in g.
# 
#     Source
#     R. A. Fisher (1947) The analysis of covariance method for the relation between a part and the whole, Biometrics 3, 65–68.
# 
#     References
#     Venables, W. N. and Ripley, B. D. (2002) Modern Applied Statistics with S. Fourth edition. Springer.

# In[ ]:




