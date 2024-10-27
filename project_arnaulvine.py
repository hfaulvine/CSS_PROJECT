#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:27:22 2024

@author: aulvine
"""

import pandas as pd
import numpy as np

path ="../Téléchargements/movie_dataset (1).csv"
df = pd.read_csv(path)

# A summary of statistics for numerical columns in a DataFrame
print(df.describe())

# Display the column labels of the DataFrame
print(df.columns)

#Rename the columns to remove spaces
df=df.rename(columns={' Runtime (Minutes)':'Runtime_(Minutes)', 'Revenue (Millions)':'Revenue_(Millions)'})

print(df)

#Filling the NaN values with the mean
average_revenue = df['Revenue_(Millions)'].mean() 
average_metascore=df['Metascore'].mean()

df['Revenue_(Millions)']=df['Revenue_(Millions)'].fillna(average_revenue) 
df['Metascore']=df['Metascore'].fillna(average_metascore)
 
print(df)

#1- What is the highest rated movie in the dataset
highest_rated_movie=df.loc[df['Rating'].idxmax(),'Title']
print('The highest rated movie in the dataset is',highest_rated_movie)

#2- What is the average revenue of all movies in the dataset? 
average_revenue = df['Revenue_(Millions)'].mean()
print('The average revenue of all movies in the dataset is',average_revenue)

#3- What is the average revenue of movies from 2015 to 2017 in the dataset?
average_revenue_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]['Revenue_(Millions)'].mean()
print('The average revenue of movies from 2015 to 2017 in the dataset is',average_revenue_2015_2017)

#4- How many movies were released in the year 2016?
count_movies_2016 = df[df['Year'] == 2016]
movies_released_2016=len(count_movies_2016)
print('The number of movies were released in the Year 2016 is',movies_released_2016)

#5- How many movies were directed by Christopher Nolan?
nolan_movies = df[df['Director'] == 'Christopher Nolan']
movies_directed_by_Chris=len(nolan_movies)
print('The number of movies were directed by christopher Nolan is',movies_directed_by_Chris)

#6- How many movies in the dataset have a rating of at least 8.0?
high_rated_movies_count = np.sum(np.where(df['Rating']>= 8.0, 1, 0)) 
print('The number of movies in the dataset have a rating of at least 8.0 is',high_rated_movies_count)

#7- What is the median rating of movies directed by Christopher Nolan?
nolan_median_rating = nolan_movies['Rating'].median()
print('The median rating of movies directed by Christpher nolan is',nolan_median_rating)

#8- Find the year with the highest average rating?
average_ratings_by_year = df.groupby('Year')['Rating'].mean()
print(average_ratings_by_year)

max_average_rating = average_ratings_by_year.max()
print("Maximum Average Rating:", max_average_rating)

year_highest_rating = average_ratings_by_year.idxmax()
print("Year with Highest Average Rating:", year_highest_rating)

#9- What is the percentage increase in number of movies made between 2006 and 2016?
year_counts=df['Year'].value_counts().sort_index()
movies_2006 = year_counts.get(2006,0)
movies_2016 = year_counts.get(2016,0)
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print('The percentage increase in number of movies made between 2006 and 2016 is', percentage_increase)

#10- Find the most common actor in all the movies?
all_actors = df['Actors'].str.cat(sep=',').split(',')
most_common_actor = pd.Series(all_actors).value_counts().idxmax()
print('The most common actor in all the movies is',most_common_actor)

#11- How many unique genres are there in the dataset?
all_genres = df['Genre'].str.cat(sep=',').split(',')
unique_genres = len(set(all_genres))
print('The number of unique genres are there in dataset is', unique_genres)



