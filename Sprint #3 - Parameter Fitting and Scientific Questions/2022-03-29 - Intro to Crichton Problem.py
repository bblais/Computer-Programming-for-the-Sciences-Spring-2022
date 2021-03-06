#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


from lmfit import *


# In[4]:


data=pd.read_csv('data/station.csv')


# In[5]:


data


# In[24]:


x=data['YEAR']
y=data['metANN']

x=x[y<200]
y=y[y<200]


plot(x,y,'-o')


# In[25]:


mymodel=models.LinearModel()
mymodel.param_names


# In[26]:


params=mymodel.make_params()


# In[27]:


result = mymodel.fit(y, params, x=x)


# In[28]:


result


# In[29]:


slope=result.params['slope'].value
slope


# In[30]:


plot(x,y,'-o')

x_fake=linspace(1990,2022,100)
y_fake=result.eval(x=x_fake)
plot(x_fake,y_fake,'-')
title(f'Slope={slope}')


# In[31]:


plot(x,y,'-o')

x_fake=linspace(min(x),max(x),100)
y_fake=result.eval(x=x_fake)
plot(x_fake,y_fake,'-')
title(f'Slope={slope}')


# In[32]:


data=pd.read_csv('data/crichton/time series data pandas.csv.zip')


# In[33]:


data.head()


# In[34]:


data.to_excel('blah.xlsx')


# In[ ]:




