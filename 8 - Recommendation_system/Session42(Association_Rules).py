
# Association_Ruless

import pandas as pd
# Pandas library for data manipulation   
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

#Sample dataset
transactions = [['Milk','Bread','Butter'],['Bread','eggs'],['Milk','Bread','Eggs','Butter'],['Bread','Eggs','Butter'],['Milk','Bread','Eggs']]

#Step-1: Convert the dataset into a format 
# This dataset need to be converted into one-hot encoded format (1,0 --> item is present not present respectively) in order to apply apriori algorithm
# And we will convert this data with the help of TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns = te.columns_)
# pd.DataFrame(te_ary): Creates a DatFrame from binary array te_ary.
# columns = te.columns_ : This sets the column names of the DataFrame to the item names from the transactions

#Step-2: Apply the Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support = 0.5, use_colnames=True)
# min_support = 0.5: Only interested in itemsets that appear in at least 50% of the transactions
# use_colnames = True : Actually use column names instead of column indices.
# The output is a DataFrame containing the frequent itemsets (item combination)

# Bread appears in 100% transactions
# Egg, Butter, Milk each appears in 60% of transactions.
# The combination also appear in 60% of transactions

#Step-3: Generate association rules from the frequent itemsets
# Now, generating association rules
# Generating association rules based on frequent itemsets.
rules = association_rules(frequent_itemsets, metric = 'lift', min_threshold=1)
# metric='lift': This specifies that we want to calculate the lift of the association rules. 
#  Lift measures how much more likely two items are to be bought together than if they were independent (i.e., bought randomly).

# min_threshold=1:  This tells the algorithm to only return association rules where the lift is 1 or higher, 
# meaning we are only interested in associations that are as likely or more likely than chance.

# Step-4: Output the results
print("Frequent Itemsets: ")
print(frequent_itemsets)

print("\nAssociation Rules: ")
print(rules[['antecedents','consequents','support','confidence','lift']])

###########################################
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Step-1: Simulating healthcare transactions (symptoms/diseases/treatment)
healthcare_data = [
    ['Fever','Cough','COVID-19'],
    ['Cough','Sore Throat','Flu'],
    ['Fever','Cough','Shortness of Breadth','COVID-19'],
    ['Cough','Sore Throat','Flu','Headache'],
    ['Fever','Body Ache','Flu'],
    ['Fever','Cough','COVID-19','Shortness of Breadth'],
    ['Sore Throat','Headache','Cough'],
    ['Body Ache','Fatigue','Flu']
    ]

# Step-2: 
te = TransactionEncoder()
te_ary = te.fit(healthcare_data).transform(healthcare_data)
df = pd.DataFrame(te_ary, columns = te.columns_)
 

#Step-3: Apply the Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support = 0.3, use_colnames=True)

#Step-4: Generate association rules from the frequent itemsets
rules = association_rules(frequent_itemsets, metric = 'confidence', min_threshold=0.7)

# Step-5: Output the results
print("Frequent Itemsets: ")
print(frequent_itemsets)

print("\nAssociation Rules: ")
print(rules[['antecedents','consequents','support','confidence','lift']])

###################################################
# Step-1: Simulate e-commerce transactions
transactions = [
    ['Laptop','Mouse','Keyboard'],
    ['Smartphone','Headphones'],
    ['Laptop','Mouse','Headphones'],
    ['Smartphone','Charger','Phone Case'],
    ['Laptop','Mouse','Monitor'],
    ['Headphones','Smartwatch'],
    ['Laptop','Keyboard','Monitor'],
    ['Smartphone','Charger','Phone Case','Screen Protector'],
    ['Mouse','Keyboard','Monitor'],
    ['Smartphone','Headphones','Smartwatch']]

# Step-2: 
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns = te.columns_)
 

#Step-3: Apply the Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support = 0.2, use_colnames=True)

#Step-4: Generate association rules from the frequent itemsets
rules = association_rules(frequent_itemsets, metric = 'confidence', min_threshold=0.5)

# Step-5: Output the results
print("Frequent Itemsets: ")
print(frequent_itemsets)

print("\nAssociation Rules: ")
print(rules[['antecedents','consequents','support','confidence','lift']])
