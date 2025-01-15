
# Scrapping or scrabbing
#GodFather_review

import bs4
from bs4 import BeautifulSoup as bs
import requests
link="https://m.imdb.com/title/tt0068646/reviews?ref_=tt_urv"
page =requests.get(link)
page
page.content
soup=bs(page.content,'html.parser')
print(soup.prettify())
# prettify() = filtering the content or data
####################################################################################

title=soup.find_all('span',class_="sc-16ede01-2 cXDzZC")
title
review_title=[]

for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title

review_title[:]=[title.strip('\n') for title in review_title]
review_title

len(review_title)

# we got 25 review titles
# Now let us scrap rating
# rating = soup.find_all('svg',class_='ipl-icon ipl-star-icon')
rating = soup.find_all('span',class_='point-scale')
rating
rate = []
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
rate[:]=[r.strip('/') for r in rate]
rate
len(rate)
rate.append('')
rate.append('')
len(rate)
rate.pop(1)
####################################################
# now let us scrapp the review body
review=soup.find_all('div',class_='text show-more_control')
review
review_body=[]
for i in range(0,len(review)):
    review_body.append(review[i].get_text())
    
review_body.append(20)
len(review_body)
# we got 25 review_body
# now we have to save the data in csv file
import pandas as pd 
df=pd.DataFrame()
df['Review_Title']=review_title
df['rate']=rate
df['Review']=review_body
df

################################################################
# To create .csv file
df.to_csv("C:/8-text_mining/GodFather_review.csv")

################################################################
# Sentiment analysis
import pandas as pd
from textblob import TextBlob
sent="This is very excellent garden"
pol=TextBlob(sent).sentiment.polarity
pol
df=pd.read_csv("C:/8-text_mining/GodFather_review.csv")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
  


