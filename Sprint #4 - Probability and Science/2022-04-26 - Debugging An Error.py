#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('pylab', 'inline')


# In[6]:


from sci378 import *


# In[7]:


from lmfit import *


# In[8]:


data=pd.read_csv('Dose-Response Data (1).csv')
data


# In[9]:


t=data["Dose [mg]"]
y=data["Percent Pain Free"]
plot(t,y,'o')


# In[10]:


def dose(D,Eo,Em,ED):
    
    return Eo+((D*Em)/(D+ED))


# In[11]:


x=linspace(0,200,20)
y=dose(x,5,25,10)
plot(x,y)


# In[12]:


qmodel=Model(dose)   


# In[13]:


qmodel.param_names


# In[14]:


params=qmodel.make_params()
params


# In[15]:


params['Eo']=Parameter("Eo",min=3,max=6,value=5)
params['Em']=Parameter("Em",min=0,max=30,value=25)
params['ED']=Parameter("ED",min=6,max=60,value=10)


# In[17]:


result = qmodel.fit(y, params, D=x,method="powell")


# In[ ]:




