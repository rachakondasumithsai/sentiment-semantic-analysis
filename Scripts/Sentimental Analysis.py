# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:29:42 2020

@author: racha
"""


import re
import sys
import time
import tweepy
import pandas as pd
import numpy as np


# Authenticate to Twitter
auth = tweepy.OAuthHandler("stOGyiJB2YiiOseFkCrC1Xy6f",
                       "2IB7FYAYMHe7W0vUZ5EvAqhOQkPhFOhzucVr2tPrOYEl0oiq6y")
auth.set_access_token("201589155-7nOHwAEWkpk8B56UT2wX1cW04Ze0lbHa0Sc4bL1M",
                      "HMg5XO4K8Hg1U0ivohb6fw67mluVq3mMhcSs4aUlwHnvs")

api = tweepy.API(auth, wait_on_rate_limit=True,
             wait_on_rate_limit_notify=True)

search_words = ["Canada", "University", "Dalhousie University", "Canada Education", "Halifax"]

#reading all negative words into a list
with open('negative-words.txt', 'r') as f:
    negativewords = f.readlines()
#removing '\n' in all words at ending
negativewords = [word.rstrip('\n') for word in negativewords]
#reading all positive words into a list
with open('positive-words.txt', 'r') as f:
    positivewords = f.readlines()
#reading all positive words into a list 
positivewords = [word.rstrip('\n') for word in positivewords]

#initializing counter for tracking of tweets count and index
count = 1

#creating a list for word cloud
wordcloud = []
positivewordcloud = []
negativewordcloud = []
#creating an empty list of dict
listofdict = []
#searching for tweets and writing int dataframe and matching words and calculating polarity
for items in search_words:
        print('Searching for keyword: ' + items)
        tweets = tweepy.Cursor(api.search,
                       q=items,
                       lang="en",
                       result_type="recent").items(200)
        for tweet in tweets:
            tweet_text= re.sub('http\S+|[^0-9a-zA-Z\ ]+|RT', '', tweet.text)
            #initializing polarity to 0 neutral
            polarity = 0
            #getting a list of words by lowering and splitting by space
            bagofwordslist = tweet_text.lower().split() 
            #creating an empty dict to store matched words and their count
            matchwords = {}
            #creating empty bag of words dict with freq count as value and key as word 
            bow = {}
            #calculating the polarity and adding words to list if matched
            for word in bagofwordslist:
                #update dict with key value pair
                if word not in bow:
                    bow[word] = 0
                bow[word] += 1
                
                #checking if positive words are present
                if word in positivewords:
                    polarity+=1 
                    if word not in matchwords:
                        matchwords[word] = 0
                    matchwords[word] += 1
                    #saving word to word positive word cloud
                    positivewordcloud.append(word)
                    #saving word to wordcloud
                    wordcloud.append(word)
                
                #checking if negative words are present       
                if word in negativewords:
                    polarity-=1
                    if word not in matchwords:
                        matchwords[word] = 0
                    matchwords[word] += 1
                    #saving word to word positive word cloud
                    negativewordcloud.append(word)
                    #saving word to wordcloud
                    wordcloud.append(word)
                    
            #checking the polarity        
            if polarity>0:
                polarity = 'positive'
            elif polarity<0:
                polarity = 'negative'
            else:
                polarity = 'neutral'
            #appending the tweet and its data we created into list of dict
            listofdict.append(
                {'id': count, 'tweet': tweet_text, 'bow': bow , 
                 'match': matchwords , 'polarity': polarity })
            #incrementing count for every tweet
            count+=1

#print number of tweets gathered
print("total tweets found : "+str(count))
#load listofdict to df
df = pd.DataFrame(listofdict)
#write the data frame into csv file
df.to_csv('sentimentalanalysisresulttable.csv', index = False)
#saving wordcloud to csv file
df2 = pd.DataFrame(wordcloud)
#write the data frame into csv file
df2.to_csv('wordcloud.csv', index = False)
#saving positivewordcloud to csv file
df3 = pd.DataFrame(positivewordcloud)
#write the data frame into csv file
df3.to_csv('positivewordcloud.csv', index = False)
#saving wordcloud to csv file
df4 = pd.DataFrame(negativewordcloud)
#write the data frame into csv file
df4.to_csv('negativewordcloud.csv', index = False)

