#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation
from sci378 import *


# In[4]:


data=pd.read_excel('Mobile telephone service.xlsx')
data


# In[9]:


t=data['Year']
x=data['Americans with Cellular Service (%)']
t=t-min(t)  # this data doesn't start at t=0, so adjust


# In[53]:


sim=Simulation()
sim.add("x' = a*x*(1-x/K)",13)
sim.params(a=.25,K=110)
sim.run(20)

plot(sim.t,sim.x,'g-')
plot(t,x,'bo-')

# plot the x=0 fixed point
sim=Simulation()
sim.add("x' = a*x*(1-x/K)",0)
sim.params(a=.25,K=110)
sim.run(20)
plot(sim.t,sim.x,'r-')


# plot the x=K fixed point
sim=Simulation()
sim.add("x' = a*x*(1-x/K)",110)
sim.params(a=.25,K=110)
sim.run(20)
plot(sim.t,sim.x,'r-')

xlabel('Time [years]')
ylabel('Percent Cell Service')


# In[52]:


sim=Simulation()
sim.add("x' = a*x*(1-x/K)",13)
sim.params(a=.25,K=110)
sim.run(20)

plot(sim.t,sim.x,'g-')
plot(t,x,'bo-')

# plot the x=0 fixed point
sim=Simulation()
sim.add("x' = a*x*(1-x/K)",0)
sim.params(a=.25,K=110)
sim.run(20)
plot(sim.t,sim.x,'r-')


# plot the x=K fixed point
sim=Simulation()
sim.add("x' = a*x*(1-x/K)",110)
sim.params(a=.25,K=110)
sim.run(20)
plot(sim.t,sim.x,'r-')

xlabel('Time [years]')
ylabel('Percent Cell Service')


# probably easier to do this in powerpoint, but this gives you the idea

text(12, 60, "Equation: $x'=ax(1-x/K)$", style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
text(12, 40, "FP: $ax(1-x/K)=0$\n$x=0,x=K$", style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
text(0, 70, "Params: $a=0.25, K=110$", style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})


annotate('$x=0$ fixed point (unstable)',(18,0),xytext=(12,10), arrowprops=dict(arrowstyle="->"))
annotate('$x=K$ fixed point (stable)',(1,109),xytext=(1,90), arrowprops=dict(arrowstyle="->"))


# ## data and variable names

# In[55]:


# plot the x=K fixed point
sim=Simulation()
sim.add("bob' = a*bob*(1-bob/K)",13,plot=True)
sim.params(a=.25,K=110)
sim.run(20)


# In[56]:


sally=data['Year']
frank=data['Americans with Cellular Service (%)']
sally=sally-min(sally)  # this data doesn't start at t=0, so adjust


# In[57]:


# plot the x=K fixed point
sim=Simulation()
sim.add("bob' = a*bob*(1-bob/K)",13,plot=True)
sim.params(a=.25,K=110)
sim.add_data(t=sally,bob=frank,plot=True      )
sim.run(20)


# In[ ]:




