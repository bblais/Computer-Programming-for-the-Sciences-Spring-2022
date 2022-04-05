#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


pwd


# In[9]:


data=pd.read_csv('data/g149novickA.txt')
data


# In[6]:


data=pd.read_csv('data/HIVseries.csv',header=None)
data.columns=['Bob','Sally']
data


# In[7]:


get_ipython().run_line_magic('pinfo', 'pd.read_csv')


# In[11]:


x=randn(10000)
y=randn(10000)
plot(x,y,'o')
axis('equal')


# In[17]:


x=randn(10000)+.3
y=randn(10000)+.2
plot(x,y,'o',alpha=0.05)
plot([0,0],[-4,4],'k-')
plot([-4,4],[0,0],'k-')

axis('equal')


# In[18]:


linspace(0,3,8)


# In[20]:


linspace(0,3,12)


# In[21]:


linspace(0,4,12)


# In[26]:


x=linspace(0,2*pi,10)
y=sin(x)
plot(x,y,'-o')


# In[31]:


x=randn(10000)+.3
y=randn(10000)+.2
plot(x,y,'o',alpha=1)
plot([0,0],[-4,4],'k-')
plot([-4,4],[0,0],'k-')

xlim([0,.2])
ylim([0,.2])
#axis('equal')


# ## SIR Model

# In[32]:


from pyndamics3 import Simulation


# In[36]:


sim=Simulation()
sim.add("S' = -β*S*I/N",100,plot=1)
sim.add("I' = +β*S*I/N - γ*I",1,plot=1)
sim.add("R' = +γ*I",0,plot=1)
sim.params(β=2,γ=1,N=101)
sim.run(10)


# In[38]:


sim=Simulation()
sim.add("S' = -β*S*I/N",100,plot=1)
sim.add("I' = +β*S*I/N - γ*I",1,plot=1)
sim.add("R' = +γ*I",0,plot=1)
sim.add("N = S+I+R",plot=1)
sim.params(β=2,γ=1)
sim.run(10)


# In[39]:


x=sim.t
y=sim.I

plot(x,y)


# In[40]:


x=sim.t
y=max(sim.I)-sim.I

plot(x,y)


# In[ ]:




