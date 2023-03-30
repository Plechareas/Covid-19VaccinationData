#!/usr/bin/env python
# coding: utf-8

# In[85]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[87]:


df=pd.read_csv("vaccination.csv")


# In[90]:


df.head()


# In[54]:


df.isnull().sum()


# In[55]:


df.fillna(0, inplace = True)
df.drop(df.index[df['areaid'] == 0], inplace = True)


# In[56]:


df.isnull().sum()


# In[69]:


df.info()


# In[76]:


df['referencedate'] =  pd.to_datetime(df['referencedate'], format='%Y-%m-%d')


# In[59]:


df.columns


# In[60]:


df.drop(["area","areaid", "dailydose1", "dailydose2", "dailydose3", "daydiff",
       "daytotal", "referencedate", "totaldistinctpersons", "totaldose1",
       "totaldose2", "totaldose3", "totalvaccinations"],axis=1, inplace=True)


# In[93]:


df_thess = df[df["area"] == 'ΘΕΣΣΑΛΟΝΙΚΗΣ'].copy()
df_thess


# In[112]:


df_thess.drop(df_thess.index[df_thess['totalvaccinations'] == 0], inplace = True)


# In[113]:


plt.figure(figsize=(18,6))
sns.lineplot(data=df_androu, x="referencedate", y="totalvaccinations")
plt.title("Total vaccinations in Thessaloniki May 2021 - May 2022")
plt.xticks(rotation=45)
plt.show()


# In[116]:


df_thess.drop(df_thess.index[df_thess['dailydose1'] == 0], inplace = True)


# In[117]:


plt.figure(figsize=(18,6))
sns.lineplot(data=df_thess, x="referencedate", y="dailydose1")
plt.xticks(rotation=90)
plt.title("Daily vaccinations of the first vaccine in Thessaloniky")


# In[115]:


plt.figure(figsize=(18,6))
sns.lineplot(data=df_thess, x="referencedate", y="dailydose2")
plt.xticks(rotation=90)
plt.title("Daily vaccinations of the second vaccine in Thessaloniky")


# In[99]:


plt.figure(figsize=(18,6))
sns.lineplot(data=df_thess, x="referencedate", y="dailydose3")
plt.xticks(rotation=90)
plt.title("Daily vaccinations of the third vaccine in Thessaloniky")


# In[102]:


df_Ark = df[df["area"] == 'ΑΡΚΑΔΙΑΣ'].copy()
df_Ark


# In[118]:


df_Ark.drop(df_Ark.index[df_Ark['totalvaccinations'] == 0], inplace = True)


# In[119]:


plt.figure(figsize=(18,6))
sns.lineplot(data=df_Ark, x="referencedate", y="totalvaccinations")
plt.title("Total vaccinations in Arkadia")
plt.xticks(rotation=45)
plt.show()


# In[103]:


plt.figure(figsize=(18,6))
sns.lineplot(data=df_Ark, x="referencedate", y="dailydose1")
plt.xticks(rotation=90)
plt.title("Daily vaccinations for the first vaccine in Arkadia")


# In[80]:


plt.figure(figsize=(18,6))
sns.lineplot(data=df_Ark, x="referencedate", y="dailydose2")
plt.xticks(rotation=90)
plt.title("Daily vaccinations for second vaccine in Arkadia")


# In[81]:


plt.figure(figsize=(18,6))
sns.lineplot(data=df_Ark, x="referencedate", y="dailydose3")
plt.xticks(rotation=90)
plt.title("Daily vaccinations for third vaccine in Arkadia")


# In[82]:


vacc_by_area = df.groupby('area').max().sort_values('totalvaccinations', ascending=False)
vacc_by_area = vacc_by_area.iloc[:10]
vacc_by_area


# In[105]:


vacc_by_area = vacc_by_area.sort_values('totaldistinctpersons', ascending=False)
vacc_by_area


# In[106]:


plt.figure(figsize=(18, 6))
plt.bar(vacc_by_area.index, vacc_by_area.totaldistinctpersons)
plt.xticks(rotation = 90)
plt.ylabel('Vaccinations per 100')
plt.xlabel('Area')
plt.show()


# In[107]:


total_vacc_by_area = df.groupby('area').max().sort_values('totalvaccinations', ascending=False)
total_vacc_by_area = total_vacc_by_area.iloc[:10]
total_vacc_by_area


# In[108]:


plt.figure(figsize=(16, 7))
plt.bar(total_vacc_by_area.index, total_vacc_by_area.totalvaccinations)
plt.title('Total vaccinations per area')
plt.xticks(rotation = 90)
plt.ylabel('Total vaccinations')
plt.xlabel('Area')
plt.show()


# In[120]:


fig = px.choropleth(df.reset_index(), locations="areaid",
                    color="totaldistinctpersons",
                    color_continuous_scale=px.colors.sequential.Electric,
                   title= "Total vaccinations per 100")

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})  #No margin on left, right, top and bottom
fig.show()


# In[ ]:




