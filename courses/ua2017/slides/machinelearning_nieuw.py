#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from glob import glob
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics

reviews=[]
test=[]

print("Constructing training dataset")

# glob gives you a list of filenames that match a specific criterion
# in this case, all .txt-files in the postivie training folder

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


#%% Checking the data
# Thus, we got two lists, reviews and test.
# Both contain tuples (pairs of two values: The first is the review, 
# the second the classification: 1 or -1)
    
# We can easiliy verify this by looking at a random entry:
print(reviews[244])
# or
print('The following review\n\n\n',reviews[244][0],"\n\n\nis evaluated as",reviews[244][1])
    
#%% Training the classifier                

print("Training classifier...")        

# Generate BOW representation of word counts
vectorizer = CountVectorizer(stop_words='english')   #alternatively, you could provide a list of stop words
train_features = vectorizer.fit_transform([r[0] for r in reviews])
test_features = vectorizer.transform([r[0] for r in test])

# Fit a naive bayes model to the training data.
nb = MultinomialNB()
nb.fit(train_features, [r[1] for r in reviews])


#%% testing the classifier
# Now we can use the model to predict classifications for our test features.
predictions = nb.predict(test_features)
# and also put the 'true' results from the test dataset in a list
actual=[r[1] for r in test]

# now we can compare whether the predicted values and the actual values match.
# We could write the output to a tab seperated file to see what matches:
with open("/home/damian/agreement.tab", mode='w') as fo:
    fo.write("actual\tpredicted\tfirst words\n")
    for i in range(len(predictions)):
        fo.write(str(actual[i])+"\t"+str(predictions[i])+"\t"+test[i][0][:50]+"\n")

# That can be helpful for inspecting where sth goes wrong, but we can better 
# just calculate some measures of performance immediately here:

# lets start with the AUC:

fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
print("Multinomal naive bayes AUC: {0}".format(metrics.auc(fpr, tpr)))


# %% Some more metrics to evaluate the performance


print('Accuracy:')
print(metrics.accuracy_score(actual,predictions,normalize=True))

print('Precision:')
print(metrics.precision_score(actual,predictions,pos_label='1', labels = ['-1','1']))
print('Recall:')
print(metrics.recall_score(actual,predictions,pos_label='1', labels = ['-1','1']))

# note that Precision is not a symmetric measure (look back at the slides!), if we want
# the precision for retrieving a NEGATIVE review instead of a positive we get a different value:

print('\t side note: Precision if we are interested in retrieving negative reviews:')
print('\t',metrics.precision_score(actual,predictions,pos_label='-1', labels = ['-1','1']))
print('\t side note: Recall if we are interested in retrieving negative reviews:')
print('\t',metrics.recall_score(actual,predictions,pos_label='-1', labels = ['-1','1']))

# back to normal


print('F1-score:')
print(metrics.f1_score(actual,predictions,pos_label='1', labels = ['-1','1']))
print('Confusion matrix:')
print(metrics.confusion_matrix(actual,predictions))


#%% Now, let's play around and see how well it would work on new unseen data:
newreviews=["What a crappy movie! It sucks!",
            "This is awsome. I liked this movie a lot, fantastic actors",
            "I would not recomment it to anyone.",
            "Enjoyed it a lot"]
newdata=vectorizer.transform(newreviews)
predictions = nb.predict(newdata)
print(predictions)
for i in range(len(predictions)):
    if predictions[i]==1:
        print(newreviews[i],'\nis probably about a GOOD movie\n')
    elif predictions[i]==-1:
        print(newreviews[i],'\nis probably about a BAD movie\n')

# COOL, ISN'T IT???
   

#%% We started with a Naive Bayes classifier, but there are others
# let's see if another one works better, for example logistic regression or 
# a support vector machine.


# about the difference between NB en Logistic regression:
# https://www.quora.com/What-is-the-difference-between-logistic-regression-and-Naive-Bayes?share=1
# (basically, in NB all IV's are assumed to be uncorrelated)
# LR 



# logistic regression:
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(train_features, [r[1] for r in reviews])
predictions = logreg.predict(test_features)
# we could get more info, see http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
#predictionsproba = logreg.predict_proba(test_features)
#print([j for i in logreg.coef_ for j in i])


# It's always a good idea to compare several classifiers and take the one
# that performs best!



#%% SVM (took to long for practical use on my machine):
# for more info, see http://scikit-learn.org/stable/modules/svm.html#

#from sklearn import svm
#clf = svm.SVC()
#clf.fit(train_features, [r[1] for r in reviews])
#predictions = clf.predict(test_features)


#%% Other BOW-representatons
# We used a BOW representation of word freeuency counts
# from sklearn.feature_extraction.text import CountVectorizer
# vectorizer = CountVectorizer(stop_words='english')
# But maybe our classifier can be improved by using a TfIdf-Vectoryizer
# for details see http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer(stop_words='english')
train_features = vectorizer.fit_transform([r[0] for r in reviews])
test_features = vectorizer.transform([r[0] for r in test])
logreg = LogisticRegression()
logreg.fit(train_features, [r[1] for r in reviews])
predictions = logreg.predict(test_features)
