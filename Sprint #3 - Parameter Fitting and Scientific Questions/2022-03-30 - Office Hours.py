#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


from lmfit import *


# In[6]:


data=pd.read_csv('data/logistic_sample_data/logistic_sample_data_9.csv')
data


# In[7]:


t=data['t']
y=data['y']


# In[8]:


plot(t,y,'o')


# In[9]:


def f(x,a,b,c,d):
    return a/(1+exp(-c*(x-d)))+b


# In[23]:


xx=linspace(0,50,1000)
yy=f(xx,a=600,b=0.5,c=20,d=0.5)

plot(t,y,'o')
plot(xx,yy,'-')


# ## arccotagent

# In[20]:


arctan2(5,4)  # y=5, x=4


# In[19]:


arctan2(4,5)  # this is the arc cotangent


# compare with https://www.wolframalpha.com/input?i=arccot%285%2F4%29

# In[ ]:




