from lxml import html
from urllib import request

req=request.Request("https://www.kieskeurig.nl/smartphone/product/3518003-samsung-galaxy-a5-2017-zwart/reviews")
tree = html.fromstring(request.urlopen(req).read().decode(encoding="utf-8",errors="ignore"))        

reviews = tree.xpath('//*[@class="reviews-single__text"]/text()')

# remove empty reviews
reviews = [r.strip() for r in reviews if r.strip()!=""]

print (len(reviews),"reviews scraped. Showing the first 60 characters of each:")
i=0
for review in reviews:
    print("Review",i,":",review[:60])
    i+=1