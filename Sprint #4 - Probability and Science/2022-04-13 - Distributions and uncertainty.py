#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


from scipy.stats import distributions as D


# In[11]:


dist=D.norm
#dist=D.cauchy


# In[12]:


x=linspace(0,10,100)
y=dist.pdf(x,loc=5,scale=1)
plot(x,y)


# In[ ]:





# In[13]:


sample=dist.rvs(loc=5,scale=1,size=50)


# In[14]:


sample


# In[15]:


sample.mean()


# In[16]:


distribution_of_mean=dist.rvs(loc=5,scale=1/sqrt(len(sample)),size=(50,10000))


# In[17]:


histogram(distribution_of_mean.mean(axis=0));

x=linspace(4.5,5.5,100)
y=dist.pdf(x,loc=5,scale=1/len(sample))
plot(x,y)


# In[ ]:





# In[ ]:




