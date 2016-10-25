import argparse
import os
import datetime as dt
import oauth2 as oauth
import json
import urllib.request as ur
import urllib.parse as par
from requests_oauthlib import OAuth1
import requests

API_KEY = "fIsG5ocnl8SVgbxD0aESYDkhz"
API_SECRET = "IKytIIG1oTbKwtdAuVUbJSzyXv4DnF8TTJkWHzgYPqG4hx1bQR"
ACCESS_TOKEN = "788621334687391744-T0qILt4jZgXUyOdmjs7lQWgKtBwXFTR"
ACCESS_TOKEN_SECRET = "zCH6Idk3DFzPUl7xBKP4cDVgNUOeu3vcBhTEp0DabKxKL"
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
requests.get(url, auth=auth)

path = "C:\\Shailesh Hegde\\Desktop\\Python\\"
parser = argparse.ArgumentParser()
parser.add_argument("--date")
parser.add_argument("searchTerm")
args = parser.parse_args()
date = args.date
todayDate = dt.datetime.today().strftime("%m/%d/%Y")
print (todayDate)
searchTerm = args.searchTerm

url1 = "https://api.twitter.com/1.1/search/tweets.json?q=" + searchTerm +"&result_type=recent"
r = requests.get(url1, auth=auth)

def folderCheck():
    if(os.path.isdir(path+searchTerm)):
        print ("Folder " + searchTerm + " is Present")
        print ("checking for date specific folder...")
        if not date:
            print (todayDate)
            newPath =  path+searchTerm+"\\"+dt.datetime.now().strftime('%Y-%m-%d')
            print (newPath)
            createFile(r, searchTerm, path+searchTerm)
            createjsonFile(r, searchTerm, path+searchTerm)
            if(os.path.isdir(newPath)):
                print ("todays's date folder present")
                createFile(r, searchTerm, newPath)
            else:
                mydir = os.path.join(path+searchTerm, dt.datetime.now().strftime('%Y-%m-%d'))
                os.makedirs(mydir)
                createFile(r, searchTerm, newPath)
                #os.makedirs(path+searchTerm+"\\"+str(todayDate) )  
        else:
           if(os.path.isdir(path+searchTerm+"\\"+date)):
                print ("DATE FOLDER PRESENT")
           else:
                print ("Creating Date Folder..")
                os.makedirs(path+searchTerm+"\\"+date)
    else:
        print("Folder " + searchTerm + "is Absent")
        print("Creating a new Folder!!!!" + searchTerm)
        os.makedirs(path+searchTerm)
    return;



def createFile(r, searchTerm, newPath):
    searchTermnew = searchTerm +"_" + dt.datetime.now().strftime('%Y-%m-%d') + ".txt"
    file_loc = os.path.join(newPath, searchTermnew)
    try:
        fp = open(file_loc)
    except IOError:
        with open(file_loc, 'w') as f:
            json.dump(r.json(), f)
        #fp = open(file_loc, 'a')
    #with open(searchTermnew, 'w+') as d:

def createjsonFile(r, searchTerm, newPath):
    searchTermnew = searchTerm +"_" + dt.datetime.now().strftime('%Y-%m-%d') + ".json"
    file_loc = os.path.join(newPath, searchTermnew)
    try:
        fp = open(file_loc)
    except IOError:
        with open(file_loc, 'w') as f:
            json.dump(r.json(), f)


folderCheck()
print(args)