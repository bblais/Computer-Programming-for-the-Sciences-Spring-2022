#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


import pandas as pd
data=pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/boot/catsM.csv')
data.describe()


# In[4]:


data


# In[6]:


x=data['Bwt']
y=data['Hwt']

figure(figsize=(12,8))
plot(x,y,'ro')
xlabel('Body Weight [kg]')
ylabel('Heart Weight [g]')
title('My Lovely Cats and Their Hearts')


# In[ ]:




