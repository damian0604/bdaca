from lxml import html
from urllib import request

req=request.Request("http://www.kieskeurig.nl/smartphone/product/2334455-apple-iphone-6/reviews")
tree = html.fromstring(request.urlopen(req).read().decode(encoding="utf-8",errors="ignore"))        

reviews = tree.xpath('//*[@class="grid margin-mobile-top-large single-review"]//div[@class="user-review grid-tablet-portrait-9 grid-tablet-landscape-8 grid-gutter-mobile-large"]/text()')

# remove empty reviews
reviews = [r for r in reviews if r.strip()!=""]

print (len(reviews),"reviews scraped. Showing the first 60 characters of each:")
i=0
for review in reviews:
    print("Review",i,":",review[:60])
    i+=1