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


# In[11]:


data=pd.read_csv('data/Orange.csv')


# In[12]:


data


# In[15]:


x=data[data['Tree']==1]['age']
y=data[data['Tree']==1]['circumference']

plot(x,y,'o')

x=data[data['Tree']==2]['age']
y=data[data['Tree']==2]['circumference']

plot(x,y,'s')


# In[ ]:




