#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


pwd


# In[9]:


data=pd.read_csv('data/g149novickA.txt')
data


# In[6]:


data=pd.read_csv('data/HIVseries.csv',header=None)
data.columns=['Bob','Sally']
data


# In[7]:


get_ipython().run_line_magic('pinfo', 'pd.read_csv')


# In[11]:


x=randn(10000)
y=randn(10000)
plot(x,y,'o')
axis('equal')


# In[14]:


x=randn(10000)
y=randn(10000)
plot(x,y,'o',alpha=0.05)
axis('equal')


# In[ ]:




