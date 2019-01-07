from lxml import html
import requests

htmlsource = requests.get("https://www.kieskeurig.nl/smartphone/product/3518003-samsung-galaxy-a5-2017-zwart/reviews").text
tree = html.fromstring(htmlsource)        

reviews = tree.xpath('//*[@class="reviews-single__text"]/text()')

# remove empty reviews
reviews = [r.strip() for r in reviews if r.strip()!=""]

print (len(reviews),"reviews scraped. Showing the first 60 characters of each:")
i=0
for review in reviews:
    print("Review",i,":",review[:60])
    i+=1