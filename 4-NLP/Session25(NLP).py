
#Python for NLP-Natural Language Processing
'''NLP techniques
1.Rules
2.Machine Learning 
3.Deep Learning

Feature Engineering :It is the process of extracting features from raw data'''

######Text mining######
sentence="we are learning TextMining from Sanjivani AI"
#if we want to know position of learning
sentence.index("learning")
#it will show learning is at position 7
sentence.index("AI")
#index starting from 0 to n

#we want to know position TextMining word
sentence.split().index("TextMining")
#it will show at 3
#["we","are",...]-->tokenization chop the words into token
#it will split the words in list and count the position
sentence.split().index("from")

#######################################
#Suppose we want print any word in reverse order
sentence.split()[2][::-1]
#[start:end end:-1(start)] will start from -1,-2,-3
#learning will be printed as gninrael

#######################################
#Suppose want to print first and last word of the sentence
word=sentence.split()
word
#first it will do tokenization
first_word=word[0]
first_word
last_word=word[-1]
last_word
#now we want to concatinate these two words
print(first_word,last_word)
print(first_word+last_word)
print(first_word+" "+ last_word)
concat_word=first_word+" "+ last_word
concat_word

######################################
#We want to print even words from the sentences
[word[i] for i in range(len(word)) if i%2==0]
#word having odd length will not be printed

######################################
sentence
#now we want to display only AI
sentence[-2:]
#it will start from -2,-1 i.e.AI

######################################
#Suppose we want to display entire sentence in reverse order
sentence[::-1]
#OUTPUT : IA inavijnaS morf gniniMtxeT gninrael era ew

######################################
#Suppose we want to select each word and print it reversed order
word
print(" ".join(word[::-1] for word in word))

#Tokenization
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize("I am reading NLP Fundamentals")
words

#####################################
#parts of speech (PoS) tagging
import nltk
nltk.download('punkt')
from nltk import word_tokenize
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
#it is going to mention parts of speech

####################################
#Stop words from NLTK library
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words=stopwords.words('English')
#179 stop words
print(stop_words)
#OUTPUT : 
'''['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 
'ourselves', 'you', "you're", "you've", "you'll", 
"you'd", 'your', 'yours', 'yourself', 'yourselves', 
'he', 'him', 'his', 'himself', 'she', "she's", 'her', 
'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 
'them', 'their', 'theirs', 'themselves', 'what', 'which', 
'who', 'whom', 'this', 'that', "that'll", 'these', 'those',
 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 
 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 
 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 
 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 
 'against', 'between', 'into', 'through', 'during', 'before', 
 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 
 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 
 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 
 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 
 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
 "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 
 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', 
 "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 
 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 
 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', 
 "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 
 'wouldn', "wouldn't"]'''
    
