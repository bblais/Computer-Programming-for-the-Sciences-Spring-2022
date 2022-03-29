#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


from lmfit import *


# In[4]:


data=pd.read_csv('data/station.csv')


# In[5]:


data


# In[7]:


x=data['YEAR']
y=data['metANN']

x=x[y<200]
y=y[y<200]


plot(x,y,'-o')


# In[ ]:




