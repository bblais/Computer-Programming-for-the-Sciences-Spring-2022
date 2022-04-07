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


# In[29]:


figure(figsize=(12,8))
subplot(2,1,1)
plot(t_data,h_data,'o')
plot(t1,y1,'b-')


subplot(2,1,2)
plot(t_data,h_data,'ro')
plot(t2,y2,'r--')
xlabel('time')


# In[30]:


figure(figsize=(12,8))
subplot(1,2,1)
plot(t_data,h_data,'o')
plot(t1,y1,'b-')


subplot(1,2,2)
plot(t_data,h_data,'ro')
plot(t2,y2,'r--')
xlabel('time')


# In[38]:


for i in range(6):
    subplot(2,3,i+1)
    plot(rand(400)+5*rand())
    
    xlim([0,400])
    ylim([0,10])
    
    if i in [0,1,2]:
        gca().set_xticklabels([])
    else:
        xlabel("Time")
        
    if i in [1,2,4,5]:
        gca().set_yticklabels([])
    else:
        ylabel('Magnitude')


# In[ ]:




