#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from PIL import Image
import requests


# In[24]:


fifa_df=pd.read_csv("FIFA21.csv")
fifa_df


# ## function to read URL from the dataset and show the picture

# In[25]:


from urllib.request import Request, urlopen

def get_photo(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    image = Image.open(urlopen(request))
    image.show()
    


# In[26]:


get_photo(fifa_df['Photo'][5])


# In[ ]:




