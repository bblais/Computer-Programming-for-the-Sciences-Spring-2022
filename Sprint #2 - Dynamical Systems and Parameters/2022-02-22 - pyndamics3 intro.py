#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation


# $$
# \frac{dy}{dt}=v
# $$
# 
# 
# $$
# \frac{dv}{dt}=a
# $$
# 
# $$a=-10, x_o=100, v_o=0$$
# 
# 

# In[12]:


sim=Simulation()
sim.add("y'=v",100,plot=True)
sim.add("v'=a",0,plot=True)
sim.params(a=-10)
sim.run(5)  # run until t=3


# In[13]:


sim=Simulation()
sim.add("y'=v",100)
sim.add("v'=a",0)
sim.params(a=-10)
sim.run(3)  # run until t=3


# In[15]:


t,x=sim.t,sim.y
plot(t,x,'r-')


# In[9]:


for a in [-10,-8,-6]:
    sim=Simulation()
    sim.add("x'=v",100)
    sim.add("v'=a",0)
    sim.params(a=a)
    sim.run(3)  # run until t=3    
    
    
    t,x=sim.t,sim.x
    plot(t,x,'-',label=f"a={a}")    
    
legend()


# In[ ]:




