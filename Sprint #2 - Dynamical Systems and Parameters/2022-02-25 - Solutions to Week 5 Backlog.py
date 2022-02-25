#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[4]:


from pyndamics3 import Simulation
from sci378 import *


# $$\frac{dx}{dt}=ax\left(1-\frac{x}{K}\right)$$

# In[5]:


sim=Simulation()
sim.add("x' = a*x*(1-x/K)",1,plot=True)
sim.params(a=1,K=50)
sim.run(10)


# $$\frac{dx}{dt}= v$$
# 
# $$\frac{dv}{dt}= -k\cdot x/m$$

# In[6]:


sim=Simulation()
sim.add("x'=v",1)
sim.add("v'=-k*x/m",0)
sim.params(k=2,m=1)
sim.run(10)


# In[10]:


subplot(2,1,1)
plot(sim.t,sim.x)
ylabel('x')
gca().set_xticklabels([])
subplot(2,1,2)
plot(sim.t,sim.v)
ylabel('v')
xlabel('t')


# <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/eba353633616971f427b13e175bfbdb1b99bcff0">

# ![image.png](attachment:9bf25939-8691-425f-a323-7fe34236b592.png)![image.png](attachment:47d0362f-fb22-4280-86f5-fad95086d22e.png)

# In[12]:


sim=Simulation()
sim.add("x'=α*x-β*x*y",10,plot=1)
sim.add("y'=δ*x*y-γ*y",10,plot=1)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)


# In[17]:


plot(sim.t,sim.x,label='Baboons')
plot(sim.t,sim.y,label='Cheetahs')
legend(loc='upper left')
ylim([0,37])


# In[ ]:




