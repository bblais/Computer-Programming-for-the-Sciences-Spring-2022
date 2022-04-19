#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:a5b02c33-ffc2-4e31-a9f5-193c3eba79cc.png)

# https://youtu.be/Qqz5AJjyugM

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[4]:


island=9
p=arange(1,11)
counts=zeros(len(p))
p,p[island]

path=[island]
counts[island]+=1


# In[5]:


r=rand()<0.5  # flip a coin
if r:
    new_island=island-1
else:
    new_island=island+1

new_island=new_island%10  # wrap around

p_accept=p[new_island]/p[island]
r=rand()
if r<p_accept:
    island=new_island
    
counts[island]+=1
path.append(island)


subplot(1,2,1)
plot(path,'-o')
subplot(1,2,2)
bar(arange(len(p)),counts)


# In[6]:


figure(figsize=(20,8))
plot(rand(100))


# In[7]:


from IPython.display import display, clear_output


# In[8]:


f=figure(figsize=(20,8))

for i in range(100):
    
    r=rand()<0.5  # flip a coin
    if r:
        new_island=island-1
    else:
        new_island=island+1

    new_island=new_island%10  # wrap around

    p_accept=p[new_island]/p[island]
    r=rand()
    if r<p_accept:
        island=new_island

    counts[island]+=1
    path.append(island)


    clear_output(wait=True)
    f.clf()
    subplot(1,2,1)
    plot(path,'-o')
    subplot(1,2,2)
    bar(arange(len(p)),counts)
    display(f)


# In[9]:


f=figure(figsize=(20,8))

for i in range(10000):
    
    r=rand()<0.5  # flip a coin
    if r:
        new_island=island-1
    else:
        new_island=island+1

    new_island=new_island%10  # wrap around

    p_accept=p[new_island]/p[island]
    r=rand()
    if r<p_accept:
        island=new_island

    counts[island]+=1
    path.append(island)

    if i % 100 ==0:
        clear_output(wait=True)
        f.clf()
        subplot(1,2,1)
        plot(path,'-o')
        subplot(1,2,2)
        bar(arange(len(p)),counts)
        display(f)


# ## Does it work with another shape, and more islands?

# In[10]:


N=100
island=9
x=arange(N)
μ=30
σ=5
p=1/sqrt(2*pi*σ**2)*exp(-(x-μ)**2/2/σ**2)
counts=zeros(len(p))
path=[island]
counts[island]+=1


# In[11]:


plot(p,'-o')


# In[12]:


f=figure(figsize=(20,8))

for i in range(10000):
    
    r=rand()<0.5  # flip a coin
    if r:
        new_island=island-1
    else:
        new_island=island+1

    new_island=new_island%len(p)  # wrap around

    p_accept=p[new_island]/p[island]
    r=rand()
    if r<p_accept:
        island=new_island

    counts[island]+=1
    path.append(island)

    if i % 100 ==0:
        clear_output(wait=True)
        f.clf()
        subplot(1,2,1)
        plot(path,'-o')
        subplot(1,2,2)
        bar(arange(len(p)),counts)
        display(f)


# In[ ]:




