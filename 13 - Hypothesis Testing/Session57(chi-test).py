import pandas as pd
import numpy as np
import scipy
from scipy import stats

'''p is high, null fly
   p is low, null go'''
# Chi-square test

# Objective : is defective proportions are independent of the country?
# The dataset contains two columns:
    
# Defective: Indicates whether an item is defective (likely binary, with 1 
# for defective and 0 for not defective).

# Country : Specifies the country associated with the item

# The dataset has 800 entries, and there are no missing values in either column.
# It appears to be designed to analyse defect rates across different 
# countries, which aligns with the chi-square test you performed earlier
# to determine if defectiveness is independent of the country.

Bahaman = pd.read_excel("C:/Data Science/Assignment Data/Bahaman.xlsx")

# Cross Tabulation
count = pd.crosstab(Bahaman["Defective"], Bahaman["Country"])
count
# Chi-square test
chi2_result = scipy.stats.chi2_contingency(count)
print("Chi-square Test:", chi2_result)

#Output:
'''Chi-square Test: Chi2ContingencyResult(statistic=1.7243932538050184, pvalue=0.6315243037546223, dof=3, expected_freq=array([[178.75, 178.75, 178.75, 178.75],
           [ 21.25,  21.25,  21.25,  21.25]]))'''
# we accept null hypothesis
# Conclusion: Defective proportions are independent of the country.
