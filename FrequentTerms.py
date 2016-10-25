from collections import Counter
from collections import defaultdict
from nltk.corpus import stopwords 
from nltk.tokenize import wordpunct_tokenize
d = defaultdict(dict)
for line in open('C:\\Users\\Shailesh Hegde\\Desktop\\Python\\datasalman\\2016-10-24\\salman.txt','r'):
    line = line.strip()
    a,b = line.split(',',1)
    node = a.split('=',1)
    key, value = b.split('=',1)
    d[key] = value
    print(d)
    words = open('C:\\Users\\Shailesh Hegde\\Desktop\\Python\\datasalman\\2016-10-24\\salman.txt','r').read().split()
    
    d = {}
    
    for w in words:
        
        if w in d:
            
            d[w] += 1
            
            
            
                

            num_words = sum(d[w] for w in d)
                

            lst = [(d[w],w) for w in d]
            lst.sort()
            lst.reverse()
            
                
                

# Program assumes user has downloaded an imported stopwords from NLTK


            stop_words = set(stopwords.words('english')) # creating a set makes the searching faster
            print ([word for word in lst if word not in stop_words])
            print('Your input file has the following words = '+str(num_words))
            print('\n The 30 most frequent words are /n')
            i = 1
        
            for count, word in lst[:50]:
                
                print('%2s. %4s %s' %(i,count,word))
            
                i+= 1