#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pyndamics3 import Simulation
from sci378 import *


# In[3]:


data=pd.read_csv('logistic_sample_data/logistic_sample_data_0.csv')
data


# In[5]:


data=pd.read_csv('logistic_sample_data/logistic_sample_data_0.csv')
t_data=data['t']
y_data=data['y']


# In[6]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",75,plot=True)
sim.params(a=1,k=50)
sim.add_data(t=t_data,x=y_data,plot=True)
sim.run(50)


# In[16]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",75)
sim.params(a=.1,k=50)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[17]:


plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[18]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",75)
sim.params(a=0.1,k=280)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[19]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",75)
sim.params(a=5,k=280)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[20]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",75)
sim.params(a=1,k=280)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[23]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",1)
sim.params(a=1,k=280)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[24]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",1)
sim.params(a=1.5,k=280)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# In[26]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",1)
sim.params(a=1.5,k=270)
sim.run(50)

plot(sim.t,sim.x)
plot(t_data,y_data,'o')


# ## stability of fixed points
# 
# - x=0
# - x=k

# In[27]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",0)
sim.params(a=1.5,k=270)
sim.run(50)

plot(sim.t,sim.x)

sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",270)
sim.params(a=1.5,k=270)
sim.run(50)

plot(sim.t,sim.x)


# In[32]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",0.1)
sim.params(a=1.5,k=270)
sim.run(50)

plot(sim.t,sim.x)
title("Untable -- runs away from FP when started a little bit off of the FP")


# In[31]:


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",270+.1)
sim.params(a=1.5,k=270)
sim.run(50)

plot(sim.t,sim.x)


sim=Simulation()
sim.figsize=(8,4)
sim.add("x'=a*x*(1-x/k)",270-.1)
sim.params(a=1.5,k=270)
sim.run(50)

plot(sim.t,sim.x)


title("Stable -- approaches FP when started a little bit off of the FP")


# ## Non-zero mean SHO

# In[41]:


sim=Simulation()
sim.add("x'=v",30)
sim.add("v'=-k*x/m",0)
sim.params(k=2,m=1)
sim.run(50)


# In[44]:


new_y_data=y_data[3:]
new_t_data=t_data[3:]


# In[64]:


μ=median(new_y_data)
min_t=min(new_t_data)
plot(sim.t+min_t,sim.x+μ)

plot(new_t_data,new_y_data,'-o')


# In[60]:


sim=Simulation()
sim.add("x'=v",30)
sim.add("v'=-k*x/m",0)
sim.params(k=2,m=1)
sim.run(9,50)


#μ=median(new_y_data)
plot(sim.t,sim.x+260)

plot(new_t_data,new_y_data,'o')


# ## Data with dates

# In[5]:


get_ipython().run_line_magic('pylab', 'inline')
from sci378 import *


# In[6]:


data=pd.read_csv('http://jooskorstanje.com/full_data_logistic.csv',sep=';')
data


# In[22]:


date_to_float(data['date'],"european")


# In[23]:


x=data['date']
y=data['total_cases']
plot(x,y,'-o')
title('This is broken')


# In[24]:


x=date_to_float(data['date'],"european")
y=data['total_cases']
plot(x,y,'-o')


# In[25]:


x


# In[57]:


x


# ## Data on different time scales

# In[66]:


data=pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/datasets/nottem.csv")
data


# In[68]:


t_data=data['time']
x_data=data['value']
plot(t_data,x_data,'-o')


# In[69]:


sim=Simulation()
sim.add("x'=v",1)
sim.add("v'=-k*x/m",0)
sim.params(k=20,m=2)
sim.run(50)


# In[70]:


plot(sim.t,sim.x)


# In[75]:


t_data=data['time']
x_data=data['value']
t_data=t_data-min(t_data)
x_data=x_data-mean(x_data)
plot(t_data,x_data,'-o')


# In[76]:


plot(sim.t,sim.x)
plot(t_data,x_data,'-o')


# ## Y scales

# In[85]:


data=pd.read_csv('logistic_sample_data/logistic_sample_data_0.csv')
t_data=data['t']
y_data=data['y']

new_y_data=y_data[3:]*1000
new_t_data=t_data[3:]


new_y_data=new_y_data-mean(new_y_data)
plot(new_t_data,new_y_data,'-o')


# In[86]:


sim=Simulation()
sim.add("x'=v",1)
sim.add("v'=-k*x/m",0)
sim.params(k=20,m=2)
sim.run(50)

plot(sim.t,sim.x)
plot(new_t_data,new_y_data,'-o')


# In[89]:


sim=Simulation()
sim.add("x'=v",1)
sim.add("v'=-k*x/m",0)
sim.params(k=20,m=2)
sim.run(50)

plot(sim.t,sim.x)


sim=Simulation()
sim.add("x'=v",10)
sim.add("v'=-k*x/m",0)
sim.params(k=20,m=2)
sim.run(50)

plot(sim.t,sim.x)


# In[ ]:


data=pd.read_excel("filename")

