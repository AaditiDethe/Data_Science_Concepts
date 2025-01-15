
import re
chat1='Hello, I am having an issue with my order # 412889912'
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d)',chat1)

import re
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
'''
#strip=remaining lines are getting strip out
get_pattern_match(r'age (\d+)',text)
get_pattern_match(r'Born(.*)\n',text).strip()
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
get_pattern_match(r'\(age.*\n(.*)',text)

def extract_personal_information(text):
    age=get_pattern_match('age (\d+)',text)
    full_name=get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match('\(age.*\n(.*)',text)
    return{
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_information(text)
#####################################################
import re
chat1='Hello, I am having an issue with my order # 412889912'
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d)',chat1)

text='''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 67)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''

get_pattern_match(r'age (\d+)',text)
#Output: '67'
get_pattern_match(r'Born(.*)\n',text).strip()
#Output: 'Mukesh Dhirubhai Ambani'
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
#Output: '19 April 1957'
get_pattern_match(r'\(age.*\n(.*)',text)
#Output: 'Aden, Colony of Aden'

def extract_personal_information(text):
    age=get_pattern_match('age (\d+)',text)
    full_name=get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match('\(age.*\n(.*)',text)
    return{
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_information(text)
#OUTPUT: 
'''{'age': 67,
     'name': 'Mukesh Dhirubhai Ambani',
     'birth_date': '19 April 1957',
     'birth_place': 'Aden, Colony of Aden'}'''
#####################################################
from PyPDF2 import PdfFileReader
#importing required modules
from PyPDF2 import PdfReader

#creating a pdf reader object
reader=PdfReader('c:/1-python/kopargaon-part-1.pdf')
#printing the number of pages
print(len(reader.pages))

#getting the specific page from the pdf file
page=reader.pages[2]

#extracting text from page
text=page.extract_text()
print(text)
      