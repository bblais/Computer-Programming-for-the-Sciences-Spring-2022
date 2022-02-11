#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# The exponential function can be approximated with a series as shown in https://en.wikipedia.org/wiki/Exponential_function#Computation
# 
# ![image.png](attachment:13eededb-b293-45a3-8577-f1884a78970b.png)
# 
# Say we want to write a function that gives us the 1st $n$ terms of this sum, and compare it to the python exponential function we could do it like:

# In[3]:


def factorial(n):
    value=1
    for v in range(1,n+1):
        value=value*v
        
    return value
    
def exponential_approximation(x,max_n=3):   # we'll do 3 terms by default
    total=0
    
    for n in range(max_n+1):
        total=total+x**n/factorial(n)
        
        
    return total


# In[4]:


exponential_approximation(.5),exp(.5)  # pretty close for small x


# In[5]:


exponential_approximation(3),exp(3) # gets bad for larger x


# In[7]:


exponential_approximation(3,max_n=10),exp(3) # gets closer for larger x if we include more terms


# ## a graphical way of seeing it

# In[28]:


x=linspace(0,8,100)
y=exp(x)

plot(x,y,label='True Exponential',linewidth=3)

for max_n in [3,6,9,12]:
    y=exponential_approximation(x,max_n)

    plot(x,y,label=f'{max_n} terms included')
    
legend(loc="upper left")

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

ax=inset_axes(gca(), width="30%", height="30%", loc='center')

x=linspace(0,6,100)
y=exp(x)
plot(x,y,label='True Exponential',linewidth=3)

for max_n in [3,6,9,12]:
    y=exponential_approximation(x,max_n)

    plot(x,y,label=f'{max_n} terms included')


# In[ ]:




