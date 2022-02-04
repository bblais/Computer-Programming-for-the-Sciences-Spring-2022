#!/usr/bin/env python
# coding: utf-8

# Factorial
# 
# $$
# 1 \times 2 \times 3 \times \cdots \times N
# $$

# In[3]:


def factorial_return(N):
    total=1
    for i in range(N):  
        value=i+1
        total=total*value
        
    return total


# In[4]:


def factorial_print(N):
    total=1
    for i in range(N):  
        value=i+1
        total=total*value
        
    print(total)


# In[5]:


factorial_return(5)


# In[6]:


factorial_print(5)


# In[7]:


a=factorial_return(5)
print(2*a)


# In[8]:


a=factorial_print(5)
print(2*a)


# In[9]:


def factorial(N):
    total=1
    for value in range(1,N+1):  
        total=total*value
        
    return total


# In[10]:


factorial(5)


# In[14]:


from math import sin,cos
from pylab import rand


# In[13]:


angle=15
sin(angle)**2 + cos(angle)**2


# In[15]:


for i in range(100):
    angle=rand()*100
    print(angle,"    ",sin(angle)**2 + cos(angle)**2)


# In[ ]:




