#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import requests 
from bs4 import BeautifulSoup
url='https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW'


# In[61]:


page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')
print (soup)


# In[70]:


names=soup.find_all('td', class_='a-text-left mojo-field-type-title')
print(names)


# In[71]:


names_titles = [title.text.strip() for title in names]

print(names_titles)


# In[72]:


df = pd.DataFrame(columns = names_titles)

df


# In[73]:


years=soup.find_all('td', class_='a-text-left mojo-field-type-year')
print(years)


# In[74]:


years_titles = [title.text.strip() for title in years]

print(years_titles)


# In[76]:


info= soup.find_all('tr')
print(info)


# In[82]:


table_names=soup.find('tr')
print(table_names)


# In[77]:


for row in info[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[83]:


world_table_titles = [title.text.strip() for title in table_names]

print(world_table_titles)


# In[86]:


df2 = pd.DataFrame(columns = world_table_titles)

df2


# In[89]:


column_data = soup.find_all('tr')
print(column_data)


# In[90]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df2)
    df2.loc[length] = individual_row_data


# In[91]:


df2


# In[92]:


df=df2
df


# In[93]:


df.info


# In[94]:


df.describe


# In[95]:


df = df.drop_duplicates()
df


# In[96]:


#df = df.replace('N/a','')
#df = df.replace('NaN','')


df=df.fillna('')
df


# In[97]:


df.describe()


# In[98]:


df.isnull().sum()


# In[100]:


df.nunique()
df


# In[133]:


df3=df.sort_values(by="Lifetime Gross", ascending=False).head(100)
df3


# In[134]:


df4=df3.groupby('Year')['Lifetime Gross'].count()
df4


# In[135]:


# Зависимость между годами и зароботком
import seaborn as sns
import matplotlib.pyplot as plt
df4.plot()


# In[136]:


df4.plot.pie(y='Year',figsize=(10,10))


# In[161]:


df


# In[177]:


df


# In[182]:


df.set_index('Title', inplace = True)

df


# In[185]:


df["Lifetime Gross"] = df["Lifetime Gross"].str.strip("$")

print(df)


# In[187]:


df['Lifetime Gross'] = df['Lifetime Gross'].str.replace(',', '').astype(float)
print(df)


# In[188]:


df.corr()


# In[190]:


sns.heatmap(df3.corr(), annot = True)

plt.rcParams['figure.figsize'] = (20,7)

plt.show()


# In[191]:


df3.set_index('Title', inplace = True)

df3


# In[194]:


df3['Lifetime Gross'] = df3['Lifetime Gross'].replace({'\$': '', ',': ''}, regex=True).astype(float)
df3


# In[195]:


sns.heatmap(df3.corr(), annot = True)

plt.rcParams['figure.figsize'] = (20,7)

plt.show()


# In[200]:


df6 = df3.groupby('Year')[['Year', 'Lifetime Gross']].count()
df6


# In[214]:


selected_columns = df3[['Year', 'Lifetime Gross']]
selected_columns = df3.reset_index(inplace=True)
selected_columns


# In[215]:


selected_columns.corr()
selected_columns.set_index('Year', inplace = True)

selected_columns


# In[216]:


sns.heatmap(selected_columns.corr(), annot = True)

plt.rcParams['figure.figsize'] = (20,7)

plt.show()


# In[217]:


df4.plot.area(figsize = (10,5))

