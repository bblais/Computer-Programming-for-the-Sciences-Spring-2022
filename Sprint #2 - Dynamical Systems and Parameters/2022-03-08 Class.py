#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation


# In[25]:


sim=Simulation()
sim.add("N'=r*N*(1-N/K)-H",1,plot=True)
sim.params(r=1,K=50,H=.979)
sim.run(600)


# In[26]:


sim=Simulation()
sim.add("x'=v",1)
sim.add("v'=a",0)
sim.add("a=k*vm*exp(-k*t)")
sim.params(k=3,vm=2)
sim.run(600)


# In[28]:


import pandas as pd


# In[30]:


pwd


# In[ ]:


pd.read_csv('c:/Users/bblais/Downloads/somefile.csv')


# In[32]:


pd.read_csv('logistic_sample_data/logistic_sample_data_0.csv')


# In[41]:


data=pd.read_csv('FISH_LAND.csv')
data


# In[42]:


set(data['Species'])


# In[43]:


data=data[data['Species']=='Japanese seabass [Lateolabrax japonicus]']
data=data[data['MEASURE']=='TON']
data


# In[44]:


t=data['Year']
y=data['Value']
plot(t,y,'o')


# In[46]:


t=data['Year']
y=data['Value']/1000
plot(t,y,'o')
ylabel('Tons [thousands]')


# In[ ]:




