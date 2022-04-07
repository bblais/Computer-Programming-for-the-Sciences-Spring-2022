#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation


# In[3]:


t_data=array([7,14,21,28,35,42,49,56,63,70,77,84],float)
h_data=array([17.93,36.36,67.76,98.10,131,169.5,205.5,228.3,247.1,250.5,253.8,254.5])


# In[15]:


sim=Simulation()
sim.add("y' = a*y*(1-y/k)",10,plot=1)
sim.add("x' = b",10,plot=1)
sim.params(a=.1,k=250,b=3)
sim.add_data(t=t_data,y=h_data,plot=True)
sim.run(90)


# https://www.w3schools.com/colors/colors_picker.asp

# In[20]:


plot(t_data,h_data,'-o',color='#9b42f5')
plot(sim.t,sim.y,'b-')
plot(sim.t,sim.x,'r-')


# In[23]:


sim=Simulation()
sim.add("y' = a*y*(1-y/k)",10,plot=1)
sim.params(a=.1,k=250,b=3)
sim.add_data(t=t_data,y=h_data,plot=True)
sim.run(90)

t1=sim.t
y1=sim.y


# In[24]:


sim=Simulation()
sim.add("y' = a*y*(1-y/k)",10,plot=1)
sim.params(a=3,k=100)
sim.add_data(t=t_data,y=h_data,plot=True)
sim.run(90)


t2=sim.t
y2=sim.y


# In[26]:


plot(t_data,h_data,'o')
plot(t1,y1,'b-')
plot(t2,y2,'r--')


# In[ ]:




