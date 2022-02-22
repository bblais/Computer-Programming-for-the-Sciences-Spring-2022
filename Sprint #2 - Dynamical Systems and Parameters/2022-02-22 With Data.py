#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation


# In[5]:


from sci378 import *


# In[6]:


data=pd.read_csv('sample_position_data.csv')
data


# In[7]:


t_data=data['t']
y_data=data['y']
plot(t_data,y_data,'o')


# In[ ]:





# In[11]:


sim=Simulation()
sim.add("y'=v",100,plot=True)
sim.add("v'=a",0)
sim.params(a=-5)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(6)  # run until t=3


# In[ ]:




