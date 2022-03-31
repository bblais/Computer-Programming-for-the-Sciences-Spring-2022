#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *
from lmfit import *


# In[3]:


data=pd.read_csv('data/peaks/sample0.csv')


# In[4]:


data.head()


# In[8]:


t=data['t']
y=data['y']


# In[9]:


plot(t,y,'o')


# In[10]:


model=models.GaussianModel()
model.param_names


# In[11]:


results=model.fit(y,x=t,amplitude=1e7,center=1,sigma=1)
results


# In[15]:


x_fake=linspace(0,2,2000)
y_fake=results.eval(x=x_fake)
plot(t,y,'o')
plot(x_fake,y_fake,'-')
xlim([.9,1.3])

A=results.best_values['amplitude']
c=results.best_values['center']
σ=results.best_values['sigma']
text(.91,1.2e7,f"A={A}\nc={c}\nσ={σ}")


# In[13]:


results.best_values


# ## You can get individual parameters by name

# In[14]:


A=results.params['amplitude'].value
A


# ## Now your turn - Goal: find the amplitudes for all of the peaks for the data in the peaks folder

# In[ ]:




