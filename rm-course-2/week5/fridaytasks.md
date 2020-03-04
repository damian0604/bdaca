# Week 5, Friday
Big Data and Automated Content Analysis I+II (12 ECTS)

Anne Kroon and Damian Trilling


## Task 1: Preprocessing data

Take a dataset of your choice. Use the techniques we covered this week (look it up on the slides or in the book) to preprocess it. Techniques you can try out include:

- lowercasing
- stopword removal
- stemming and/or lemmatizing)


## Task 2: Extract information

Try to extract meaningful information from your texts. Depending on your interests and the nature of the data, you could:

- use regular expressions to distinguish relevant from irrelevant texts, or to extract substrings
- use NLP techniques such as Named Entity Recognition to extract entities that occur.

You are **very much** encouraged to use your own data for this. Alternatively, you could use the following (huge!) dataset of this year's ICWSM Dataset challenge (see http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=99774&copyownerid=99078)

You can get it like this:

```
cd DIRECTORY-WHERE-YOU-WANT-YOUR-DATA
wget https://dataverse.harvard.edu/api/access/datafile/:persistentId?persistentId=doi:10.7910/DVN/ULHLCB/MWLJVN -o mydata.tar.gz
tar -xzf mydata.tar.gz
```
A subfolder called `articles` will be created. Once all looks good, don't forget to delete the archive again:
```
rm mydata.tar.gz
```

Within Python, you can then use `glob` to get a list of all the files you care about (explore the structure of the directory before!):

```
from glob import glob
infowarsfiles = glob('*/Infowars/*')
infowarsarticles = []
for filename in infowarsfiles:
    with open(filename) as f:
	    infowarsarticles.append(f.read())
```
