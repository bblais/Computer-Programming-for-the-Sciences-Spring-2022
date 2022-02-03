#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[12]:


t=linspace(0,10,100)
a=-2
c=100
b=0
yp=a*t**2+b*t+c
plot(t,yp)
ylabel(r'$\frac{dy}{dt}$')
xlabel('$t$')


# In[13]:


y0=10  # initial
y_solution=a*t**3/3+b*t**2/2+c*t+y0
t_solution=linspace(0,10,100)
plot(t_solution,y_solution)


# In[32]:



dt=.5

t=0
y=y0

while t<10:

    dy=(a*t**2+b*t+c)*dt
    
    plot([t,t+dt,t+dt],[y,y,y+dy],'k-')
    plot([t],[y],'ko')
    
    text(t+dt+.1,y,f'{(a*t**2+b*t+c):.3f}$\cdot$ {dt}',fontsize=10)
    y=y+dy
    t=t+dt
    
plot(t_solution,y_solution,'g-',lw=3)
    
    


# In[ ]:




