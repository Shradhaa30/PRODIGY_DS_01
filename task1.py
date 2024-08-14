#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("D:\stroke_dataset.csv")
print(df.head())


# In[3]:


# Bar chart for Gender Distribution
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(6, 5))
plt.bar(gender_counts.index, gender_counts.values, color=['blue', 'brown'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()        
# Histogram for Age Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=20, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()


# In[ ]:




