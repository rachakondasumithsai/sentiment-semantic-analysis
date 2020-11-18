# sentiment-semantic-analysis

## A. Sentiment Analysis
1. I have considered only message present in tweets.
2. Data cleaning[1][2] is done using regular expression technique with regex function in python. Cleaned tweets are available at cleanedtweets.csv
3. Bag of words are created using python script for every tweet[3][4].
4. I have downloaded the positive and negative words (negative-words.txt and positive-words.txt) and then compared them with bag of words and saved the matched words along with its frequency count.
5. Sentimental analysis is performed by tagging each tweet a polarity such as positive, negative and neutral using matched positive and negative words.
I have created an output file as csv named sentimentalanalysisresulttable.csv
This csv contains id, tweet, bow, match and polarity columns.
The cleaned tweet is saved in tweet column. The bow column contains bag of words along with frequency count for every tweet. If there are any matched positive or negative words, then they are present in match column with frequency count. The polarity column contains the overall polarity of the text or tweet. Polarity is calculated based on highest type of matched words. A tweet is considered as neutral if it has no match words or balanced amount of positive and negative words.
The script for above sentimental analysis is available in Sentimental Analysis.py.
6. Using Tableau, I have visualized frequently occurring words for individual positive and negative word clouds as well as both word cloud[5].
All word cloud visualizations are available at Negative Word Cloud Fullscreen.png, Negative Word Cloud.png, Positive and Negative Word Cloud Fullscreen.png, Positive and Negative Word Cloud.png, Positive Word Cloud Fullscreen.png, Positive Word Cloud.png.
I have maintained all matched words when calculating the polarity and saved them into csv files. Data source for word cloud is available in files negativewordcloud.csv, positivewordcloud.csv and wordcloud.csv, by using these data sources I have created sheets with visualizations.
## B. Semantic Analysis
7. I have obtained news articles and cleaned them using regular expression technique in python. I have saved every article into a new document in json format[6]. The documents are available in jsonfiles folder[7].
8. Each file is considered as one news article which is cleaned.
9. Each news file contains title, description and content.
10. I have calculated TF-IDF (term frequency-inverse document frequency)
	10.a. I have calculated total number of documents[8]. It is available in file total_no_news.json, and I have considered search query with words “Canada”, “University”, “Dalhousie University”, “Halifax”, “Business”, and searched in every document to find out in how many documents these words have appeared[9]. The output file is saved into tf_idf.xlsx, where total documents (N), search keyword, document count for each keyword (df), N/df value and Log10(N/df) values are calculated and available[10][11].
	10.b. By considering search term as “Canada”, I calculated the count of occurrence of this word in each article. I have found the article that has the maximum occurrence of word “Canada”, by retrieving and printing entry with maximum value of frequency. The output file is saved into canadadf.xlsx with filenames and their total words (m), frequency (f) and relative frequency (f/m). I have found the article which contains highest frequency and printed it on console and is available at Output.png.
	10.c. I have also computed relative frequency (f/m) value for each article and saved into canadadf.xlsx, and I have found the news article which has highest relative frequency (f/m) value by finding and retrieving the maximum of relative frequency (f/m) column. The article output is printed on console and is available at Output.png.
## References:
[1] J. Brownlee, “How to Clean Text for Machine Learning with Python,” Machine Learning Mastery, 17-Oct-2017. [Online]. Available: https://machinelearningmastery.com/clean-text-machine-learning-python/. [Accessed: 13-Apr-2020]
[2] “Python re.sub Examples,” Lzone.de, 2020. [Online]. Available: https://lzone.de/examples/Python%20re.sub. [Accessed: 13-Apr-2020]
[3] insightsbot, “Bag of Words Algorithm in Python Introduction,” InsightsBot, 09-Dec-2017. [Online]. Available: http://www.insightsbot.com/bag-of-words-algorithm-in-python-introduction/. [Accessed: 13-Apr-2020]
[4] U. Malik, “Python for NLP: Creating Bag of Words Model from Scratch,” Stack Abuse, 2018. [Online]. Available: https://stackabuse.com/python-for-nlp-creating-bag-of-words-model-from-scratch/. [Accessed: 13-Apr-2020]
[5] Parul Pandey, “Word Clouds in Tableau: Quick & Easy. - Towards Data Science,” Medium, 20-Feb-2019. [Online]. Available: https://towardsdatascience.com/word-clouds-in-tableau-quick-easy-e71519cf507a. [Accessed: 13-Apr-2020]
[6] “Save a dictionary to a file,” pythonspot, 25-Jul-2016. [Online]. Available: https://pythonspot.com/save-a-dictionary-to-a-file/. [Accessed: 13-Apr-2020]
[7] Python client library - News API, “Python client library - News API,” Newsapi.org, 2017. [Online]. Available: https://newsapi.org/docs/client-libraries/python. [Accessed: 13-Apr-2020]
[8] K. Weaver, “Get JSON file with Python,” Gist, 10-Mar-2017. [Online]. Available: https://gist.github.com/keithweaver/f803d6ad45d3ccc193315d8af40221be. [Accessed: 13-Apr-2020]
[9] “How to check if Python string contains another string,” Educative: Interactive Courses for Software Developers, 2020. [Online]. Available: https://www.educative.io/edpresso/how-to-check-if-python-string-contains-another-string. [Accessed: 13-Apr-2020]
[10] “Adding new column to existing DataFrame in Pandas - GeeksforGeeks,” GeeksforGeeks, 11-Dec-2018. [Online]. Available: https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/. [Accessed: 13-Apr-2020]
[11] “numpy.log10 — NumPy v1.17 Manual,” Scipy.org, 2019. [Online]. Available: https://docs.scipy.org/doc/numpy/reference/generated/numpy.log10.html. [Accessed: 13-Apr-2020]
