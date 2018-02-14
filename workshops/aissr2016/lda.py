from gensim import corpora, models
from glob import glob
from nltk.corpus import stopwords
import re

NTOPICS = 50
LDAOUTPUTFILE="topicscores.tsv"
STOPW=set(stopwords.words("english"))

texts=[]
beginfulltext=[]
for file in glob ("/home/damian/aclImdb/train/pos/*.txt"):
    with open(file) as fi:
        inp=re.sub(r"<.*?>"," ",fi.read()).lower()   #remove html tags
        beginfulltext.append(inp[:100])
        texts.append([w for w in inp.split() if w not in STOPW])

# Create a BOW represenation of the texts
id2word = corpora.Dictionary(texts)
mm =[id2word.doc2bow(text) for text in texts]

# Train the LDA models.
lda = models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=NTOPICS, alpha="auto")

# Print the topics.
for top in lda.print_topics(num_topics=NTOPICS, num_words=5):
    print ("\n",top)

print ("\nFor further analysis, a dataset with the topic score for each document is saved to",LDAOUTPUTFILE)

scoresperdoc=lda.inference(mm)

i=0
with open(LDAOUTPUTFILE,"w",encoding="utf-8") as fo:
    for row in scoresperdoc[0]:
        fo.write(str(i))
        fo.write("\t")
        fo.write(beginfulltext[i])
        fo.write("\t")        
        fo.write("\t".join(["{:0.3f}".format(score) for score in row]))
        fo.write("\n")
        i+=1
