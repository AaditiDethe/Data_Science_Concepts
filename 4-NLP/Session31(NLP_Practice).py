
# Practice: 
text='''I purchased it after fit tuber recommended it.
 The shampoo has a good fragrance but it is not that strong to wash 
 away dandruff effectively and hence requires a greater amount 
 to wash the scalp completely . If you are still in doubt whether 
 to purchase it or not ! I would say that you should purchase and 
 after using it you can better decide whether to repurchase it or not .'''
 
import re
def n_gram_extractor(input_str, n):
    tokens=re.sub(r'([^\s\w]|_)+', ' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
n_gram_extractor(text,2)
n_gram_extractor(text,3)

################################
#Extracting the titles
text='''
Review 1: Shampu.
I purchased it after fit tuber recommended it.
The shampoo has a good fragrance but it is not that strong to wash 
away dandruff effectively and hence requires a greater amount 
to wash the scalp completely . If you are still in doubt whether 
to purchase it or not ! I would say that you should purchase and 
after using it you can better decide whether to repurchase it or not.
 
Review 2: Shampu2.
I purchased it after fit tuber recommended it.
The shampoo has a good fragrance but it is not that strong to wash 
away dandruff effectively and hence requires a greater amount 
to wash the scalp completely . If you are still in doubt whether 
to purchase it or not ! I would say that you should purchase and 
after using it you can better decide whether to repurchase it or not.

Review 3: Shampu3.
I purchased it after fit tuber recommended it.
The shampoo has a good fragrance but it is not that strong to wash 
away dandruff effectively and hence requires a greater amount 
to wash the scalp completely . If you are still in doubt whether 
to purchase it or not ! I would say that you should purchase and 
after using it you can better decide whether to repurchase it or not.
'''

pattern='Review \d: ([^\n]*)'
matches=re.findall(pattern, text)
matches

#########################################
text='''
Review : Shampu.
I purchased it after fit tuber recommended it.
The shampoo has a good fragrance but it is not that strong to wash 
away dandruff effectively and hence requires a greater amount 
to wash the scalp completely . If you are still in doubt whether 
to purchase it or not ! I would say that you should purchase and 
after using it you can better decide whether to repurchase it or not.
 
Review : Shampu2.
I purchased it after fit tuber recommended it.
The shampoo has a good fragrance but it is not that strong to wash 
away dandruff effectively and hence requires a greater amount 
to wash the scalp completely . If you are still in doubt whether 
to purchase it or not ! I would say that you should purchase and 
after using it you can better decide whether to repurchase it or not.
'''
pattern='Review :([^\n]*)'
re.findall(pattern, text)
#########################################
'''Session 31'''
#In nltk there is default function ngrams
#For any new function created do 'import re'
from nltk import ngrams
#extract n-grams with nltk
list(ngrams("The cute little boy is playing with kitten".split(),2))
list(ngrams("The cute little boy is playing with kitten".split(),3))

#list(ngrams("The cute little boy is playing with kitten".split(),2))
#Output:
'''[('The', 'cute'),
 ('cute', 'little'),
 ('little', 'boy'),
 ('boy', 'is'),
 ('is', 'playing'),
 ('playing', 'with'),
 ('with', 'kitten')]'''
  
#list(ngrams("The cute little boy is playing with kitten".split(),3))
#Output:
'''[('The', 'cute', 'little'),
 ('cute', 'little', 'boy'),
 ('little', 'boy', 'is'),
 ('boy', 'is', 'playing'),
 ('is', 'playing', 'with'),
 ('playing', 'with', 'kitten')]'''

###########################################
from textblob import TextBlob
blob=TextBlob("The cute little boy is playing with kitten.")
blob.ngrams(n=2)
blob.ngrams(n=3)

#blob.ngrams(n=2)
#Output:
'''[WordList(['The', 'cute']),
 WordList(['cute', 'little']),
 WordList(['little', 'boy']),
 WordList(['boy', 'is']),
 WordList(['is', 'playing']),
 WordList(['playing', 'with']),
 WordList(['with', 'kitten'])]'''
    
#blob.ngrams(n=3)
#Output: 
'''[WordList(['The', 'cute', 'little']),
 WordList(['cute', 'little', 'boy']),
 WordList(['little', 'boy', 'is']),
 WordList(['boy', 'is', 'playing']),
 WordList(['is', 'playing', 'with']),
 WordList(['playing', 'with', 'kitten'])]'''

#########################################
#Tokenization using keras
sentence5='''sharat twitted ,Withnessing 68th republic day 
             India from Rajpath, \ new Delhi,Memorizing performance by 
             Indian Army'''
from keras.preprocessing.text import text_to_word_sequence()
text_to_word_sequence(sentence5)

#########################################
#Tokenization using TextBlob
sentence5='''sharat twitted ,Withnessing 68th republic day 
             India from Rajpath, \ new Delhi,Memorizing performance by 
             Indian Army'''
from textblob import TextBlob
blob=TextBlob(sentence5)
blob.words
#Output:
''' WordList(['sharat', 'twitted', 'Withnessing', '68th', 
'republic', 'day', 'India', 'from', 'Rajpath', 'new', 
'Delhi', 'Memorizing','performance', 'by', 'Indian', 'Army'])'''
    
###########################################
#Tweet Tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)
#Output:
'''Out[81]: 
['sharat',
 'twitted',
 ',',
 'Withnessing',
 '68th',
 'republic',
 'day',
 'India',
 'from',
 'Rajpath',
 ',',
 'ew',
 'Delhi',
 ',',
 'Memorizing',
 'performance',
 'by',
 'Indian',
 '!',
 'Army']'''
###########################################
from nltk.tokenize import MWETokenizer
'''multi-word  tokenizers are essential for tasks where
the meaning of the text heavily depends on the interpretation of
phrases as wholes rather than as sums of individual words.
For instance, in sentiments analysis, recognizing "not good"
as a single negative sentiment unit rather than as "not" 
and "good" separately can significantly affect the outcome'''

sentence5='''sharat twitted ,Withnessing 68th republic day 
             India from Rajpath , \new Delhi,Memorizing performance by 
             Indian ! Army'''
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenize(sentence5.replace('!',' ').split())
mwe_tokenizer.tokenize(sentence5.replace('!','!!').split())
