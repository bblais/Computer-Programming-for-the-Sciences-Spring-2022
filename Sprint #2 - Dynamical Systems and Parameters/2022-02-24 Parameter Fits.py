#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation
from sci378 import *


# In[6]:


data=pd.read_csv('https://raw.githubusercontent.com/bblais/Computer-Programming-for-the-Sciences-Spring-2022/main/Sprint%20%232%20-%20Dynamical%20Systems%20and%20Parameters/logistic_sample_data/logistic_sample_data_0.csv')


# In[3]:


data=pd.read_csv('logistic_sample_data/logistic_sample_data_0.csv')
data


# In[5]:


figure(figsize=(8,4))
t_data=data['t']
y_data=data['y']
plot(t_data,y_data,'o')


# In[ ]:




