from urllib import request
import re
import csv

onlycommentslist=[]
metalist=[]

req = request.Request('http://www.geenstijl.nl/mt/archieven/2014/05/das_toch_niet_normaal.html', headers={'User-Agent' : "Mozilla/5.0"})
tekst=request.urlopen(req).read()
tekst=tekst.decode(encoding="utf-8",errors="ignore").replace("\n"," ").replace("\t"," ")

commentsection=re.findall(r'<div class="commentlist">.*?</div>',tekst)
print (commentsection)
comments=re.findall(r'<article.*?>(.*?)</article>',commentsection[0])
print (comments)
print ("There are",len(comments),"comments")
for co in comments:
    metalist.append(re.findall(r'<footer>(.*?)</footer>',co))
    onlycommentslist.append(re.findall(r'<p>(.*?)</p>',co))
writer=csv.writer(open("geenstijlcomments.csv",mode="w",encoding="utf-8"))
output=zip(onlycommentslist,metalist)
writer.writerows(output)