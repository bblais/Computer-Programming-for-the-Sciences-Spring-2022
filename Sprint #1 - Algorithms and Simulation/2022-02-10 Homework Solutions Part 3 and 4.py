#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# ![image.png](attachment:2310d1cf-8d8a-4008-8493-355d0fe46ea6.png)

# In[48]:


x=.3


# In[6]:


def factorial(N):
    value=1
    for i in range(1,N+1):
        value=value*i
        
    return value
    
    
def mysin(x,order):
    
    if order==1:
        value=x
        
    elif order==3:
        value = x - x**3/factorial(3)
        
    elif order==5:
        value = x - x**3/factorial(3) + x**5/factorial(5)
    
    return value


# In[5]:


factorial(5)


# In[9]:


mysin(x,5),sin(x)


# In[10]:


mysin(x,3),sin(x)


# In[16]:


def mysin(x,order):
    
    term=1
    sign=1
    
    value=0
    
    while term<=order:
        print(term,sign)

        value=value+ sign*x**term/factorial(term)
    
        term=term+2
        sign=sign*-1
        
    
    return value


# In[21]:


mysin(x,3),sin(x)


# In[ ]:





# In[51]:


def mysin3(x,max_n):
    value=0

    for n in range(max_n+1):
        value=value+(-1)**n/factorial(2*n+1)*x**(2*n+1)
        
    return value
        
    
    


# In[52]:


mysin3(x,4),sin(x)


# In[47]:





# In[ ]:





# In[ ]:





# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10001st prime number?

# In[53]:


def isprime(x):
    
    for n in range(2,x):
        if x%n==0:
            return False
        
    return True


# In[54]:


isprime(5)


# In[55]:


isprime(10)


# In[56]:


isprime(2)


# In[57]:


isprime(11)


# In[58]:


for x in range(2,20):
    if isprime(x):
        print(x)


# In[59]:


count=0
for x in range(2,20):
    if isprime(x):
        count=count+1
        print(count,x)


# In[69]:


get_ipython().run_cell_magic('time', '', 'count=0\nfor x in range(2,200000):\n    if isprime(x):\n        count=count+1\n        if count==10001:\n            print(x)\n            break')


# In[ ]:





# In[77]:


def isprime2(x):
    
    if x==2:
        return True
    
    max_n=int(x/2+1)+1

    for n in range(2,max_n):
        if x%n==0:
            return False
        
    return True


# In[79]:


get_ipython().run_cell_magic('time', '', 'count=0\nfor x in range(2,200000):\n    if isprime2(x):\n        count=count+1\n        if count==10001:\n            print(x)\n            break')


# In[78]:


isprime2(2)


# In[81]:


def isprime3(x,current_primes=[]):
    
    for n in current_primes:
        if x%n==0:
            return False
        
    return True        
        


# In[82]:


get_ipython().run_cell_magic('time', '', 'count=0\ncurrent_primes=[]\nfor x in range(2,200000):\n    if isprime3(x,current_primes):\n        current_primes.append(x)\n        count=count+1\n        if count==10001:\n            print(x)\n            break')


# In[ ]:




