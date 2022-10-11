#!/usr/bin/env python
# coding: utf-8

# # Pandas

# 

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r'C:\Users\RAHUL\Documents\SALARY.csv')


# In[3]:


data


# In[4]:


# checking few records using head()


# In[5]:


data.head()


# In[6]:


data.head(2)


# In[7]:


data.tail() #bottom 5 records


# In[8]:


type(data)


# In[9]:


data1 =  data.head(6)


# In[10]:


data1


# In[11]:


data1.to_csv("data_6.csv") #storing the data


# In[12]:


ls


# In[13]:


pd.read_csv('data_6.csv') # why Unnamed column added 


# In[14]:


pd.read_csv('data_6.csv',sep='.') # changing the default delimiter


# In[15]:


data = pd.read_csv(r'C:\Users\RAHUL\Documents\SALARY.csv' ,header=None,names=['a', 'b', 'c', 'd', 'e', 'f','g'])


# In[16]:


data


# In[17]:


list('abcdefgh')


# In[18]:


data = pd.read_csv(r'C:\Users\RAHUL\Documents\SALARY.csv' ,header=None,names=['a', 'b', 'c', 'd', 'e', 'f','g'],skiprows=[0,2,3])


# In[19]:


data


# In[20]:


data = pd.read_csv(r'C:\Users\RAHUL\Documents\SALARY.csv') #original dataframe


# In[21]:


data


# In[22]:


data = pd.read_csv(r'C:\Users\RAHUL\Documents\SALARY.csv',na_values=['SINGLE'])


# In[23]:


data


# In[24]:


data.describe()


# In[25]:


data.dtypes


# In[26]:


data.to_csv("data_1.csv")


# In[27]:


ls


# In[28]:


data1


# In[38]:


data.to_csv("data_2.csv",index=False,header=False)


# In[39]:


data2  = pd.read_csv(r'C:\Users\RAHUL\Documents\ThreePython\data_2.csv')


# In[40]:


data2


# # row and column selection

# In[41]:


data


# In[42]:


data.columns


# In[46]:


# data['BASIC'] 
data[['BASIC']]


# In[47]:


data[['BASIC','MONTH ']]


# In[ ]:




