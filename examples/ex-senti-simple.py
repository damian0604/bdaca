import csv
tweetlist=[]
processedlist=[]
with open("/home/damian/sentiment/sanders.tsv") as fi:
    reader=csv.reader(fi)
    next(reader)
    for row in reader:
        tweet=row[6]
        tweet_processed=tweet.lower().replace("!"," ").replace("."," ").replace("?"," ").replace(u"\u201A"," ").replace("'"," ").replace('"'," ").replace('#'," ").replace(':'," ")
        tweetlist.append(tweet)
        processedlist.append(tweet_processed)


#%% break

positivelist=open("/home/damian/sentiment/positive.txt").read().splitlines()
negativelist=open("/home/damian/sentiment/negative.txt").read().splitlines()

negcountlist=[]
poscountlist=[]
sentilist=[]

for tweet in processedlist:
    poscount=0
    negcount=0
    print ("Analyzing this one:",tweet)
    for word in tweet.split():
        if word in positivelist:
            poscount+=1
        elif word in negativelist:
            negcount+=1        
    print("It contained",poscount,"positive words and",negcount,"negative words.")
    poscountlist.append(poscount)
    negcountlist.append(negcount)
    sentilist.append((poscount-negcount)/len(tweet))
    
print("Average sentiment:",sum(sentilist)/len(sentilist))

#%% save
output=zip(tweetlist,processedlist,negcountlist,poscountlist,sentilist)
with open("/home/damian/sentiment/sanders-analyzed.csv",mode="w",encoding="utf-8", newline="") as fo:
    writer=csv.writer(fo)
    writer.writerows(output)


