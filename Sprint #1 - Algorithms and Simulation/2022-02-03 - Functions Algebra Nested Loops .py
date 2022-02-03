#!/usr/bin/env python
# coding: utf-8

# Fake trig identity
# 
# $$
# 3\sin x +2\cos^2 x=5
# $$

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


3sinx


# In[3]:


3sin(x)


# In[4]:


3*sin(x)


# In[5]:


x=2.0


# In[6]:


3*sin(x)


# In[7]:


2*cos**(x)


# In[8]:


2*cos(x)**2


# In[9]:


3*sin(x)+2*cos(x)**2


# Fake trig identity
# 
# $$
# 3\sin x - 2\cos^2 x=-2
# $$

# In[10]:


x=0.0


# In[11]:


3*sin(x)-2*cos(x)**2


# In[12]:


x=1.0


# In[13]:


3*sin(x)-2*cos(x)**2


# In[14]:


for x in range(100):
    print(x,3*sin(x)-2*cos(x)**2)


# In[15]:


def trig_identity1_print(x):
    value=3*sin(x)-2*cos(x)**2
    print(value)
    
    
def trig_identity1_return(x):
    value=3*sin(x)-2*cos(x)**2
    return value


# In[16]:


trig_identity1_print(1.0)


# In[17]:


trig_identity1_return(1.0)


# In[19]:


value=trig_identity1_return(1.0)
if value>0.0:
    print("bad")


# In[20]:


value=trig_identity1_print(1.0)
if value>0.0:
    print("bad")


# In[22]:


value=trig_identity1_return(1.0)
print(value)


# In[25]:


value=0
N=10
for i in range(1,N+1):
    value=value+i
    
print(value)


# In[28]:


def mysum(N):
    value=0
    for i in range(1,N+1):
        value=value+i

    return value


# In[29]:


mysum(10)


# In[30]:


mysum(10)*2


# In[ ]:




