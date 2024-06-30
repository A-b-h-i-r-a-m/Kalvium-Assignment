#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests


# CONSIDERING PARTY WISE RESULTS FOR SAMPLE

# In[4]:



url = 'https://results.eci.gov.in/PcResultGenJune2024/index.htm'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[5]:


print(soup)


# In[6]:


soup.find_all('table')[0]


# In[7]:


table = soup.find_all('table',class_='table')[0]

#<table class="table">


# In[8]:


print(table)


# In[9]:


world_titles = table.find_all('th')[:-4]


# In[10]:


world_titles


# In[11]:


world_table_titles = [title.text for title in world_titles]
print(world_table_titles)


# In[12]:


import pandas as pd


# In[13]:


df=pd.DataFrame(columns = world_table_titles)
df


# In[14]:


column_data = table.find_all('tr')[:-1]


# In[15]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length=len(df)
    df.loc[length] = individual_row_data


# In[16]:


df


# In[17]:


df.describe()


# In[33]:


df['Won'] = df['Won'].astype(int)
df['Total'] = df['Total'].astype(int)
df['Leading'] = df["Leading"].astype(int)


# In[59]:


columns_to_display = ['Party', 'Won', 'Leading', 'Total', 'Percentage']


# In[60]:


#Top Parties

top_parties = df.nlargest(5, 'Won')[columns_to_display]
print(top_parties)


# In[61]:


#Least Seats
least_n_parties = df.nsmallest(5, 'Won')[columns_to_display]
print(least_n_parties)


# In[36]:



#Total Seats Distribution
total_seats = df['Total'].sum()
print(f"Total seats: {total_seats}")


# In[37]:


#Percentage of Seats
df['Percentage'] = (df['Won'] / total_seats) * 100
print(df[['Party', 'Percentage']])


# In[38]:


#Cumulative Seats
df['Cumulative'] = df['Won'].cumsum()
print(df[['Party', 'Cumulative']])


# In[62]:


# Seats Won by Top N Parties

top_n_parties = df.nlargest(5, 'Won')[columns_to_display]
print(top_n_parties)


# In[58]:


#Party Representation

party_representation = df[df['Won'] > 15][columns_to_display]
print(party_representation)


# In[43]:



# Party Comparison
party_comparison = df[['Party', 'Won']].sort_values(by='Won', ascending=False)
print(party_comparison)


# In[45]:


# Data Visualization

#Top 10 Parties with most seats won
plt.figure(figsize=(10, 6))
sns.barplot(x='Won', y='Party', data=top_n_parties, palette='viridis')
plt.title('Top 10 Parties with Most Seats Won')
plt.xlabel('Seats Won')
plt.ylabel('Party')
plt.show()


# In[47]:


#Histogram: Distribution of total seats won
plt.figure(figsize=(10, 6))
sns.histplot(df['Won'], bins=20, kde=True)
plt.title('Distribution of Total Seats Won')
plt.xlabel('Seats Won')
plt.ylabel('Frequency')
plt.show()


# In[48]:


#Distribution of seats won by different parties
plt.figure(figsize=(10, 6))
sns.boxplot(x='Won', data=df)
plt.title('Distribution of Seats Won by Parties')
plt.xlabel('Seats Won')
plt.show()


# In[ ]:





# In[ ]:




