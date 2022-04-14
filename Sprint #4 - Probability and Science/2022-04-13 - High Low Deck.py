#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


data=array([7,9])


# In[4]:


H_likelihood=prod(data/55)
L_likelihood=prod((11-data)/55)
N_likelihood=float(all(data==9))


# In[5]:


N_likelihood


# In[6]:


def normalize(*args):
    return [_/sum(args) for _ in args]


# In[7]:


H_prior=0.5
L_prior=0.5
N_prior=1e-6

# make them add up to 1

#H_prior,L_prior,N_prior=[_/sum([H_prior,L_prior,N_prior]) for _ in [H_prior,L_prior,N_prior]]
H_prior,L_prior,N_prior=normalize(H_prior,L_prior,N_prior)
H_prior,L_prior,N_prior


# In[8]:


H_posterior=H_likelihood*H_prior
L_posterior=L_likelihood*L_prior
N_posterior=N_likelihood*N_prior

H_posterior,L_posterior,N_posterior=normalize(H_posterior,L_posterior,N_posterior)
H_posterior,L_posterior,N_posterior


# In[9]:


S=Storage()
for m in range(0,10):
    
    data=9*ones(m)
    H_likelihood=prod(data/55)
    L_likelihood=prod((11-data)/55)
    N_likelihood=float(all(data==9))    
    
    H_posterior=H_likelihood*H_prior
    L_posterior=L_likelihood*L_prior
    N_posterior=N_likelihood*N_prior

    H_posterior,L_posterior,N_posterior=normalize(H_posterior,L_posterior,N_posterior)    
    
    S+=H_posterior,L_posterior,N_posterior
    
H_posterior,L_posterior,N_posterior=S.arrays()
    
    


# In[10]:


plot(H_posterior,'-o')
plot(L_posterior,'-s')
plot(N_posterior,'-v')


# ## Flip 9 and 3

# data = UUUDUDUUUUUD
# 
# 9 U, 3 D
# 
# So if I flip $N=12$ times then...

# In[11]:


def binomial_likelihood(N,D,p):
    from scipy.special import factorial
    return factorial(N)/factorial(N-D)/factorial(D)*p**(D)*(1-p)**(N-D)


# > “The p-value is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct.” 

# In[12]:


binomial_likelihood(12,3,0.5)+binomial_likelihood(12,2,0.5)+binomial_likelihood(12,1,0.5)+binomial_likelihood(12,0,0.5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# but if I flip until 3 down, then the distribution is the negative binomial

# In[13]:


def negbinomial_likelihood(N,D,p):
    from scipy.special import factorial
    return factorial(N-1)/factorial((N-1)-(D-1))/factorial(D-1)*p**(D)*(1-p)**(N-D)


# In[14]:


negbinomial_likelihood(12,3,0.5)+negbinomial_likelihood(13,3,0.5)+negbinomial_likelihood(14,3,0.5) # + ....


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[15]:


sum([negbinomial_likelihood(_,3,0.5) for _ in range(12,100)])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[24]:


models=θ=p_D=linspace(0,1,101)
θ


# In[17]:


L=binomial_likelihood(12,3,θ)


# In[18]:


plot(θ,L,'-o')
xlabel('$p_D$')


# In[19]:


prior=ones(len(θ))/len(θ)
prior


# In[32]:


L=binomial_likelihood(12,3,θ)
prior=ones(len(θ))/len(θ)
posterior=prior*L
T=sum(posterior)
posterior/=T
plot(θ,posterior,'-o')


# In[33]:


posterior=prior*L
T=sum(posterior)
posterior/=T
plot(θ,posterior,'-o')


# In[34]:


models=θ=p_U=linspace(0,1,1001)
dθ=θ[1]-θ[0]
prior=ones(len(θ))
L=binomial_likelihood(12,3,θ)

posterior=prior*L
T=sum(posterior)*dθ
posterior/=T
plot(θ,posterior,'-')


# In[35]:


sum(posterior*dθ)


# In[36]:


sum(posterior[θ<0.5]*dθ)


# In[ ]:




