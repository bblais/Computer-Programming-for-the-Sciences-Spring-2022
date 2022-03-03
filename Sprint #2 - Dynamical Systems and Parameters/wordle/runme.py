#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("https://www.powerlanguage.co.uk/wordle/")


# In[2]:


def get_full_word_list(verbose=True):
    import random
    
    if verbose:
        print("Reading word list...",end="")
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

    if verbose:
        print("done.")
            
    return subset


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
    
    

def first_guess(words,verbose=True):
    
    import random
    
    # top 100 from 2022-01-17 - Find optimum first word
    first_words=['arose', 'aeros', 'raise', 'arise', 'reais', 'serai', 'aesir', 'rates', 'tears', 'stare', 
                 'aster', 'taser', 'tares', 'stear', 'teras', 'reast', 'laser', 'reals', 'earls', 'arles', 
                 'lares', 'seral', 'rales', 'lears', 'aloes', 'earns', 'snare', 'nears', 'saner', 'nares', 
                 'aeons', 'aisle', 'anise', 'saine', 'least', 'tales', 'steal', 'slate', 'tesla', 'stale', 'stela', 
                 'reads', 'dares', 'dears', 'arsed', 'eards', 'ursae', 'osier', 'acres', 'races', 'cares', 'scare', 
                 'carse', 'serac', 'acers', 'antes', 'nates', 'stane', 'lanes', 'leans', 'slane', 'neals', 'smear', 
                 'mares', 'reams', 'maser', 'marse', 'spare', 'parse', 'spear', 'pears',  'apres', 'reaps', 
                 'pares', 'presa', 'asper', 'apers', 'years', 'ayres', 'sayer', 'ideas', 'aside', 'aides', 'store', 
                 'resto', 'estro', 'rotes', 'roset', 'share', 'shear', 'hears', 'hares', 'roles', 'loser', 'sorel', 
                 'soler', 'lores', 'paseo', 'bears', ]
        
    return random.choice(first_words[:10])

def double_letters(word):
    if len(set(word))==len(word):
        return False
    else:
        return True

def guess(words,knowledge,previous_guesses,verbose=True):
    import random
    from tqdm import tqdm
    if not knowledge:
        assert not previous_guesses
        return first_guess(words,verbose=verbose),False
        
    if verbose:
        print(len(words))
    for know in knowledge:
        if len(know)==3:
            letter,notty,idx=know
            idx=int(idx)

            if notty=='!':
                words=[_ for _ in words if letter in _ and _[idx]!=letter]
            elif notty=='=':
                words=[_ for _ in words if letter in _ and _[idx]==letter]
        elif len(know)==2:
            assert know[0]=='!'
            letter=know[1]

            words=[_ for _ in words if letter not in _]


        if verbose:
            print(len(words))

            
    if len(words)==1:
        return words[0],True
    else:

        gy_count={}
        for word1 in tqdm(words):
            gy_count[word1]=0
            for word2 in words:
                S=difference(word1,word2)
                gy_count[word1]+=S.count('y')+S.count('g')
                    
        new_gy_count=[(k,v) for k, v in sorted(gy_count.items(), key=lambda item: item[1],reverse=True)]                    

        if len(words)<30:
            print(words)

            # # no overlapping letters (not hard mode)
            # previous_guess=previous_guesses[0]
            # words=[_[0] for _ in new_gy_count if difference(previous_guess,_[0])=='-----']
            
            
        if len(previous_guesses)==1:  # second guess - no double letters
            words=[_[0] for _ in new_gy_count if not double_letters(_[0])][:10] 
        else:            
            words=[_[0] for _ in new_gy_count][:10]              
        
        if len(words)<5:
            words=[words[0]]  # take the most popular one



        return random.choice(words),False
            


# In[3]:


def get_feedback():
    while True:
    
        fb=input('XXXXX [- y g]:')

        if not fb:
            break

        if len(fb)!=5:
            print("  wrong length %d" % len(fb))
            continue
        if (set(fb)-set('-yg')):
            print("  wrong symbol in ",fb)
            continue
            
        break
    return fb


# In[ ]:





# In[4]:


def update_knowledge(knowledge,guess,feedback):
    
    g=guess
    fb=feedback
    
    for i in range(5):
        if fb[i]=='-':
            knowledge+=["!"+g[i]]
        elif fb[i]=='y':
            knowledge+=[g[i]+"!"+"%d" % i]
        elif fb[i]=='g':
            knowledge+=[g[i]+"="+"%d" %i]
        else:
            raise ValueError("You can't get there from here.")
        
        
        
    # not sure how double letters will be handled
    # filter for duplicates
    new_knowledge=[]
    fixed_letters=[k[0] for k in knowledge if len(k)==3]
    for know in knowledge:
        if len(know)==3:
            new_knowledge.append(know)
        elif len(know)==2:
            letter=know[1]
            if letter not in fixed_letters:
                new_knowledge.append(know)
                
    knowledge=new_knowledge
    
    
    return knowledge
    
        


# In[5]:


knowledge=[]
words=get_full_word_list()
guesses=[]
while True:
    
    g,stop=guess(words,knowledge,guesses)
    print(g)
    
    if stop:
        break
    fb=get_feedback()
    if fb:
        knowledge=update_knowledge(knowledge,g,fb)

print("Done.")


# In[ ]:





# In[ ]:




