import json
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import re

def readTwitterData(twitterDataFile):
    tweets = []                                     # an empty list
    with open(twitterDataFile, "r") as tweetfile:    # open tweet file
        for line in tweetfile:                          # loop over each tweet
            try:
                line = line[0:-2]
                line = line.replace("b'",'')
                line = line.replace("\\\\","\\")
                line = line.replace("\\'","'")
                line = json.loads(line)                     # change json to dictionary
                tweets.append(line)                     # append tweet string to list
            except:
                continue
    return tweets                                   # return the list


if __name__=='__main__':
    tweets_data_path = 'output.txt'
    tweets_data = readTwitterData(tweets_data_path)
    tweets_file = open(tweets_data_path, "r")

    tweets = pd.DataFrame()

    tweets['tweet'] = list(map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data))
    tweets['location'] = list(map(lambda tweet: tweet['user']['location'] if 'user' in tweet else None, tweets_data))
    tweets_by_loc = tweets['location'].value_counts()
    print (tweets_by_loc[:10]) # outputs top 10 locations

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Locations', fontsize=15)
    ax.set_ylabel('Number of Tweets' , fontsize=15)
    ax.set_title('Top 10 Locations', fontsize=15, fontweight='bold')
    tweets_by_loc[:10].plot(ax=ax, kind='bar', color='blue')

    pylab.show()
