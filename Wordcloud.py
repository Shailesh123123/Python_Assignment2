from wordcloud import WordCloud
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
from nltk.corpus import stopwords 
from nltk.tokenize import wordpunct_tokenize


text = open('C:\\Users\\Shailesh Hegde\\Desktop\\Python\\datasalman\\2016-10-24\\salman.txt','r').read()
stop_words = set(stopwords.words('english'))
for word in text:
    
    if text not in stop_words:
        
        wordcloud = WordCloud().generate(text)


import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()