import sys
import json

def readSentimentData(sentimentDataFile):
    sentimentfile = open(sentimentDataFile, "r")	# open sentiment file
    scores = {}  									# an empty dictionary
    for line in sentimentfile:                      # loop over each word / sentiment score
        word, score = line.split("\t")  			# file is tab-delimited
        scores[word] = int(score)   				# convert score to an integer, store word / sentiment in dictionary
    sentimentfile.close()							# close the file
    return scores									# return the dictionary

def readTwitterData(twitterDataFile):
    with open(twitterDataFile, "r") as tweetfile:			# open tweet file
        tweets = []										# an empty list
        for line in tweetfile:							# loop over each tweet
            try:
                line = line[0:-2]
                line = line.replace("b'",'')
                line = line.replace("\\\\","\\")
                line = line.replace("\\'","'")
                line = json.loads(line)                     # change json to dictionary
                if "text" in line:                          # process the "text" (the tweet) in the dictionary
                    line = line["text"].encode('utf-8')      # decode the unicode text in the tweet
                    tweets.append(line)						# append tweet string to list
            except:
                    raise
    return tweets									# return the list


def main():
    if len(sys.argv) > 1:
        scores_file  = sys.argv[1]         # sentiment file - AFINN-111.txt
        tweets_file = sys.argv[2]           # tweet file - output.txt
    else:
        scores_file = input('Enter AFIN file name: ')
        tweets_file = input('Enter tweet data: ')

    scores = readSentimentData(scores_file)
    tweets = readTwitterData(tweets_file)
    sentiments = {"-5":0, "-4":0, "-3":0, "-2":0, "-1":0, "0":0, "1":0, "2":0, "3":0, "4":0, "5":0}   #sentiment dictionary

    for tweet in tweets:                            # loop over each tweet
        tweetWords = tweet.split()                  # split tweet into individual words
        for word in tweetWords:                     # loop over idndividual words in each tween
            word=word.decode("utf-8")
            word = word.strip('?:!.,;"!@')          # remove extraneous characters
            word = word.replace("\n","")            # remove end of line
            if word in scores.keys():               # check if word is in sentiment dictionary
                score = scores[word]                # check if word is in sentiment dictionary
                sentiments[str(score)] += 1         # increment sentiment counter in dictionary

# print number of sentiments in each category
    print ("-5 sentiments ", sentiments["-5"])
    print ("-4 sentiments ", sentiments["-4"])
    print ("-3 sentiments ", sentiments["-3"])
    print ("-2 sentiments ", sentiments["-2"])
    print ("-1 sentiments ", sentiments["-1"])
    print (" 0 sentiments ", sentiments["0"])
    print (" 1 sentiments ", sentiments["1"])
    print (" 2 sentiments ", sentiments["2"])
    print (" 3 sentiments ", sentiments["3"])
    print (" 4 sentiments ", sentiments["4"])
    print (" 5 sentiments ", sentiments["5"])

if __name__ == '__main__':
    main()











