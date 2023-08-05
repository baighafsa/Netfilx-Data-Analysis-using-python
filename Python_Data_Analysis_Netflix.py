#!/usr/bin/env python
# coding: utf-8

# # Netflix Data Set
# The data has information about the TV shows and movies available on Netflix til 2021.

# In[2]:


# Import the data set
import pandas as pd

data=pd.read_csv(r'C:\Users\SPECTRE\Desktop\DataAnalysis_DataSets\Netflix.csv.csv')   # r before to remove unicode error


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.tail()


# In[6]:


data.shape


# In[8]:


data.size   #total number of values in dataset


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[11]:


data.info()


# # Duplicate Records in the dataset? If yes, then remove them.

# ### duplicate()

# In[13]:


data[data.duplicated()]


# In[16]:


data.drop_duplicates(inplace=True)


# In[17]:


data[data.duplicated()]


# ## Is there any null value in any column? Show Heat-map.

# In[18]:


data.head()


# In[19]:


data.isnull()


# In[20]:


data.isnull().sum()


# In[21]:


import seaborn as sns


# In[22]:


sns.heatmap(data.isnull())


# ## for 'House of cards' what is the Show Id and who is the director of this show?

# ### isin()

# In[23]:


data.head()


# In[26]:


data[data['Title'].isin(['House of Cards'])]


# ### str.contains()

# In[27]:


data[data['Title'].str.contains('House of Cards')]


# ## In which year highest number of the TV shows and movies were released? show with Bar Graph.

# ### dtypes

# In[28]:


data.dtypes


# ### to_datetime

# In[29]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[30]:


data.dtypes


# ### dt.year.value_counts() 

# In[31]:


data['Date_N'].dt.year.value_counts()


# ### Bar Chart

# In[32]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# ## How many Movies & TV shows are in the dataset? 

# ### groupby()

# In[41]:


data.head()


# In[36]:


data.groupby('Category').Category.count()


# ## Show all the Movies that were released in te year 2020 

# In[49]:


# create new column
data['Year']=data['Date_N'].dt.year


# In[50]:


data.head(2)


# In[51]:


# filtering
data[(data['Category'] == "Movie") & (data['Year']==2020)]


# ## Show only the Titles of all TV Shows that were released in India only

# In[52]:


data.head(2)


# In[53]:


data[(data['Category']=="TV Show") & (data['Country'] == 'India')] ['Title']


# ## Show top 10 directors, who gave the highest number of TV Shows & Movies to Neflix?

# In[54]:


data['Director'].value_counts().head(10)


# ## Show all the reocrds. where 'Category is Movies and type is Comedian' or 'Country is United Kingdom'

# In[55]:


data[(data['Category']=='Movie') & (data['Type']=='Comedians') | (data['Country']=='United Kingdom')]


# ## In how many movies/shows, Tom Cruise was cast?

# In[56]:


data.head(2)


# In[57]:


data[data['Cast']=="Tom Cruise"]


# In[59]:


data[data['Cast'].str.contains('Tom Cruise')] #error because there is null values there is no cast named tom cruise


# In[60]:


#Creating new data frame to remove null values
data_new=data.dropna()


# In[61]:


data_new.head()


# In[62]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# ## What are the different ratings defined by Netflix?

# In[63]:


data.Rating.nunique()


# In[64]:


data.Rating.unique()


# ## how many movies got the 'TV-14' rating, in Canada?

# In[65]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')]


# In[66]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')].shape


# ## How many TV shows got the 'R' ratings, after year 2018

# In[68]:


data[(data['Category']=="TV Show") & (data['Rating']=='R') & (data['Year']>2018)]


# In[69]:


data[(data['Category']=="TV Show") & (data['Rating']=='R') & (data['Year']>2018)].shape


# ## What is the maximum duration of a Movie/Show on Netflix?

# In[71]:


data.Duration.unique()


# In[72]:


data.Duration.dtypes


# In[73]:


data.head(2)


# In[74]:


data[['Minutes','Unit']] = data['Duration'].str.split(' ',expand=True) # split single column into multiple


# In[75]:


data.head()


# In[76]:


data.head(2)


# In[77]:


data['Minutes'].max()


# In[78]:


data['Minutes'].min()


# In[79]:


data['Minutes'].mean()


# In[80]:


data.dtypes


# ## Which individual country has the highest no. of tv shows?

# In[82]:


data_tvshow=data[data['Category']=='TV Show']


# In[83]:


data_tvshow.Country.value_counts()


# In[84]:


data_tvshow.Country.value_counts().head(1)


# ## How can we sort the dataset by year?

# In[85]:


data.head(2)


# In[86]:


data.sort_values(by='Year')


# In[87]:


data.sort_values(by='Year', ascending=False) # in descending order


# ## Find all the instaces where:
# ### Category is 'Movie' and Type is 'Dramas'
# 
# #### OR
# 
# ### Category is 'TV Show' and Type is 'Kids TV'

# In[88]:


data.head(2)


# In[96]:


condit1=data[(data['Category']=='Movie') & (data['Type']=='Dramas')]
condit1


# In[93]:


condit2=data[(data['Category']=='TV Show') & (data['Type']== "Kids' TV") ]
condit2


# In[99]:


result=data[(data['Category']=='Movie') & (data['Type']=='Dramas') | (data['Category']=='TV Show') & (data['Type']== "Kids' TV")]
result


# In[ ]:





# In[ ]:




