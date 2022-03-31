#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


from lmfit import *


# - For each urban station
#     - find slope
#     - whether urban or rural
#     - closest rural
#         - find slope
# 

# In[5]:


data=pd.read_csv('data/crichton/time series data pandas.csv.zip')
data.head()


# In[36]:


# Brightness > 10 = urban
station_data=pd.read_excel('data/crichton/station_info.xlsx')
station_data.head(20)


# In[9]:


len(station_data)


# ## find slope

# In[14]:


name="SAVE"
time=data['time']
temp=data[name]
plot(time,temp,'-o')


# In[13]:


temp


# In[22]:


def get_slope(name,display=False):
    x=data['time']
    y=data[name].dropna()
    x=data['time'][y.index]
    
    mymodel=models.LinearModel()
    params=mymodel.make_params()
    result = mymodel.fit(y, params, x=x)
    slope=result.params['slope'].value    
    if display:
        plot(x,y,'-o')

        xx=linspace(min(x),max(x),100)
        yy=result.eval(x=xx)
        plot(xx,yy,'-')
        title(f'Station={name} Slope={slope}')        
    
    return slope


# In[23]:


get_slope("SAVE",display=True)


# In[24]:


name


# In[28]:


station_data['Brightness'][station_data['Station']==name]>=10


# In[40]:


array((station_data['Brightness'][station_data['Station']==name]>=10))[0]


# In[41]:


def isurban(name):
    if array((station_data['Brightness'][station_data['Station']==name]>=10))[0]:
        return True
    else:
        return False


# In[67]:


def latitude(name=None):
    if name is None:
        return array(station_data['Latitude'])
    else:
        return array(station_data['Latitude'][station_data['Station']==name])[0]
def longitude(name=None):
    if name is None:
        return array(station_data['Longitude'])
    else:
        return array(station_data['Longitude'][station_data['Station']==name])[0]


# In[68]:


latitude("SAVE"),longitude("SAVE")


# In[69]:


latitude()


# In[70]:


d2=(latitude()-latitude("SAVE"))**2+(longitude()-longitude("SAVE"))**2
argmin(d2)


# In[59]:


min_dist=1e500
min_name=None
name="SAVE"
lat=latitude(name)
long=longitude(name)



for index,row in station_data.iterrows():
    if row.Station==name:
        continue
        
    d2=(lat-latitude(row.Station))**2+(long-longitude(row.Station))**2
    if d2<min_dist:
        min_dist=d2
        min_name=row.Station
    



# In[57]:


row.Station


# In[42]:


isurban("SAVE")


# In[43]:


isurban("HERAT")


# In[44]:


station_data['Latitude']


# In[60]:


station_data.T


# In[61]:


S=station_data.T
S.columns=station_data.Station


# In[62]:


S


# In[63]:


S[name]


# In[71]:


station_data['d2']=(latitude()-latitude(name))**2+(longitude()-longitude(name))**2


# In[74]:


station_data.sort_values('d2')


# In[81]:


def closest_rural(name):
    station_data['d2']=(latitude()-latitude(name))**2+(longitude()-longitude(name))**2
    sorted_station_data=station_data.sort_values('d2')
    
    for i,row in sorted_station_data.iterrows():
        if row.Station==name:
            continue
        if not isurban(row.Station):
            return row.Station

    raise ValueError("You can't get there from here.")


# In[82]:


closest_rural("SAVE")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# - For each urban station
#     - find slope
#     - whether urban or rural
#     - closest rural
#         - find slope
# 

# In[83]:


from tqdm import tqdm


# In[97]:


S=Storage()

for i,row in tqdm(station_data.iterrows()): # go through all the stations
    U_name=row.Station
    if not isurban(U_name):  # if it's rural, go to the next station
        continue
        
    # if you are here, you're an urban station
        
    U_slope=get_slope(U_name)
    
    R_name=closest_rural(U_name)
    R_slope=get_slope(R_name)
    
    S+=U_slope,R_slope
    
U_slope,R_slope=S.arrays()


# In[99]:


len(U_slope)


# In[ ]:




