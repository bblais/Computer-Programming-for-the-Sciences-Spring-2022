#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[9]:


from lmfit import *


# In[11]:


from glob import glob
from tqdm import tqdm


# In[7]:


filenames=glob('../Sprint #3 - Parameter Fitting and Scientific Questions/data/logistic_sample_data/logistic_sample_data_*.csv')
filenames[:10]


# In[12]:


def f(x,a=1,b=1,c=1,d=1):
    return a/(1+exp(-c*(x-d)))+b


# In[29]:


S=Storage()
for filename in filenames:
    data=pd.read_csv(filename)
    t=data['t']
    y=data['y']
    mymodel=Model(f)   # from lmfit
    params=mymodel.make_params()
    params['a']=Parameter("a",min=0,max=1000,value=1)
    params['b']=Parameter("b",min=0,max=1000,value=1)
    params['c']=Parameter("c",min=0,max=5,value=1)
    params['d']=Parameter("d",min=0,max=10,value=1)

    result = mymodel.fit(y, params, x=t)
    
    S+=result.params['a'].value,result.params['a'].stderr,result.params['c'].value,result.params['c'].stderr
    


# In[30]:


a,σa,c,σc=S.arrays()


# In[31]:


c


# In[32]:


σc


# In[35]:


plot(a,c,'o')


# In[38]:


errorbar(x=a,y=c,xerr=σa,yerr=σc,fmt='o',elinewidth=1)


# In[39]:


errorbar(x=a,y=c,yerr=σc,xerr=σa,fmt='o',elinewidth=1)
ylim([-20,20])


# In[48]:


x=rand(10)
y=rand(10)

xerr=.2*rand(10)
yerr=.01*rand(10)

errorbar(x,y,xerr=xerr,yerr=3*yerr,fmt='o',elinewidth=1)
text(0,.9,"y errorbars are 3σ")


# In[ ]:




