from lxml import html
from urllib import request

req=request.Request("http://www.kieskeurig.nl/tablet/samsung/galaxy_tab_3_101_wifi_16gb/reviews/1344691")
tree = html.fromstring(request.urlopen(req).read().decode(encoding="utf-8",errors="ignore"))        

reviews = tree.xpath('//*[@id="reviews-container"]//*[@class="text margin-mobile-bottom-large"]/text()')

print (len(reviews),"reviews scraped. Showing the first 60 characters of each:")
i=0
for review in reviews:
    print("Review",i,":",review[:60])
    i+=1