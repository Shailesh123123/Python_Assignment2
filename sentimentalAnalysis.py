from textblob import TextBlob
with open('C:\\Users\\Shailesh Hegde\\Desktop\\Python\\datasalman\\2016-10-24\\salman.txt', 'r') as f:
    for tweet in f:
        print(tweet)
        analysis = TextBlob(tweet)
        print(analysis.sentiment)