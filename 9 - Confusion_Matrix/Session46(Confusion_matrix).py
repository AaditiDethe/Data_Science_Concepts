
import numpy as np
import matplotlib.pyplot as plt

# Target value (true value)
true_value = 50

# Simulate data
# 1. Accurate and Precise (close to true value and tightly grouped)

'''
loc = true_value (True_value = 50): The values will be centered around the 
true value (50).
scale = 1: The standard deviation (spread) is small, meaning the values will
be tightly grouped around the true value.
This implies the high precision.
The measurement will vary only a little from the true value, so they'll be 
both accurate (close to 50) and precise (close to each other).
'''

accurate_precise = np.random.normal(loc = true_value, scale=1, size=10)

# 2. Accurate but not Precise (close to true value but spread out)
accurate_not_precise = np.random.normal(loc = true_value, scale=10, size=10)

'''
The two lines of code which you have highlighted may look similar, but 
they differ in one important aspect: the value of scale, which controls
the spread of the generated values around the true value (loc)
'''

# 3. Precise but not accurate (far from true value but tightly grouped )
# Standard Deviation is low
precise_not_accurate = np.random.normal(loc = 70, scale = 1, size = 10)

# 4. Neither accurate nor precise (far from true value and spread out)
not_accurate_not_precise = np.random.normal(loc = 70, scale = 10, size = 10)

#Plotting the results:
plt.figure(figsize=(10,6))

# Plot 1: Accurate and Precise
plt.scatter(accurate_precise, [1]*10, color = 'green', label = 'Accurate and Precise')

# Plot 2: Accurate but not Precise
plt.scatter(accurate_not_precise, [2]*10, color = 'blue', label = 'Accurate but Not Precise')

# Plot 3: Precise but not Accurate
plt.scatter(precise_not_accurate, [3]*10, color = 'orange', label = 'Precise but not Accurate')

# Plot 4: Not Accurate not Precise
plt.scatter(not_accurate_not_precise, [4]*10, color = 'red', label = 'Not Accurate not Precise')

# Adding target line
plt.axvline(true_value, color = 'black', linestyle = '--', label = 'True Value')

# Labels and legend
plt.yticks([1,2,3,4], ['Accurate and Precise','Accurate but not Precise','Precise but not Accurate','Neither Accurate nor Precise'])
plt.xlabel('Measurement Value')
plt.legend()
plt.title('Accuracy and Precision Demonstration')




