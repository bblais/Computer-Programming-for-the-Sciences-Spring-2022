#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('pylab', 'inline')


# In[5]:


from sci378 import *


# In[6]:


from lmfit import *


# ## Peaks fitting

# In[7]:


data=pd.read_csv('data/peaks/sample0.csv')
data


# In[6]:


t=data['t']
y=data['y']


# In[8]:


plot(t,y,'o')


# In[9]:


model=models.GaussianModel()
model.param_names


# In[10]:


results=model.fit(y,x=t,amplitude=1e7,center=1,sigma=1)
results


# In[11]:


xx=linspace(0,2,2000)
yy=results.eval(x=xx)

plot(t,y,'o')
plot(xx,yy,'-')
xlim([.9,1.3])


# In[32]:


def fit_gaussian(filename):
    data=pd.read_csv(filename)
    t=data['t']
    y=data['y']
    
    model=models.GaussianModel()
    results=model.fit(y,x=t,amplitude=1e7,center=1,sigma=1)
    
    return results


# In[33]:


results=fit_gaussian('data/peaks/sample0.csv')
xx=linspace(0,2,2000)
yy=results.eval(x=xx)

plot(t,y,'o')
plot(xx,yy,'-')
xlim([.9,1.3])


# In[1]:


from glob import glob
from tqdm import tqdm


# In[3]:


glob('data/peaks/sample4*.csv')


# In[35]:


filenames=glob('data/peaks/sample*.csv')
S=Storage()
for name in tqdm(filenames):
    results=fit_gaussian(name)
    A=results.params['amplitude'].value
    
    S+=A,
    
A=S.arrays()


# In[39]:


hist(A,30);


# In[40]:


def fit_gaussian_fixed(filename):
    data=pd.read_csv(filename)
    t=data['t']
    y=data['y']
    
    model=models.GaussianModel()
    params=model.make_params()
    params['amplitude']=Parameter("amplitude",min=0,value=1e7)

    
    results=model.fit(y,params,x=t,amplitude=1e7,center=1,sigma=1)
    
    return results


# In[41]:


filenames=glob('data/peaks/sample*.csv')
S=Storage()
for name in tqdm(filenames):
    results=fit_gaussian_fixed(name)
    A=results.params['amplitude'].value
    
    S+=A,
    
A=S.arrays()

hist(A,30);


# ## Logistic function
# 
# ![image.png](attachment:dfc3746b-1c8b-4f02-bc5e-ae75d3afeb61.png)

# In[7]:


data=pd.read_csv('data/logistic_sample_data/logistic_sample_data_0.csv')
data


# In[8]:


t=data['t']
y=data['y']
plot(t,y,'o')


# In[9]:


def f(x,a=1,b=1,c=1,d=1):
    return a/(1+exp(-c*(x-d)))+b


# In[10]:


xx=linspace(0,50,1000)
yy=f(xx,a=600,b=0.5,c=20,d=0.5)

plot(t,y,'o')
plot(xx,yy,'-')


# In[12]:


mymodel=Model(f)   # from lmfit
params=mymodel.make_params()
params['a']=Parameter("a",min=0,max=1000,value=1)
params['b']=Parameter("b",min=0,max=1000,value=1)
params['c']=Parameter("c",min=0,max=5,value=1)
params['d']=Parameter("d",min=-1000,max=1000,value=1)


# In[13]:


result = mymodel.fit(y, params, x=t)


# In[14]:


result


# In[15]:


plot(t,y,'o')

tt=linspace(0,50,300)
yy=result.eval(x=tt)
plot(tt,yy,'-')


# In[25]:


def fit_logistic(filename,display=False):
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
    
    if display:
        plot(t,y,'o')
        tt=linspace(0,50,300)
        yy=result.eval(x=tt)
        plot(tt,yy,'-')     
        
        
    return result


# In[26]:


result=fit_logistic('data/logistic_sample_data/logistic_sample_data_0.csv',display=True)


# In[27]:


filenames=glob('data/logistic_sample_data/log*.csv')
S=Storage()
for name in tqdm(filenames):
    results=fit_logistic(name)
    K=results.params['a'].value+results.params['b'].value
    
    S+=K,
    
K=S.arrays()

hist(K,30);


# In[28]:


for i,name in enumerate(filenames):
    subplot(3,4,i+1)
    results=fit_logistic(name,display=True)


# ## population growth

# In[4]:


data=pd.read_excel('data/Appendix_ World Population Estimate Sets.xlsx')
data.head()


# In[5]:


data=pd.read_excel('data/Appendix_ World Population Estimate Sets.xlsx',skiprows=2)
data.head()


# In[6]:


t=data['Time']
y=data['population']
plot(t,y,'o')


# In[27]:


# make -10000 = t=0
# scale, so that the time is in millenia rather than years
t=(data['Time'].dropna()-(-10000))/1000
y=data['population'].dropna()
plot(t,y,'o')

y=array(y[t>11])
t=array(t[t>11])
t=t-min(t)
plot(t,y,'o')


# In[28]:


y


# ![image.png](attachment:63d291aa-da6c-481b-8686-2325f0285610.png)

# In[37]:


def N(x,k,to,N1,t1):
    values=N1*((to-t1)/(to-x))**k
    return values


mymodel=Model(N)   # from lmfit
params=mymodel.make_params()
params


# In[46]:


params['to']=Parameter("to",min=max(t)+1e-4,max=1000,value=max(t)+50)
params['k']=Parameter("k",min=0,max=200,value=.1)
params['N1']=Parameter("N1",value=y[0],vary=False)
params['t1']=Parameter("t1",value=t[0],vary=False)
params


# In[47]:


result = mymodel.fit(y, params, x=t)


# In[48]:


result


# In[54]:


plot(t,y,'o')
tt=linspace(0,0.91,300)
yy=result.eval(x=tt)
plot(tt,yy,'-')     


# ## Novik-Weiner Data

# In[68]:


data=pd.read_csv('data/g149novickA.txt')
data


# In[65]:


data=pd.read_csv('data/g149novickA.txt',header=None)
data


# In[66]:


t=data[0]
z=data[1]


# In[67]:


plot(t,z,'-o')


# ![image.png](attachment:b587b8b9-416d-42c2-9528-acf67d232e34.png)

# In[71]:


from pyndamics3 import Simulation
from pyndamics3.fit import fit, Parameter


# In[73]:


sim=Simulation()
sim.add("z' = S/τ - z/τ",0,plot=True)
sim.params(S=1,τ=1)
sim.add_data(t=t,z=z,plot=True)
sim.run(7)


# In[74]:


sim=Simulation()
sim.add("z' = S/τ - z/τ",0,plot=False)
sim.params(S=1,τ=1)
sim.add_data(t=t,z=z,plot=False)
sim.run(7)


# In[75]:


results=fit(sim,
           Parameter("S",value=1,min=0),
           Parameter("τ",value=1,min=0),
           )


# In[76]:


results


# In[77]:


sim.run(7)


# In[78]:


plot(t,z,'o')
plot(sim.t,sim.z)


# In[ ]:




