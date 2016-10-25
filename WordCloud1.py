import argparse
import os
import glob
from textblob import TextBlob
path = "C:\\Shailesh Hegde\\Desktop\\Python\\Data\\"

parser = argparse.ArgumentParser()
parser.add_argument("searchTerm")
args = parser.parse_args()
searchTerm = args.searchTerm

newPath =  path+searchTerm
os.chdir(newPath)
listmy = (glob.glob("*.txt"))

for file in listmy:
    with open(file,'r') as f:
    stop_words = set(stopwords.words('english'))

    
    
    if text not in stop_words:
        
        wordcloud = WordCloud().generate(text)


import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()