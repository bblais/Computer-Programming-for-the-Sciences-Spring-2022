#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation
from sci378 import *


# In[6]:


data=pd.read_csv('https://raw.githubusercontent.com/bblais/Computer-Programming-for-the-Sciences-Spring-2022/main/Sprint%20%232%20-%20Dynamical%20Systems%20and%20Parameters/logistic_sample_data/logistic_sample_data_0.csv')


# In[7]:


data=pd.read_csv('logistic_sample_data/logistic_sample_data_0.csv')
data


# In[8]:


figure(figsize=(8,4))
t_data=data['t']
y_data=data['y']
plot(t_data,y_data,'o')


# In[20]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",75,plot=True)
sim.params(a=1,k=50)
sim.add_data(t=t_data,x=y_data,plot=True)
sim.run(50)


# In[16]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",1,plot=True)
sim.params(a=1.5,k=275)
sim.add_data(t=t_data,x=y_data,plot=True)
sim.run(50)


# <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/eba353633616971f427b13e175bfbdb1b99bcff0">

# In[21]:


"α*x-β*x*y"


# In[24]:


data=pd.read_csv("https://raw.githubusercontent.com/bblais/Systems-Modeling-Spring-2015-Notebooks/master/data/Lynx%20and%20Hare%20Data/lynxhare.csv",
                sep=";")
data


# In[25]:


t=data['year']
y1=data['hare']
y2=data['lynx']


# In[28]:


figure(figsize=(8,4))
plot(t,y1,'-o',label='hare')
plot(t,y2,'-o',label='lynx')
legend()


# In[ ]:




