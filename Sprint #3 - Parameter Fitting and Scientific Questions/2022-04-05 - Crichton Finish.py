#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


from lmfit import *


# In[4]:


data=pd.read_csv('data/RU_Crichton.csv')
data.head()


# In[11]:


figure(figsize=(8,8))
x=data['R']
y=data['U']
plot([-.6,.6],[0,0],'k-')
plot([0,0],[-.6,.6],'k-')
plot(x,y,'o',alpha=0.1)
axis('equal')
xlim([-.2,.2])
ylim([-.2,.2])


# definitely a global warming bias, but lots of examples of Crichton to cherry pick.

# ## HIV Data

# In[14]:


data=pd.read_csv('data/HIVseries.csv',header=None)
data.head()


# In[15]:


t_data=data[0]
V_data=data[1]
plot(t_data,V_data,'o-')


# In[22]:


t_data


# In[16]:


def double_exponential(t,A=1,B=1,α=1,β=1):
    return A*exp(-α*t)+B*exp(-β*t)


# In[17]:


mymodel=Model(double_exponential)   # from lmfit


# In[23]:


params=mymodel.make_params()
params['A']=Parameter("A",min=0,value=1)
params['B']=Parameter("B",min=0,value=1)
params['α']=Parameter("α",min=0,value=1)
params['β']=Parameter("β",min=0,value=1)
params


# In[24]:


result = mymodel.fit(V_data, params, t=t_data)
result


# In[25]:



tt=linspace(0,7,100)
VV=result.eval(t=tt)

plot(t_data,V_data,'o-')
plot(tt,VV)


# In[ ]:





# Can't blindly fit -- need to do a parameter search

# In[26]:


tt=linspace(0,7,100)
VV=double_exponential(tt,A=150000,B=1000,α=1,β=1)

plot(t_data,V_data,'o-')
plot(tt,VV)



# In[ ]:





# In[27]:


params['A']=Parameter("A",min=0,value=150000)
params['B']=Parameter("B",min=0,value=1000)
params['α']=Parameter("α",min=0,value=1)
params['β']=Parameter("β",min=0,value=1)
result = mymodel.fit(V_data, params, t=t_data)

tt=linspace(0,7,100)
VV=result.eval(t=tt)

plot(t_data,V_data,'o-')
plot(tt,VV)


# In[28]:


result


# In[ ]:




