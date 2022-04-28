#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


from lmfit import *


# In[4]:


data=pd.read_csv('Dose-Response Data (1).csv')
data


# In[5]:


t_data=data["Dose [mg]"]
y_data=data["Percent Pain Free"]
plot(t_data,y_data,'o')


# In[6]:


t_data,y_data


# In[7]:


def dose(D,Eo,Em,ED):
    
    return Eo+((D*Em)/(D+ED))


# In[8]:


x=linspace(0,200,20)
y=dose(x,5,25,10)
plot(x,y)


# In[9]:


qmodel=Model(dose)   


# In[10]:


qmodel.param_names


# In[11]:


params=qmodel.make_params()
params


# In[12]:


params['Eo']=Parameter("Eo",min=3,max=6,value=5)
params['Em']=Parameter("Em",min=0,max=30,value=25)
params['ED']=Parameter("ED",min=6,max=60,value=10)


# In[13]:


result = qmodel.fit(y_data, params, D=t_data,method="powell")


# In[27]:


def constant(x,a):
    return a*ones(x.shape)


# In[28]:


qmodel=Model(constant)   


# In[29]:


params=qmodel.make_params()
params


# In[30]:


params['a']=Parameter("a",min=0,value=5)


# In[31]:


result = qmodel.fit(y_data, params, x=t_data,method="powell")


# In[32]:


result


# In[33]:


x=linspace(0,200,20)
y=constant(x,5)
plot(x,y)


# In[ ]:




