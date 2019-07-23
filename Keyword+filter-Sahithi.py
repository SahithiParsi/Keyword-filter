
# coding: utf-8

# In[53]:

import os
os.chdir("C:/Users/sahithi/Desktop/sorcero")
os.listdir("C:/Users/sahithi/Desktop/sorcero")


# In[54]:

f = open('text.txt','r')


# In[55]:

lines = f.readlines()


# In[56]:

print(lines[0:3])


# In[58]:

import re
lines = [re.sub('\n','',line) for line in lines]


# In[59]:

from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
   
ps = PorterStemmer()
print(ps.stem('armors'))


# In[60]:

import re
def pattern_filter(string):
    X = [line for line in lines if re.search(ps.stem(string), line, flags=re.IGNORECASE)]
    return X


# In[61]:

pattern_filter('armors')


# In[62]:

pattern_filter('ultron')


# In[63]:

pattern_filter('ultron offensive')

