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


# In[17]:


x=data[data['Tree']==1]['age']
y=data[data['Tree']==1]['circumference']

plot(x,y,'o',label="Bob")

x=data[data['Tree']==2]['age']
y=data[data['Tree']==2]['circumference']

plot(x,y,'s',label="Sally")

legend()


# In[18]:


x=data[data['Tree']==1]['age']
y=data[data['Tree']==1]['circumference']

plot(x,y,'o',label="Bob")

x=data[data['Tree']==2]['age']
y=data[data['Tree']==2]['circumference']

plot(x,y,'s',label="Sally")

legend(loc='upper right')


# In[19]:


get_ipython().run_line_magic('pinfo', 'legend')


# In[21]:


k=5
g=3

x=data[data['Tree']==1]['age']
y=data[data['Tree']==1]['circumference']

plot(x,y,'o',label=f"Bob k={k},g={g}")


k=2
g=9

x=data[data['Tree']==2]['age']
y=data[data['Tree']==2]['circumference']

plot(x,y,'s',label=f"Sally k={k},g={g}")

legend(loc='upper right')


# In[ ]:




