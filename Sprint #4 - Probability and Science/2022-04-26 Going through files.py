#!/usr/bin/env python
# coding: utf-8

# In[1]:


from glob import glob


# In[2]:


ls data/1999aa/


# In[3]:


ls data/1999ac/


# In[6]:


filenames=glob('data/1999aa/*v_*.dat')+glob('data/1999ac/*v_*.dat')
filenames


# In[7]:


filenames=glob('data/*/*v_*.dat')
filenames


# In[ ]:




