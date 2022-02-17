#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[6]:


plot(rand(100),'o')
savefig('/Users/bblais/Downloads/figure1.png',dpi=200)


# In[7]:


plot(rand(100),'o')
savefig('/Users/bblais/Downloads/figure1.pdf')


# In[10]:


figure(figsize=(3,10))
plot(rand(100),'o')


# In[ ]:




