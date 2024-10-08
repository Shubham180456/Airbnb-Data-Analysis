# -*- coding: utf-8 -*-
"""Berlin Airbnb.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kXVlRAbQoZ8K5F-kmuLUNhfOrp8lER6k

# Data View
"""

'''Import the data'''
import pandas as pd
df = pd.read_csv('/content/Airbnb Berlin.csv')
df

"""# Information of the data"""

df.info()

df.describe()

df.head()

df.tail()

"""# Cleaning of the data"""

'''Drop any missing values'''
df1=df.dropna()
df1

"""# Convert 'Price' column to numeric type"""

'''convert 'Price' column to numeric type'''
df1['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df1['Price']

"""# Top 3 Expansive Airbnb"""

'''top 3 expansive Aibnb'''
df1.sort_values(by='Price', ascending=False).head(3)

'''plot a graph top 3 expansive Airbnb '''
df1.sort_values(by='Price', ascending=False).head(3).plot(kind='bar')

"""# Common things in top 3 expansive Airbnb"""

'''what is common in top 3 expansive Aibnb'''
df1.sort_values(by='Price', ascending=False).head(3).describe()

"""# find 5 highest rated Airbnbs in each city"""

'''find 5 highest rated Airbnbs in each city'''
df1.groupby('City')['Overall Rating'].nlargest(5)

'''plot the 5 highest rated Airbnbs in each city'''
df1.groupby('City')['Overall Rating'].nlargest(5).plot(kind='bar')

"""# Summary statistics for Overall Rating and Price"""

'''Relation between overall rating and price'''
df2 = df1[['Overall Rating', 'Price']]
df2 # Use a list of column names to select multiple columns

"""# Top 5 listings by rating"""

'''Top 5 listings by rating'''
df2.sort_values(by='Overall Rating', ascending=False).head(5)

from matplotlib import pyplot as plt
df2['Price'].plot(kind='hist', bins=20, title='Price')
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
df2['Overall Rating'].plot(kind='hist', bins=20, title='Overall Rating')
plt.gca().spines[['top', 'right',]].set_visible(False)

df2.describe()

df3=df1[df1["Price"]==455.000000]
df3

"""# Analyze Demand,Pricing Trends, and Time Analysis"""

'''daily demand for Airbnb listings'''
df1.groupby('review_date').size()

'''5 highest demand date'''
df1.groupby('review_date').size().nlargest(5)

'''plot the 5 highest demand date'''
df1.groupby('review_date').size().nlargest(5).plot(kind='bar')

'''Calculate daily average price'''
df4=df1.groupby('review_date')['Price'].mean()
df4

'''top 5 daily average price'''
df4.sort_values(ascending=False).head(5)

'''graph top 5 daily average price'''
df4.sort_values(ascending=False).head(5).plot(kind='bar')

"""# Analyze City-Based Performance"""

'''Group by city and calculate the average price and rating per city'''
df5=df1.groupby('City')[['Price', 'Overall Rating']].mean()
df5

from matplotlib import pyplot as plt
df5['Overall Rating'].plot(kind='hist', bins=20, title='Overall Rating')
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
df5['Price'].plot(kind='hist', bins=20, title='Price')
plt.gca().spines[['top', 'right',]].set_visible(False)

'''plot the average price and rating per city'''
df5.plot(kind='bar')

'''Top 5 cities by the number of listings'''
df1.groupby('City').size().sort_values(ascending=False).head(5)

'''plot the Top 5 cities by the number of listings'''
df1.groupby('City').size().sort_values(ascending=False).head(5).plot(kind='bar')

