import json
import pandas as pd
import matplotlib.pyplot as plt
import pylab
# import re

def readTwitterData(twitterDataFile):
    tweets = []                                     # an empty list
    with open(twitterDataFile, "r") as tweetfile:    # open tweet file
        for line in tweetfile:                          # loop over each tweet
            line = line[0:-2]
            line = line.replace("b'",'')
            line = line.replace("\\\\","\\")
            line = line.replace("\\'","'")
            line = json.loads(line)                     # change json to dictionary
            tweets.append(line)                     # append tweet string to list
    return tweets                               # return the list

# tweets_data = readTwitterData('output.txt')

# tweets = pd.DataFrame()

# tweets['tweet'] = list(map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data))


def word_in_text(word, text):
        word = word.lower()
        text = text.lower()
        match = re.search(word,text)
        if match:
                return True
        return False

def key_words(row):
        words = []
        if row['text']:
                text = row["text"].lower()
                if "lyme" in text or "lyme disease" in text:
                        words.append("Lyme_Disease")
                if "CDC" in text or "Centers for Disease Control" in text:
                        words.append("CDC")
                if "tularemia" in text or "rabbit fever" in text:
                        words.append("Tularemia")
                if "plague" in text or "black death" in text:
                        words.append("Bubonic_Plague")
        return ",".join(words)

# def extract_link(text):
#      regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
#      match = re.search(regex, text)
#      if match:
#              return ''

if __name__ == '__main__':
        tweets_data_path = 'output.txt'
        tweets_data = []

        tweets_data = readTwitterData(tweets_data_path)
        tweets = pd.DataFrame()
        texts = []
        tweets['text'] = list(map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data))
        # for tweet in tweets['tweet']:
        #         texts.append(tweet['text'])

        # tweets['text'] = texts

        tweets["words"] = tweets.apply(key_words,axis=1)
        counts = tweets["words"].value_counts()
        print(counts)

        fig, ax = plt.subplots()
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=10)
        ax.set_xlabel('Key Words', fontsize=15)
        ax.set_ylabel('Number of Tweets' , fontsize=15)
        ax.set_title('Key Words', fontsize=15, fontweight='bold')
        counts[1:5].plot(ax=ax, kind='bar', color='purple')

        pylab.show()
