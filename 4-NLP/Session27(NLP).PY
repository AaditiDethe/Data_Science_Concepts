
#Removing Special Characters
'''Special characters --> non-alphanumeric characters,often found in 
comments, references, currency number, etc.
regex 101.com
'''
import re
chat1='Hello, I am having an issue with my order #412889912'
pattern ='order[^\d]*(\d*)'
matches=re.findall(pattern,chat1)
matches

import re
chat1='Hello, I am having an issue with my order # 412889912'
pattern ='order[\d*]'
matches4=re.findall(pattern,chat1)
matches4

chat1='Hello, I am having an issue with my order #412889912'
pattern ='order[^\d]*(\d)'
matches=re.findall(pattern,chat1)
matches

chat2='I have a problem with my order number 412889912'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
matches

import re
chat2='I have a problem with my order number # 412889912'
pattern='order[^\d]'
matches=re.findall(pattern,chat2)
matches
pattern='order[^\d]'
matches2=re.findall(pattern,chat2)
matches2

###################################################################
import re
chat3='My order 412889912 9845040 is having an issue, I was charged 237482'
pattern='[^\d]*(\d)'
matches1=re.findall(pattern,chat3)
matches1

import re
chat3='My order 412889912 9845040 is having an issue, I was charged 237482'
pattern='[^\d]*(\d*)'
matches1=re.findall(pattern,chat3)
matches1
