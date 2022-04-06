#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


from lmfit import *


# See: https://lmfit.github.io/lmfit-py/builtin_models.html  for more examples

# ## HIV
# 

# In[5]:


data=pd.read_csv("data/HIVseries.csv",header=None)
data


# In[6]:


x=data[0]
y=data[1]


# In[7]:


plot(x,y,'o')


# ## Step 1 - define the function

# In[9]:


def double_exponential(t,A=1,α=1,B=1,β=1):
    return A*exp(-α*t)+ B*exp(-β*t)


# ## Step 1a - parameter exploration

# In[24]:


tt=linspace(0,7,100)
VV=double_exponential(tt,A=120000,α=1,B=60000,β=.1)

plot(x,y,'o')
plot(tt,VV,'-')


# ## Step 2 - define the model and construct the parameter list

# In[25]:


mymodel=Model(double_exponential)   # from lmfit


# In[26]:


mymodel.param_names


# In[27]:


params=mymodel.make_params()
params


# ## Step 3 - modify the parameter list (min, max, etc...) as needed

# In[33]:


params['A']=Parameter("A",min=1000,value=120000)
params['B']=Parameter("B",min=1000,value=60000)
params['α']=Parameter("α",min=0,value=1)
params['β']=Parameter("β",min=0,value=1)
params


# ## Step 4 - do the fit, look at the parameter values (do they make sense?), etc...

# In[34]:


result = mymodel.fit(y, params, t=x)
result


# ## Step 5 - plot your data and the predictions of the model

# In[35]:


plot(x,y,'o')

tt=linspace(0,7,100)
VV=result.eval(t=tt)

plot(tt,VV,'-')

