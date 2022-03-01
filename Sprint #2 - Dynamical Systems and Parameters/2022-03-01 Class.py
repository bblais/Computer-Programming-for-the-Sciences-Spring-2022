#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation
from sci378 import *


# In[3]:


data=pd.read_csv('logistic_sample_data/logistic_sample_data_0.csv')
data


# In[5]:


t_data=data['t']
y_data=data['y']


# In[6]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",75,plot=True)
sim.params(a=1,k=50)
sim.add_data(t=t_data,x=y_data,plot=True)
sim.run(50)


# In[16]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",75)
sim.params(a=.1,k=50)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[17]:


plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[18]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",75)
sim.params(a=0.1,k=280)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[19]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",75)
sim.params(a=5,k=280)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[20]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",75)
sim.params(a=1,k=280)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[23]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",1)
sim.params(a=1,k=280)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[24]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",1)
sim.params(a=1.5,k=280)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[26]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",1)
sim.params(a=1.5,k=270)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# ## stability of fixed points
# 
# - x=0
# - x=k

# In[27]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",0)
sim.params(a=1.5,k=270)
sim.run(50)

plot(sim.t,sim.x)

sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",270)
sim.params(a=1.5,k=270)
sim.run(50)

plot(sim.t,sim.x)


# In[28]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",0.1)
sim.params(a=1.5,k=270)
sim.run(50)

plot(sim.t,sim.x)


# In[30]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",270+.1)
sim.params(a=1.5,k=270)
sim.run(50)

plot(sim.t,sim.x)


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",270-.1)
sim.params(a=1.5,k=270)
sim.run(50)

plot(sim.t,sim.x)



# In[ ]:




