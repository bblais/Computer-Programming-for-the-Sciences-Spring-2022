#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation
from sci378 import *


# ## Logistic Growth with Data

# In[32]:


sim=Simulation()
sim.add("x' = a*x*(1-x/K)",1,plot=True)
sim.params(a=1,K=50)
sim.run(10)


# In[33]:


data=pd.read_excel('Mobile telephone service.xlsx')
data


# In[34]:


t=data['Year']
x=data['Americans with Cellular Service (%)']
plot(t,x,'ro-')


# In[35]:


t=data['Year']
t=t-min(t)
x=data['Americans with Cellular Service (%)']
plot(t,x,'ro-')


# In[50]:


sim=Simulation()
sim.add("x' = a*x*(1-x/K)",13)
sim.params(a=.25,K=110)
sim.run(17.5)


plot(sim.t,sim.x)
plot(t,x,'ro-')



# ## forced to have K=100 because the variable is a percentage

# In[53]:


sim=Simulation()
sim.add("x' = a*x*(1-x/K)",13)
sim.params(a=.29,K=100)
sim.run(17.5)


plot(sim.t,sim.x)
plot(t,x,'ro-')



# ## Oscillator with Data

# In[55]:


sim=Simulation()
sim.add("x'=v",1)
sim.add("v'=-k*x/m",0)
sim.params(k=2,m=1)
sim.run(10)

plot(sim.t,sim.x)


# In[59]:


data=pd.read_csv('vostok.icecore.co2.txt',sep="\t",skiprows=21,header=None)
data


# In[67]:


t=data[2]
x=data[3]
t=t/100
x=x-mean(x)
plot(t,x,'r-o')
xlabel("Time BP centuries")


# In[75]:


sim=Simulation()
sim.add("x'=v",50)
sim.add("v'=-k*x/m",0)
sim.params(k=.000035,m=1)
sim.run(4000)

plot(sim.t,sim.x)

plot(t,x,'r-o')


# ## Predator Prey Fixed Points

# In[76]:


sim=Simulation()
sim.add("x'=α*x-β*x*y",10,plot=1)
sim.add("y'=δ*x*y-γ*y",10,plot=1)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)


# \begin{aligned}
# \frac{dx}{dt}&= \alpha x - \beta x y\\
# \frac{dy}{dt}&= \delta xy - \gamma y
# \end{aligned}
# 
# Fixed points
# 
# \begin{aligned}
# 0&= \alpha x - \beta x y\\
# 0&= \delta xy - \gamma y
# \end{aligned}
# solve for my variables ($x,y$)
# 
# \begin{aligned}
# 0&= x(\alpha - \beta y)\\
# 0&= y(\delta y - \gamma)
# \end{aligned}
# 
# * $x,y=(0,0)$
# * $x,y=(\gamma/\delta, \alpha/\beta)$

# In[77]:


sim=Simulation()
sim.add("x'=α*x-β*x*y",0,plot=1)
sim.add("y'=δ*x*y-γ*y",0,plot=1.)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)


# In[78]:


sim=Simulation()
sim.add("x'=α*x-β*x*y",.4/.1,plot=1)
sim.add("y'=δ*x*y-γ*y",1.1/.4,plot=1)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)


# In[82]:


sim=Simulation()
sim.add("x'=α*x-β*x*y",0)
sim.add("y'=δ*x*y-γ*y",0)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)

plot(sim.t,sim.x,'b-')
plot(sim.t,sim.y,'r-')


sim=Simulation()
sim.add("x'=α*x-β*x*y",0.1)
sim.add("y'=δ*x*y-γ*y",0.1)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)

plot(sim.t,sim.x,'b-')
plot(sim.t,sim.y,'r-')


# In[83]:


sim=Simulation()
sim.add("x'=α*x-β*x*y",0)
sim.add("y'=δ*x*y-γ*y",0)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)

plot(sim.t,sim.x,'b-')
plot(sim.t,sim.y,'r-')


sim=Simulation()
sim.add("x'=α*x-β*x*y",0)
sim.add("y'=δ*x*y-γ*y",0.1)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)

plot(sim.t,sim.x,'b-')
plot(sim.t,sim.y,'r-')


# In[84]:


sim=Simulation()
sim.add("x'=α*x-β*x*y",0)
sim.add("y'=δ*x*y-γ*y",0)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)

plot(sim.t,sim.x,'b-')
plot(sim.t,sim.y,'r-')


sim=Simulation()
sim.add("x'=α*x-β*x*y",0.1)
sim.add("y'=δ*x*y-γ*y",0)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)

plot(sim.t,sim.x,'b-')
plot(sim.t,sim.y,'r-')


# In[86]:



sim=Simulation()
sim.add("x'=α*x-β*x*y",.4/.1)
sim.add("y'=δ*x*y-γ*y",1.1/.4)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)

plot(sim.t,sim.x,'b-')
plot(sim.t,sim.y,'r-')


sim=Simulation()
sim.add("x'=α*x-β*x*y",.4/.1+.1)
sim.add("y'=δ*x*y-γ*y",1.1/.4+.1)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)

plot(sim.t,sim.x,'b-')
plot(sim.t,sim.y,'r-')


# In[87]:



sim=Simulation()
sim.add("x'=α*x-β*x*y",.4/.1)
sim.add("y'=δ*x*y-γ*y",1.1/.4)
sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
sim.run(100)

plot(sim.t,sim.x,'b-')
plot(sim.t,sim.y,'r-')

for i in range(10):
    r1=randn()*.1
    r2=randn()*.1    
    sim=Simulation()
    sim.add("x'=α*x-β*x*y",.4/.1+r1)
    sim.add("y'=δ*x*y-γ*y",1.1/.4+r2)
    sim.params(α=1.1,β=0.4,δ=.1,γ=.4)
    sim.run(100)

    plot(sim.t,sim.x,'b-',alpha=0.1)
    plot(sim.t,sim.y,'r-',alpha=0.1)


# In[ ]:




