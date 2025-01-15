
# Naive Bayes Classification Algorithm

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

### Loading the dataset
email_data = pd.read_csv("C:/Naive Bayes Classification/sms_raw_NB.csv", encoding="ISO-8859-1")

#these sms are in text form , open the data frame and there are ham or spam mail
#cleaning the data 
#the function toknizes the text and remove words
#with fewer than 4 characters

import re

def cleaning_text(i):
    i=re.sub("[^A-Z a-z]+ "," ",i).lower()
    w=[]
    # every thing else A to Z and a to z  is going to convert to space and
    # we will take each row and tokenize
    for word in i.split(""):
        if len(word)>3:
            w.append(word)
    return(" ".join(w))
# testing above function with sample text
    cleaning_text("Hope you are having good week. just checking")
    cleaning_text("hope i can i understand your feeling12321.123.hi how are")
    cleaning_text("hi how are you")
# note the dataframe size is 5559, 2, now removing empty spaces
# remove empty rows

email_data = email_data.loc[email_data.text != "",:]
email_data.shape
# you can yous count vectorizer which directly convert the collection of document

# first we will split the data 
from sklearn.model_selection import train_test_split
email_train, email_test = train_test_split(email_data,test_size=0.2)

#split each email into a list of words 
# creating matrix of cout for entire dataframe
def split_into_words(i):
    return[word for word in i.split(" ")]
# define the preparation of the email text into word count matrix format
# CountVectorize : converts the email into a matrix of token counts.
# .fit(): Learns the vocabulary from the text data
# .tranform () convert text data into a token count matrix

email_bow = CountVectorizer(analyzer=split_into_words).fit(email_data.text)

# define BOW for all data frames 

all_emails_matrix = email_bow.transform(email_data.text)
train_email_matrix = email_bow.transform(email_train.text)

# for testing message

test_email_matrix = email_bow.transform(email_test.text)

# learning term weighting and normalizing entire emails

tfidf_transformer = TfidfTransformer().fit(all_emails_matrix)

#preparing tfidf for the emails

train_tfidf = tfidf_transformer.transform(train_email_matrix)
train_tfidf.shape

test_tfidf = tfidf_transformer.transform(test_email_matrix)
test_tfidf.shape

# Now apply to naive bayes Algorithm

from sklearn.naive_bayes import MultinomialNB as MB
classifier_mb = MB()

classifier_mb.fit(train_tfidf, email_train.type)

# email_train.type : this is the column in training dataset
# (email_train ) that contains the target labels
# which specify wheather each message is spam or ham (non - spam).
# the .type attibute refers to that specific column
# in the email_train datframe
# training data prepared in term of tfidf and
# labels of corresponding training data

test_pred_m = classifier_mb.predict(test_tfidf)

# calculate accuracy 
accuracy_test_m = np.mean(test_pred_m == email_test.type)
accuracy_test_m

# Evaluation on test data accuracy matrix

from sklearn.metrics import accuracy_score
accuracy_score(test_pred_m, email_test.type)
pd.crosstab(test_pred_m, email_test.type)

# traing  data accuracy
train_pred_m = classifier_mb.predict(train_tfidf)
# calculate accuracy 
accuracy_train_m = np.mean(train_pred_m == email_train.type)
accuracy_train_m

# test data( with Laplace Smoothing ): This accuracy is
# computed after applying Laplace smoothing (with alph = 3)
# to the Naive Bayes model.

# Interpretation : smoothing helps avoid issues when encountering 
# words in the text data that were not seen in the training data 
# (zero -frequncy problem)

classifier_mb_lab = MB(alpha= 3)
classifier_mb_lab.fit(train_tfidf, email_train.type)
# accuracy after tunning 

test_pred_lab = classifier_mb_lab.predict(test_tfidf)
accuracy_test_lab = np.mean(test_pred_lab == email_test.type)
accuracy_test_lab
accuracy_score(test_pred_lab, email_test.type)

from sklearn.metrics import accuracy_score

accuracy_score(test_pred_lab, email_test.type)
pd.crosstab(test_pred_lab, email_test.type)

# training data aacuracy
train_pred_lab = classifier_mb_lab.predict(train_tfidf)
accuracy_train_lab = np.mean(train_pred_lab)