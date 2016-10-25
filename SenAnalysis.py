import argparse
import os
import glob
from textblob import TextBlob
path = "C:\\Shailesh Hegde\\Desktop\\Python\\"
parser = argparse.ArgumentParser()
parser.add_argument("searchTerm")
args = parser.parse_args()
searchTerm = args.searchTerm
newPath =  path+searchTerm
os.chdir(newPath)
listmy = (glob.glob("*.txt"))
for file in listmy:
    with open(file) as f:
        for t in f:
            #print (t)
            analysis = TextBlob(t)
            print (analysis.sentiment)