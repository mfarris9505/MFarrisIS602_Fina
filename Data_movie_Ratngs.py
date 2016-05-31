# -*- coding: utf-8 -*-
"""
Data Extraction and Cleaning

Source:http://grouplens.org/datasets/movielens/
"""
import pandas as pd 
import csv


f = open("data/u.data")
text = csv.reader(f, delimiter = "\t")
ratings = list(text)

f = open("data/u.user")
text = csv.reader(f, delimiter = "|")
user = list(text)

f = open("data/u.item")
text = csv.reader(f, delimiter = "|")
item = list(text)

f = open("data/u.occupation")
text = csv.reader(f, delimiter = "\t")
jobs = list(text)


ratings_pd = pd.DataFrame(ratings, columns = ["user_id","movie_id", "rating","timestamp"])
items_pd = pd.DataFrame(item, columns = ["movie_id","title","release","video_release","IMDB","unknown","Action","Adventure","Animation","Child","Comedy","Crime","Doc","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi", "Thriller","War", "Western"])
user_pd = pd.DataFrame(user, columns = ["user_id","age","gender","occupation","zip"])

total_pd = ratings_pd.merge(items_pd, how="left", left_on = "movie_id", right_on="movie_id")
total_pd = total_pd.merge(user_pd, how="left", left_on = "user_id", right_on="user_id")


# Using Pandas to Clean and Concise Data
total_pd = total_pd.drop(["movie_id","user_id","timestamp","title","unknown","release","video_release", "IMDB", "zip"], 1)

map_gender = {"M":0,"F":1}
map_jobs = {}

i = 0 
for job in jobs:
    map_jobs[job[0]] = i
    i = i + 1

total_pd = total_pd.replace({"gender": map_gender, 'occupation': map_jobs})


total_pd.to_csv("total_pd.csv")
