# -*- coding: utf-8 -*-

from glob import glob
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics

reviews=[]
test=[]

print("Constructing training dataset")

for file in glob ("/home/damian/aclImdb/train/pos/*.txt"):
    with open(file) as fi:
        reviews.append((fi.read(),1))
nopostr=len(reviews)

print ("Added",nopostr,"positive reviews")  

for file in glob ("/home/damian/aclImdb/train/neg/*.txt"):
    with open(file) as fi:
        reviews.append((fi.read(),-1))
nonegtr=len(reviews)-nopostr
print ("Added",nonegtr,"negative reviews")  
  
   
print("Constructing test dataset")

for file in glob ("/home/damian/aclImdb/test/pos/*.txt"):
    with open(file) as fi:
        test.append((fi.read(),1))
noposte=len(test)
print ("Added",noposte,"positive reviews")  

for file in glob ("/home/damian/aclImdb/test/neg/*.txt"):
    with open(file) as fi:
        test.append((fi.read(),-1))
nonegte=len(test)-noposte
print ("Added",nonegte,"negative reviews")  
    
    
#%% Training and testing classifier                

print("Training classifier...")        

# Generate BOW representation of word counts
vectorizer = CountVectorizer(stop_words='english')
train_features = vectorizer.fit_transform([r[0] for r in reviews])
test_features = vectorizer.transform([r[0] for r in test])

# Fit a naive bayes model to the training data.
nb = MultinomialNB()
nb.fit(train_features, [r[1] for r in reviews])

# Now we can use the model to predict classifications for our test features.
predictions = nb.predict(test_features)
actual=[r[1] for r in test]

# Compute the error.  It is slightly different from our model because the internals of this process work differently from our implementation.
fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
print("Multinomal naive bayes AUC: {0}".format(metrics.auc(fpr, tpr)))


#%% Now, let's play around:
newdata=vectorizer.transform(["What a crappy movie! It sucks!",
                              "This is awsome. I liked this movie a lot, fantastic actors",
                              "I would not recomment it to anyone.",
                              "Enjoyed it a lot"])
predictions = nb.predict(newdata)
print(predictions)