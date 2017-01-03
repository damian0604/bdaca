#/usr/bin/env python3
from twitter import *
import json

consumer_key = "XXX"
consumer_secret = "XXX"
access_key = "XXX"
access_secret = "XXX"

tweetidfilename='sanders.txt'

auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)

tweetids=[e.strip() for e in open(tweetidfilename).readlines()]

# LIMIT TO 900 TWEETS B/C OF API RESTRICTIONS AND CREATE CHUNKS OF 100
def chunker(seq, size):
    return [seq[pos:pos + size] for pos in range(0, len(seq), size)]
batches = chunker(tweetids[:900],100)

# API expects comma-separated strings, no lists:
batches = [','.join(l) for l in batches]

posts = []

for batch in batches:
    posts += twitter.statuses.lookup(_id=batch)


headers=["text","retweeted","retweet_count","hashtags","urls","created_at","description","screen_name","name","friends_count","followers_count","statuses_count"]
with open('sanders.tsv',mode='w') as fo:
        fo.write("\t".join(headers)+"\n")
        for post in posts:
            output=[]
            output.append(post["text"].replace("\t"," ").replace("\n"," ").replace("\r"," "))
            output.append(str(post["retweeted"]))
            output.append(str(post["retweet_count"]))            
            hashtags = [tag["text"] for tag in post["entities"]["hashtags"]]        
            output.append(str(hashtags))
            urls = [u["expanded_url"] for u in post["entities"]["urls"]]    
            output.append(str(urls))    
            output.append(post["created_at"])
            output.append(post["user"]["description"].replace("\t"," ").replace("\n"," ").replace("\r"," "))
            output.append(post["user"]["screen_name"])
            output.append(post["user"]["name"].replace("\t"," ").replace("\n"," ").replace("\r"," "))
            output.append(str(post["user"]["friends_count"]))
            output.append(str(post["user"]["followers_count"]))
            output.append(str(post["user"]["statuses_count"]))            
            fo.write("\t".join(output)+"\n")
