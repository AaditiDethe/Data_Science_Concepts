
#Suppose we want to replace words in string
sentence2="I visited MY from IND on 14-02-19"
normalized_sentence=sentence2.replace("MY","Malaysia").replace("IND","India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)

#When the words repeat
sentence3="I visited MY from IND on 14-02-19 to MY"
normalized_sentence=sentence3.replace("MY","Malaysia").replace("IND","India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)

sentence3="I visited MY from IND on 14-02-19 to MY"
normalized_sentence=sentence3.replace("MY","Malaysia").replace("IND","India")
normalized_sentence=sentence3.replace("MY","Mom")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)

sentence3="I visited MY from IND on 14-02-19 to MY"
normalized_sentence=sentence3.replace("MY","Malaysia").replace("IND","India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
normalized_sentence1=normalized_sentence.replace("MY","Mom")
print(normalized_sentence1)

##########################################
#Suppose we want auto correction in the sentence
from autocorrect import Speller
#declare the function Speller defined for English
spell=Speller(lang='en')
spell("Engilish")
spell("engllish")
spell("Indai")
spell("marrthi")

spell=Speller(lang='ma')
spell("marrathi")
spell('Marrthi')

spell=Speller(lang='Ma')
spell('Marrthi')

spell=Speller(lang='en')
spell("endiuwe")

###########################################
#Suppose we want to correct whole sentence
import nltk
nltk.download('punkt')
from nltk import word_tokenize
sentence3='''Naaturla laguange processin delas withhh the artt fo ecxtarting senttiiments'''
#let us first tokenize this sentence
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word) for word in sentence3])
print(corrected_sentence)

###########################################
##Stemming
'''Process of removing 'ing','ed', 'ly' '''
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("Jumping")
stemmer.stem("Jumped")
stemmer.stem("Lively")

###########################################
#Lemmatizer
'''Looks into dictionary words --> mapping all words into 1 word'''
import nltk
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("programmed")
lemmatizer.lemmatize("programs")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")

###########################################
#Chunking
'''(Shallow Parsing) Identifying named entities'''
import nltk
from nltk import word_tokenize
nltk.download("maxent_ne_chunker")
nltk.download('words')
sentence4="We are learning NLP in python by SanjivaniAI"
#first we will tokenize
nltk.download('averaged_perceptron_tagger')
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]

###########################################
#Sentence tokenization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("We are learning NLP in Pyhton. Delivered by SanjivaniAI")
sent
#OUTPUT : 
'''['We are learning NLP in Python.','Delivered by SanjivaniAI']'''

###########################################
#He went to bank and checked account it was almost 0 
#looking this he went to river bank and was crying
from nltk.wsd import lesk
sentence1="Keep your saving in the bank"
print(lesk(word_tokenize(sentence1),'bank'))
#OUTPUT : Synset('savings_bank.n.02')
sentence2="It is so risky to drive over the banks of river"
print(lesk(word_tokenize(sentence2),'bank'))
#OUTPUT : Synset('bank.v.07')