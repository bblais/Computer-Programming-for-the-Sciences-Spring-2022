#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# ## The math
# 
# Google search Markdown syntax,  Latex syntax (for equations)
# https://www.markdownguide.org/basic-syntax
# 
# https://victoromondi1997.github.io/blog/latex/markdown/2020/07/03/Markdown-LaTeX.html#LaTeX
# 
# 
# $$
# \frac{dx}{dt}=v
# $$
# 
# $$
# \frac{dv}{dt}=a
# $$
# 
# $$
# a=-10
# $$
# 

# In[6]:


# initial values of variables
x=0
v=8

# parameters
a=-10

# initial time
t=0
dt=0.1

S=Storage()

S+=t,x,v
while t<20:
    dx=v*dt
    dv=a*dt
    
    x=x+dx
    v=v+dv
    t=t+dt
    
    S+=t,x,v
    
t,x,v=S.arrays()
    
    


# In[9]:


plot(t,x)
xlabel('time')
ylabel('x-position')


# In[10]:


plot(t,v)
xlabel('time')
ylabel('speed')


# In[13]:


# initial values of variables
x=0
v=8

# parameters
a=-10

# initial time
t=0
dt=0.1

S=Storage()

S+=t,x,v
while t<20:
    dx=v*dt
    dv=a*dt
    
    x=x+dx
    v=v+dv
    t=t+dt
    
    S+=t,x,v
    
t,x,v=S.arrays()
    
    
plot(t,x)
xlabel('time')
ylabel('x-position')    


#==============================================

# initial values of variables
x=0
v=8

# parameters
a=-5

# initial time
t=0
dt=0.1

S=Storage()

S+=t,x,v
while t<20:
    dx=v*dt
    dv=a*dt
    
    x=x+dx
    v=v+dv
    t=t+dt
    
    S+=t,x,v
    
t,x,v=S.arrays()
    
    
plot(t,x)
xlabel('time')
ylabel('x-position')    


#==============================================

# initial values of variables
x=0
v=8

# parameters
a=2

# initial time
t=0
dt=0.1

S=Storage()

S+=t,x,v
while t<20:
    dx=v*dt
    dv=a*dt
    
    x=x+dx
    v=v+dv
    t=t+dt
    
    S+=t,x,v
    
t,x,v=S.arrays()
    
    
plot(t,x)
xlabel('time')
ylabel('x-position')    




# ## Usng a loop for exploration

# In[21]:


for a in [-10,-5,0,2]:
    # initial values of variables
    x=0
    v=8

    # parameters
    #a=2   #<------ since I'm looping this parameter, don't set it

    # initial time
    t=0
    dt=0.01

    S=Storage()

    S+=t,x,v
    
    #for i in range(200):
    while t<20:
        dx=v*dt
        dv=a*dt

        x=x+dx
        v=v+dv
        t=t+dt

        S+=t,x,v

    t,x,v=S.arrays()


    plot(t,x,label=f"a = {a}")
    xlabel('time')
    ylabel('x-position')    

legend()


# In[22]:


for a in [-10,-5,0,2]:
    # initial values of variables
    x=0
    v=8

    # parameters
    #a=2   #<------ since I'm looping this parameter, don't set it

    # initial time
    t=0
    dt=0.01

    S=Storage()

    S+=t,x,v
    
    #for i in range(200):
    while t<20:
        dx=v*dt
        dv=a*dt

        x=x+dx
        v=v+dv
        t=t+dt

        S+=t,x,v

    t,x,v=S.arrays()

    plot(t,v,label=f"a = {a}")
    xlabel('time')
    ylabel('speed')


legend()


# Watch out for closing parentheses -- the error may occur on the wrong line.

# In[23]:


x=(5+(2+8)*6
   
   
   
y=5


# In[ ]:




