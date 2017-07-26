# __author__ = 'homecomputer'
import json
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import re

def readTwitterData(twitterDataFile):
    tweetfile = open(twitterDataFile, "r")          # open tweet file
    tweets = []                                     # an empty list
    for line in tweetfile:                          # loop over each tweet
        line = line[0:-2]
        line = line.replace("b'",'')
        line = line.replace("\\\\","\\")
        line = line.replace("\\'","'")
        try:
            line = json.loads(line)                    #  change json to dictionary
            tweets.append(line)                     # append tweet string to list
        except:
            continue
    tweetfile.close()                               # close the file
    return tweets                                   # return the list

tweets_data = readTwitterData('output.txt')

tweets = pd.DataFrame()

tweets['tweet'] = list(map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet['user']['lang'] if 'user' in tweet else None, tweets_data))
tweets_by_lang = tweets['lang'].value_counts()
print (tweets_by_lang[:5]) #outputs top 5 languages

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of Tweets' , fontsize=15)
ax.set_title('Top 10 Languages', fontsize=15, fontweight='bold')
tweets_by_lang[:10].plot(ax=ax, kind='bar', color='green')

pylab.show()
