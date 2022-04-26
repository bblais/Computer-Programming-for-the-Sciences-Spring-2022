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


# In[26]:


t_data=data["Dose [mg]"]
y_data=data["Percent Pain Free"]
plot(t_data,y_data,'o')


# In[27]:


t_data,y_data


# In[28]:


def dose(D,Eo,Em,ED):
    
    return Eo+((D*Em)/(D+ED))


# In[29]:


x=linspace(0,200,20)
y=dose(x,5,25,10)
plot(x,y)


# In[30]:


qmodel=Model(dose)   


# In[31]:


qmodel.param_names


# In[32]:


params=qmodel.make_params()
params


# In[33]:


params['Eo']=Parameter("Eo",min=3,max=6,value=5)
params['Em']=Parameter("Em",min=0,max=30,value=25)
params['ED']=Parameter("ED",min=6,max=60,value=10)


# In[34]:


result = qmodel.fit(y_data, params, D=t_data,method="powell")


# In[16]:


t


# In[17]:


y


# In[ ]:





# In[ ]:





# In[12]:


result = qmodel.fit(y, params, D=x,method="powell")


# In[15]:


plot([1,2,3],[4,5,6,7],'o')


# In[ ]:




