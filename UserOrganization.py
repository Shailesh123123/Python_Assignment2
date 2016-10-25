import argparse
import os
import glob
import json
import pandas as pd
from textblob import TextBlob
path = "C:\\Shailesh Hegde\\Desktop\\Python\\"
parser = argparse.ArgumentParser()
parser.add_argument("searchTerm")
args = parser.parse_args()
searchTerm = args.searchTerm
newPath =  path+searchTerm
os.chdir(newPath)
listmy = (glob.glob("*.json"))
test = 100
for file in listmy:
    with open(file,'r') as json_data:
        a = json.load(json_data)
data = a['statuses']
for i in data:
    print (i['user']['screen_name'] + "  " + i['created_at'] )