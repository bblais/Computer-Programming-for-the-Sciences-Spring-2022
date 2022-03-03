#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_full_word_list():
    import random
    with open("wordlist_guesses.txt") as fid:
        lines=fid.readlines()
    five_letter_words=[_.strip() for _ in lines]    

    with open("count_1w.txt") as fid:
        lines=fid.readlines()

    popwords,counts=zip(*[_.split() for _ in lines if len(_.split()[0])==5])    

    subset=[]
    for word in popwords:
        if word in five_letter_words:
            subset.append(word)

    return subset


# In[2]:


words=get_full_word_list()


# In[3]:


import random


# In[5]:


word1=random.choice(words)
word2=random.choice(words)

word1,word2


# In[14]:


def difference(word1,word2):
    L=['-']*5
    word1=list(word1)
    word2=list(word2)    
    positions=list(range(5))
    for idx in positions.copy():
        if word1[idx]==word2[idx]:
            L[idx]='g'
            positions.remove(idx)
            word1[idx]="."
            word2[idx]="."

            
    for idx in positions:
        try: 
            idx2=word2.index(word1[idx])
            L[idx]='y'
            word1[idx]="."
            word2[idx2]="."
        except ValueError:
            continue
            
    
    return ''.join(L)
    
    


# In[15]:


difference('slime','smart')


# In[20]:


word1=random.choice(words)
word2=random.choice(words)

word1,word2,difference(word1,word2)


# In[22]:


'g----'.count('y')


# In[24]:


from tqdm import tqdm


# In[36]:


gy_count={}
for word1 in tqdm(words):
    gy_count[word1]=0
    
    
    for word2 in words:
        S=difference(word1,word2)
        gy_count[word1]+=S.count('y')+S.count('g')
        


# In[37]:


new_gy_count=[(k,v) for k, v in sorted(gy_count.items(), key=lambda item: item[1],reverse=True)]


# In[39]:


[_[0] for _ in new_gy_count].index("steam")


# In[43]:


first_words=[_[0] for _ in new_gy_count[:100]]
print(first_words)


# In[ ]:





# In[ ]:





# In[ ]:


five_letter_words=[_.strip() for _ in lines]    

with open("count_1w.txt") as fid:
    lines=fid.readlines()

popwords,counts=zip(*[_.split() for _ in lines if len(_.split()[0])==5])    

subset=[]
for word in popwords:
    if word in five_letter_words:
        subset.append(word)

if verbose:
    print("done.")



# In[1]:


import random


# In[2]:


with open("wordlist_guesses.txt") as fid:
    lines=fid.readlines()


# In[7]:


wordle_words=set([_.strip() for _ in lines if _])
len(wordle_words)


# In[8]:


with open("count_1w.txt") as fid:
    lines=fid.readlines()


# In[9]:


popwords,counts=zip(*[_.split() for _ in lines if len(_.split()[0])==5])    


# In[10]:


popwords[:10]


# In[11]:


popwords=set(popwords)


# In[13]:


len(wordle_words-popwords)


# In[15]:


len(popwords-wordle_words)


# In[16]:


diff=wordle_words-popwords


# In[20]:


print(list(diff)[:100])


# In[21]:


'quags' in wordle_words


# In[22]:


with open("/Users/bblais/Downloads/1_1_all_fullalpha.txt") as fid:
    lines=fid.readlines()


# In[26]:


lines[100000:100000+10]


# In[ ]:




