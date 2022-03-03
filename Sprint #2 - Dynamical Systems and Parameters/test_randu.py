#!/usr/bin/env python
# coding: utf-8

#     function randu(iseed)
#     parameter (IMAX = 2147483647, XMAX_INV = 1./IMAX)
#     iseed = iseed * 65539
#     if (iseed < 0) iseed = iseed + IMAX + 1
#     randu = iseed * XMAX_INV
#     end

# ![image.png](attachment:0f29011d-a259-442f-8cbe-3ff7ee42cf44.png)

# In[25]:


get_ipython().run_line_magic('pylab', 'inline')
from mpl_toolkits.mplot3d import axes3d


# In[26]:


def randu(*args,seed=None):
    from numpy import prod,array
    if len(args)==0:
        global Ij
        
        if not seed is None:
            Ij=seed
            return
        
        try:
            _ = Ij
        except NameError:
            Ij=101

        m=2**31
        c=0
        a=65539

        Ij=(a*Ij+c) % m


        return Ij/m
    
    else:
        N=prod(args)
        a=array([randu() for _ in range(N)]).reshape(*args)
        return a


# In[35]:


randu(seed=101)


# In[36]:


randu(100)


# In[38]:


im=randu(1000)
plot(im)


# In[37]:


255*255


# In[39]:


im=randu(255,255)
plt.figure(figsize=(10,10))
plt.pcolor(im,cmap=plt.cm.gray)


# In[40]:


im=randu(1000)
plt.plot(im[:-1],im[1:],'.')
plt.axis('equal')


# In[41]:


count=0
fig = plt.figure(figsize=(10,10))
im=randu(10000,3)
ax = fig.add_subplot(projection='3d')
count+=1

x=im[:,0]
y=im[:,1]
z=im[:,2]

ax.scatter(x, y, z,s=2)


# In[42]:


count=0
fig = plt.figure(figsize=(15,15))
im=randu(10000,3)
for angle in [20,25,30,35,40,45,50,55,60]:
    ax = fig.add_subplot(3,3,count+1,projection='3d')
    count+=1

    x=im[:,0]
    y=im[:,1]
    z=im[:,2]

    ax.scatter(x, y, z,s=2)
    ax.view_init(30, angle)


# In[43]:


count=0
fig = plt.figure(figsize=(15,15))
im=rand(10000,3)
for angle in [20,25,30,35,40,45,50,55,60]:
    ax = fig.add_subplot(3,3,count+1,projection='3d')
    count+=1

    x=im[:,0]
    y=im[:,1]
    z=im[:,2]

    ax.scatter(x, y, z,s=2)
    ax.view_init(30, angle)


# In[ ]:




