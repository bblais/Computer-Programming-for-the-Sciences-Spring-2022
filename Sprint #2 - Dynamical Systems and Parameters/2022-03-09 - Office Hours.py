#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


data=pd.read_csv('covid_japan.csv')


# In[4]:


data.head(10)


# In[ ]:





# In[7]:


t=date_to_float(data['Date'])
c=data['Confirmed']


# In[10]:





# In[14]:


N=700
plot(t[:N],c[:N])

t,c=t[:N],c[:N]


# In[16]:


plot(t,c,'o-')


# In[17]:


diff([1,2,4,5,8,9,10])


# In[18]:


t_data=t[1:]
I_data=diff(c)
plot(t_data,I_data,'o-')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# $$
# n'= rn(1-n/k) - hn/(a+n)
# $$

# $$
# n'= n \cdot (r(1-n/k) -h/(a+n))
# $$

# $$
# r(1-n/k) -h/(a+n)=0
# $$
# 
# $$
# r(1-n/k)=h/(a+n)
# $$
# 

# In[ ]:




