# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:51:03 2021

@author: sachin
"""
import praw

reddit = praw.Reddit(
    client_id="0Dr0yv8JxUNwkg",
    client_secret="-63wewAiP6_4nonn7KBMtZz6oiqo-g",
    password="Reddit@579",
    user_agent="ssd user agent",
    username="ssd579",
)

subreddit = reddit.subreddit("investing")

for submission in reddit.subreddit("all").hot(limit=100):
    print(submission.title)

