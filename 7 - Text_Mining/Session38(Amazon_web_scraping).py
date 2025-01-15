# Amazon_web_scraping

import bs4
from bs4 import BeautifulSoup as bs
import requests
page=requests.get("https://www.amazon.com/Elon-Musk-SpaceX-Fantastic-Future-ebook/dp/B00KVI76ZS/ref=sr_1_4?crid=GTVMFX8FDDEY&dib=eyJ2IjoiMSJ9.5NB32a37A5nPyBaGn4c2Yv62OYzwo7JBRcDsZOHTOC4AZJPrb0txCAJjNV5aSnj124THzO6a2NWBAYki_y8bQp5CahA2d4e5zoDvgfjqaG2C3u4YZXmqbIfcH6l45XezDucJBAr1xczKneljIVn7yEuU8FCiutHqel2PWaj7TlkU5R-R3qJT3sSv-ZGDawQvOESyDl-KC5Fp0as40phwRoJKDEcOfWySbG3bb1tvtlU.O9ptINTjyHf8NYecKubeopn-6U0sScLDqiiXa-l7KOM&dib_tag=se&keywords=elon+musk&qid=1725392334&s=digital-text&sprefix=elon+mus%2Cdigital-text%2C426&sr=1-4")
page
page.content
soup=bs(page.content,"html.parser")
print(soup.prettify)
########################################################
<div class="a-section a-spacing-small a-spacing-top-medium"><h3 class="a-size-base-plus a-color-base a-text-bold">Customers say</h3></div>
<h3 class="a-size-base-plus a-color-base a-text-bold">Customers say</h3>
title=soup.find_all('span',class_="a-spacing-small")
title
review_title=[]
for i  in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
review_title[:]=[title.strip('\n') for title in review_title]
review_title
len(review_title)


#########
#now let us scrap rating
rating=soup.find_all('span',class_='rating-other-user-rating')
rating
rate=[]
for i  in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
rate[:]=[r.strip('\n\n\n\n\n\n') for r in rate]
rate=[r.replace('/10', '') for r in rate]
rate
len(rate)
rate.append('')
rate.append('')
len(rate)


#Let us scrap the review body
review=soup.find_all('div',class_='text show-more__control')
review
review_body=[]
for i  in range(0,len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)

#create a dataframe
import pandas as pd
df=pd.DataFrame()
df['Review_title']=review_title
df['Rate']=rate
df['Review']=review_body
df
######################
#now create csv file
df.to_csv("C:/8-text_mining/IMDb_reviews1.csv",index=True)
########

#Sentiment Analysis
import pandas as pd
from textblob import TextBlob
sent="This is very excellent garden"
pol=TextBlob(sent).sentiment.polarity
pol
df=pd.read_csv("C:/8-text_mining/IMDb_reviews1.csv")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']