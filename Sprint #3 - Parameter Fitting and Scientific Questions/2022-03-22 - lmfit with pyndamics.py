#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[5]:


import pandas as pd


# https://lmfit.github.io/lmfit-py/

# In[2]:


from pyndamics3 import Simulation


# In[4]:


t_data=array([7,14,21,28,35,42,49,56,63,70,77,84],float)
h_data=array([17.93,36.36,67.76,98.10,131,169.5,205.5,228.3,247.1,250.5,253.8,254.5])


# In[5]:


plot(t_data,h_data,'o')


# In[6]:


sim=Simulation()
sim.add("y' = a",0,plot=True)
sim.add_data(t=t_data,y=h_data,plot=True)
sim.params(a=1)
sim.run(80)


# In[3]:


from pyndamics3.fit import fit, Parameter


# In[8]:


results=fit(sim,
           Parameter("a",value=1,min=0))


# In[9]:


results


# In[10]:


sim.a


# In[11]:


sim.run(80)


# ## Logistic growth

# In[12]:


sim=Simulation()
sim.add("y' = a*y*(1-y/k)",1,plot=True)
sim.params(a=1,k=30)
sim.add_data(t=t_data,y=h_data,plot=True)
sim.run(80)


# In[17]:


results=fit(sim,
           Parameter("a",value=1,min=0,max=10),
           Parameter("k",value=30,min=0),
           )


# In[18]:


sim.run(80)


# In[16]:


results


# In[22]:


results=fit(sim,
           Parameter("a",value=1,min=0,max=10),
           Parameter("initial_y",value=1,min=0),
           Parameter("k",value=30,min=0),
           )
results


# In[20]:


sim.run(80)


# In[25]:


results=fit(sim,
           Parameter("a",value=1,min=0,max=10),
           Parameter("initial_y",value=1,min=0,max=20),
           Parameter("k",value=30,min=0),
           )
results


# In[26]:


sim.run(80)


# https://lmfit.github.io/lmfit-py/fitting.html?highlight=powell  methods described here, Powell works sometimes

# In[28]:


results=fit(sim,
           Parameter("a",value=1,min=0,max=10),
           Parameter("initial_y",value=1,min=0),
           Parameter("k",value=30,min=0),
            method="Powell"
           )
sim.run(80)
results


# ## population data

# In[10]:


data=pd.read_csv('data/s007.csv')
x_data=data['year']-1700
y_data=data['population (millions)']
data


# In[11]:


sim=Simulation()
sim.add("y' = a*y*(1-y/k)",1,plot=True)
sim.params(a=1,k=30)
sim.add_data(t=x_data,y=y_data,plot=True)
sim.run(80)


# In[12]:


results=fit(sim,
           Parameter("a",value=1,min=0,max=10),
           Parameter("initial_y",value=1,min=0,max=20),
           Parameter("k",value=30,min=0),
           )
results


# How to deal with nans -- drop them when you load them from pandas

# In[13]:


data=pd.read_csv('data/s007.csv')
data=data.dropna()
x_data=data['year']-1700
y_data=data['population (millions)']
data


# In[18]:


sim=Simulation()
sim.add("y' = a*y*(1-y/k)",1,plot=True)
sim.params(a=1,k=30)
sim.add_data(t=x_data,y=y_data,plot=True)
sim.run(300)


# In[23]:


results=fit(sim,
           Parameter("a",value=1,min=0,max=10),
           Parameter("initial_y",value=8,min=0,max=20),
           Parameter("k",value=30,min=0),
           )
results


# In[24]:


sim.run(300)


# In[22]:


plot(x_data,y_data,'o')
plot(sim.t,sim.y,'-')
xlabel('time [minutes]')


# In[ ]:




