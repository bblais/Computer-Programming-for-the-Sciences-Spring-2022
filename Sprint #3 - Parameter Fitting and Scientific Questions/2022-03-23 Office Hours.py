#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation


# In[3]:


t_data=array([7,14,21,28,35,42,49,56,63,70,77,84],float)
h_data=array([17.93,36.36,67.76,98.10,131,169.5,205.5,228.3,247.1,250.5,253.8,254.5])


# In[8]:


sim=Simulation()
sim.add("y' = a*y*(1-y/k)",10,plot=True)
sim.params(a=.1,k=250)
sim.add_data(t=t_data,y=h_data,plot=True)
sim.run(80)


# ## Plot "by-hand" instead of with plot=True pyndamics thing

# In[9]:


sim=Simulation()
sim.add("y' = a*y*(1-y/k)",10,plot=False)
sim.params(a=.1,k=250)
sim.add_data(t=t_data,y=h_data,plot=False)
sim.run(80)


# In[10]:


plot(t_data,h_data,'bo')
plot(sim.t,sim.y,'b-')
xlabel('time [minutes]')
ylabel('population')


# In[24]:


sim=Simulation()
sim.add("y' = a*y*(1-y/k)",10,plot=False)
sim.params(a=.1,k=250)
sim.add_data(t=t_data,y=h_data,plot=False)
sim.run(90)


plot(t_data,h_data,'bo')
plot(sim.t,sim.y,'b-')
xlabel('time [minutes]')
ylabel('population')

sim=Simulation()
sim.add("y' = a*y*(1-y/k)",250,plot=False)
sim.params(a=.1,k=250)
sim.add_data(t=t_data,y=h_data,plot=False)
sim.run(90)

plot(sim.t,sim.y,'r-')


sim=Simulation()
sim.add("y' = a*y*(1-y/k)",0,plot=False)
sim.params(a=.1,k=250)
sim.add_data(t=t_data,y=h_data,plot=False)
sim.run(90)

plot(sim.t,sim.y,'g-')

sim=Simulation()
sim.add("y' = a*y*(1-y/k)",0.1,plot=False)
sim.params(a=.1,k=250)
sim.add_data(t=t_data,y=h_data,plot=False)
sim.run(90)

plot(sim.t,sim.y,'g--')

sim=Simulation()
sim.add("y' = a*y*(1-y/k)",240,plot=False)
sim.params(a=.1,k=250)
sim.add_data(t=t_data,y=h_data,plot=False)
sim.run(90)

plot(sim.t,sim.y,'r--')



sim=Simulation()
sim.add("y' = a*y*(1-y/k)",10,plot=False)
sim.params(a=.1,k=150
          )
sim.add_data(t=t_data,y=h_data,plot=False)
sim.run(90)


plot(sim.t,sim.y,'b:')


sim=Simulation()
sim.add("y' = a*y*(1-y/k)",10,plot=False)
sim.params(a=.3,k=250)
sim.add_data(t=t_data,y=h_data,plot=False)
sim.run(90)


plot(sim.t,sim.y,'b:')



# ## Fixed points for free fall

# $$
# v' = g - \frac{k v^2}{m}
# $$

# $$
# v' = g - \frac{k v^2}{m} = 0
# $$
# 
# $$
# g - \frac{k v^2}{m} = 0
# $$

# $$
# m g - k v^2 = 0
# $$

# -----
# $$
# 5-x=0
# $$

# $$
# 5=x
# $$

# $$
# -x=-5
# $$

# $$
# x=5
# $$
# 
# ----

# $$
# m g - k v^2 = 0
# $$
# 
# $+kv^2$ to both sides
# 
# $$
# m g = k v^2 
# $$
# 

# $$
# \frac{m g}{k} = v^2 
# $$
# 
# $$
# v^2 = \frac{m g}{k} 
# $$
# 

# $$
# v = \sqrt{\frac{m g}{k}}
# $$
# 

# $$
# x^2=25
# $$

# $$
# x=5,-5
# $$

# $$
# v = \pm \sqrt{\frac{m g}{k}}
# $$
# 

# In[ ]:




