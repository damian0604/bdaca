
#%% example 1: Google Books

from urllib.request import urlopen
import json
from pprint import pprint
antwoord=urlopen("https://www.googleapis.com/books/v1/volumes?q=python").read()
data=json.loads(antwoord.decode("utf-8"))
pprint(data)
totalpages=0
numberofbooks=0
for boek in niklas["items"]:  
    pages=int(boek["volumeInfo"]["pageCount"])
    print(pages)
    totalpages=totalpages+pages
    numberofbooks=numberofbooks+1
print ("The average length of a book by Luhmann is", totalpages/numberofbooks, "pages")



#%% alternative approach example2

pagelist=[]
for boek in niklas["items"]:
    pagelist.append(int(boek["volumeInfo"]["pageCount"]))
print ("The average length of a book by Luhmann is", sum(pagelist)/len(pagelist), "pages")




#%% example 3: Twitter 
from twitter import *

CONSUMER_KEY = "......................"
CONSUMER_SECRET = "......................"
ACCESS_KEY = "......................"
ACCESS_SECRET = "......................"

twitter = Twitter(auth = OAuth(ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
posts=twitter.statuses.user_timeline(screen_name="damian0604", count=20)

tweep="damian0604"
info=twitter.users.show(screen_name=tweep)
print(tweep,"has",info["followers_count"],"followers.")
print("He is following",info["friends_count"], "people.")
print("This means that his follower-to-following-ratio is",int(info["followers_count"])/int(info["friends_count"]))
print("\nThis is what he says about himself:\n")
print(info["description"])




#%% example 4: saving a Twitter profile as JSON
with open("/home/damian/someone.json", mode="w", encoding="utf-8") as fo:
        json.dump(info,fo)
        

#%% example 5: saving tweets and dates as CSV

import csv
tweets=[]
dates=[]
for i in posts:
    tweets.append(i["text"])
    dates.append(i["created_at"])
output=zip(dates,tweets)
with open("tweetswithdate.csv",mode="w",encoding="utf-8") as fo:
    writer=csv.writer(fo)
    writer.writerows(output) 
