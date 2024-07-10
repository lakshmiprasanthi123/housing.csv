#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
hus = pd.read_csv("housing.csv")


# In[17]:


hus.head()


# In[18]:


hus.tail()


# In[19]:


hus.info()


# In[20]:


hus["ocean_proximity"].value_counts() 


# In[23]:


hus.describe() #numeric


# In[39]:


import matplotlib. pyplot as plt
hus.hist(bins=50,figsize=(20,15))
plt.show()


# In[ ]:


import numpy as np


# In[ ]:




