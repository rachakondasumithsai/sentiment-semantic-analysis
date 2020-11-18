# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:11:22 2020

@author: racha
"""

import os
import requests
import json
import re
import newsapi
from newsapi import NewsApiClient
import pandas as pd
import numpy as np

# Init defining API
newsapi = NewsApiClient(api_key='92c12525ca5f4ed5a6f26f4b36d23d4a')
#api = NewsApiClient(api_key='92c12525ca5f4ed5a6f26f4b36d23d4a')
api_key='92c12525ca5f4ed5a6f26f4b36d23d4a'

#initialising search key words
searchkeynews=["Canada", "University", "Dalhousie University", "Canada Education", "Halifax","Moncton","Toronto"]
#initializing count for tracking number of articles retrived
count = 1

#iterating all items in search key words
for item in searchkeynews:
                for pg in range(1, 2):
                    #getting a resonse object by creating a request to API
                    response = requests.get("https://newsapi.org/v2/everything",
                                       {'q': item, 'language': 'en',
                                        'sortBy': 'popularity', 'apiKey': '92c12525ca5f4ed5a6f26f4b36d23d4a',
                                        'pageSize':  100, 'page': pg})
                    #parsing response to json format
                    response_json = json.loads(response.text)
                    #iterating though each article in response object 
                    for article in response_json['articles']:
                        #if any description or content value is None then cntinue
                        if article.get('description') is None or article.get('content') is None:
                            continue
                        #saving title
                        article_title = article['title']
                        #cleaning and saving description
                        article_description = re.sub('http\S+|[^0-9a-zA-Z\ ]+|RT',
                            " ", article.get('description'))
                        #Clean content only if description is available otherwise continue
                        if article.get('description') is None:
                            continue
                        else:
                            article_content = re.sub('http\S+|[^0-9a-zA-Z\ ]+|RT',
                            " ", article.get('content'))
                        
                        #Creating and Writing into JSON Files 
                        #creating a dict with article information
                        file = {'id': count, 'article_title': article_title,
                                               'article_description': article_description,
                                               'article_content': article_content}
                        #dumping json file
                        writejson = json.dumps(file)
                        #opening articles based on index number
                        f = open("jsonfiles/article{}.json".format(count),"w")
                        #writing into opened file
                        f.write(writejson)
                        #closing the file
                        f.close()
                        
                        #incrementing the counter for article tracking
                        count+=1

#create and write into a json file for total number of news retrived
#dumping json file
writejson = json.dumps({'Total_news': count})
#opening Json file
f = open("jsonfiles/total_no_news.json","w")
#writing into json
f.write(writejson)
#closing file
f.close()   

#opening all json files
#method for getting json data by opening and loading the data using path
def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)
    
#path for base directory
base_dir = 'jsonfiles/' 
#creating a dict for calculating frequencies and initialize them to zero                   
wor_freq_dict = {'Canada': 0 , 'University': 0, 'Dalhousie University': 0, 'Halifax': 0, 'Business': 0}
#creating a list of lists to save the dataframe artcle, total words, freq, relative freq
listoflists = []

#initializing index to 1 for tracking purpose 
index = 1
#initializing a list of search words
search_query = ['Canada', 'University', 'Dalhousie University', 'Halifax', 'Business']

#iterating through each file in directory
for file in os.listdir(base_dir):

    #checking If file is a json, and index is lessthan or equal to 688
    if 'json' in file and index<=688:
        
        #get the JSON data append all info to a string
        myObj=getJSON("jsonfiles/article{}.json".format(index))
        news_text = myObj['article_title']+" "+myObj['article_description']+" "+myObj['article_content']
        
        #iterate through eaxh query and check whether that query is in the news text.
        #if it is present then increment the word frequency with respect to query word
        for query in search_query:
            if query in news_text: 
                wor_freq_dict[query] += 1
                      
        #initializing frequency as zero used for cal freq of 'Canada' in each article
        freq=0
        
        #iterating through each word in list of words returned by split().
        #If word is 'Canada' then increment the frequency
        for word in news_text.split():
            if word == "Canada":
                freq+=1
        
        #checking if frequency is greater than zero then append the article with index, total words in text, frequency
        if freq>0:
            listoflists.append(['article{}'.format(index), len(news_text.split()), freq])

        #incrementing the index value
        index+=1
 
#calculating total number of files on which operation is done
total_files = index-1
#print total records
print("\ntotal files are : {}\n".format(total_files))

#preparing TF-IDF data frame
#creating a dataframe
tfidf = pd.DataFrame(wor_freq_dict.items(), columns=['Term', 'Docs contining terms(df)'])

#inserting a new columns with including calculated values
tfidf['N/df'] = total_files/tfidf['Docs contining terms(df)']

tfidf['Log10(N/df)'] = np.log10(tfidf['N/df'])

#writing into excel file
tfidf.to_excel("tf_idf.xlsx", index=False)

#preparing canada wordcount dataframe for each article
canadadf = pd.DataFrame(listoflists, columns=['Canada appeared in {} documents'.format(len(listoflists)), 
                                              'Total Words (m)', 'Frequency (f)'])

canadadf['relative frequency (f/m)'] = canadadf['Frequency (f)']/canadadf['Total Words (m)']

canadadf.to_excel("canadadf.xlsx", index=False)

#getting maximum frequency (f) article
temp3 = canadadf.loc[canadadf['Frequency (f)'].idxmax()]
#printing highest freq value
print("\nPrinting highest frequency (f) entry\n")
print(temp3)
print("\n")
#retriving Json file containing the max(f) value
retrivedarticle=getJSON("jsonfiles/{}.json".format(temp3['Canada appeared in {} documents'.format(len(listoflists))]))
#printing the Title Description and Content
print("\n<---Doc containing max freq count--->\n")
print("Title: "+retrivedarticle['article_title']+"\n")
print("Description: "+retrivedarticle['article_description']+"\n")
print("Content: "+retrivedarticle['article_content']+"\n")
print("<----------------------------------->\n")


#getting maximum of (f/m) from all alticles
temp = canadadf[canadadf['relative frequency (f/m)']==canadadf['relative frequency (f/m)'].max()]
temp2 = canadadf.loc[canadadf['relative frequency (f/m)'].idxmax()]
#print highest relative freq data
print("\nPrinting highest relative frequency (f/m) entry\n")
print(temp2)
#retriving Json file containing the max(f/m) value
retrivedarticle=getJSON("jsonfiles/{}.json".format(temp2['Canada appeared in {} documents'.format(len(listoflists))]))
#printing the Title Description and Content
print("\n<---Doc containing max (f/m) value--->\n")
print("Title: "+retrivedarticle['article_title']+"\n")
print("Description: "+retrivedarticle['article_description']+"\n")
print("Content: "+retrivedarticle['article_content']+"\n")
print("<----------------------------------->\n")



