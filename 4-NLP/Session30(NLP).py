
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

##################################################
import re
sentence5='''sharat twitted ,Withnessing 68th republic day 
             India from Rajpath, \new Delhi,Memorizing performance by 
             Indian Army'''
re.sub(r'([^\s\w]|_)+', ' ',sentence5).split()
#Output: 
'''['sharat',
 'twitted',
 'Withnessing',
 '68th',
 'republic',
 'day',
 'India',
 'from',
 'Rajpath',
 'ew',
 'Delhi',
 'Memorizing',
 'performance',
 'by',
 'Indian',
 'Army']'''

#Difference '\new' and '\ new':
import re
sentence5='''sharat twitted ,Withnessing 68th republic day 
             India from Rajpath, \ new Delhi,Memorizing performance by 
             Indian Army'''
re.sub(r'([^\s\w]|_)+', ' ',sentence5).split()
#Output:
'''['sharat',
     'twitted',
     'Withnessing',
     '68th',
     'republic',
     'day',
     'India',
     'from',
     'Rajpath',
     'new',
     'Delhi',
     'Memorizing',
     'performance',
     'by',
     'Indian',
     'Army']'''

#########################################
###extracting n-grams
#n-gram can be extracted using three techniques
#1.custom defined function
#2.NLTK
#3.TextBlob

#########################################
#Extracting n-grams using custom defined function

import re
def n_gram_extractor(input_str, n):
    tokens=re.sub(r'([^\s\w]|_)+', ' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
n_gram_extractor("The cute little boy is playing with kitten",2)
n_gram_extractor("The cute little boy is playing with kitten",3)

#n_gram_extractor("The cute little boy is playing with kitten",2)
#Output:
'''['The', 'cute']
['cute', 'little']
['little', 'boy']
['boy', 'is']
['is', 'playing']
['playing', 'with']
['with', 'kitten']'''

#n_gram_extractor("The cute little boy is playing with kitten",3)
#Output:
'''['The', 'cute', 'little']
['cute', 'little', 'boy']
['little', 'boy', 'is']
['boy', 'is', 'playing']
['is', 'playing', 'with']
['playing', 'with', 'kitten']'''

###########################################
from nltk import ngrams
#extraction n-grams with nltk
list(ngrams("The cute little boy is playing with kitten".split(),2))

#############################################
#1.Extract all twitter handles from following text:
text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern='https://twitter.com/([a-zA-Z0-9_]+)'

re.findall(pattern, text)
#Output:['elonmusk', 'teslarati', 'dummy_tesla', 'dummy_2_tesla']

#############################################
#2.Extract Concentration Risk Types. It will be a text that appears
text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, 
prospects, financial condition and operating results.'''

pattern='Concentration of Risk: ([^\n]*)'
re.findall(pattern, text)
#Output: ['Credit Risk', 'Supply Risk']

#another example 
text = '''
Student name: Aaditi Dethe 
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Student name: Ishwari Deshmukh 
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, 
prospects, financial condition and operating results.'''

pattern='Student name: ([^\n]*)'
re.findall(pattern, text)
#Output: ['Aaditi Dethe ', 'Ishwari Deshmukh ']

###############################################
#Companies in europe reports their financial numbers of semi annual basis 
#and you can have a document like this. To extract quarterly and semin annual
#period you can use a regex as shown below.

text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''

pattern='FY(\d{4} (?:Q[1-4]|S[1-2]))'
#  ?: match this and | a or b
matches=re.findall(pattern, text)
matches
#Output: ['2021 Q1', '2021 S1']

###############################################
import re
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''

pattern='\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches=re.findall(pattern, text)
matches
#Output: ['9991116666', '(999)-333-7777']

##############################################
text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.

Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''

pattern='Note \d - ([^\n]*)'
matches=re.findall(pattern, text)
matches
#Output: ['Overview', 'Summary of Significant Accounting Policies']

#########################################
#Extract financial periods from a company's financial reporting
text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 Q4 was $8 billion.
'''

pattern='FY\d{4} Q[1-4]'

matches=re.findall(pattern, text)
matches
#Output: ['FY2021 Q1', 'FY2021 Q4']

########################################
#Case insensitive pattern match using flags
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''

pattern='FY\d{4} Q[1-4]'

matches=re.findall(pattern, text, flags=re.IGNORECASE)
matches
#Output: ['FY2021 Q1', 'fy2020 Q4']