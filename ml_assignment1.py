#!/usr/bin/env python
# coding: utf-8

# 1.  FAANG stock dataset:
# 
# - Link: https://www.kaggle.com/aayushmishra1512/faang-complete-stock-data
# - Purpose : I can use this dataset to understand the stocks in depth and to find the max highest price of the stocks and raise and downfall of stocks. 
# 
# 
# 2.  Streamers on TWITCH:
# 
# - Link: https://www.kaggle.com/aayushmishra1512/twitchdata
# - Purpose : This data consists of different things like number of viewers, number of active viewers, followers gained and many other relevant columns regarding a particular streamer.
# 
# 3.  IPL dataset:
# 
# - Link: https://www.kaggle.com/saurav9786/indian-premier-league-match-analysis
# - Purpose :  I would use this dataset to predict the winner of the tournament.
# 
# 4.  UBER:
# 
# - Link: https://github.com/fivethirtyeight/uber-tlc-foil-response/blob/master/Uber-Jan-Feb-FOIL.csv
# - Purpose : I will use this to find how many diapatches were made in specific day, and how trpis were taken
# 
# 5.  FIFA 2021:
# 
# - Link: https://www.kaggle.com/aayushmishra1512/fifa-2021-complete-player-data
# - Purpose : I will use this dataset to group the age of player with his potential growth. 
# 

# I choose NETFLIX dataset from FAANG to explore. 

# In[3]:


import pandas as pd
netflix_dataset=pd.read_csv("D:/fall sem/Applied Machine Learning/ML_git/stocks/Netflix.csv")
netflix_dataset


# In[4]:


netflix_dataset.head()


# In[5]:


netflix_dataset.info()


# In[6]:


netflix_dataset.tail()


# In[8]:


netflix_dataset.shape


# In[9]:


netflix_dataset.describe()


# In[ ]:




