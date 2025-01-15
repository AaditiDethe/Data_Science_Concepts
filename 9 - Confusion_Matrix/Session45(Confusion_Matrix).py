
# Confusion Matrix:
''' 1. A confusion matrix is a performance measurement tool used to evaluate the
    accuracy of a classification algorithm. 
   2. It provides a summary of the prediction results on a classification problem
     by showing the comparison between the actual labels and the predicted 
     labels.

Structure of a Confusion Matrix:
                    Predicted Positive	Predicted Negative
    Actual Positive	True Positive (TP)	False Negative (FN)
    Actual Negative	False Positive (FP)	True Negative (TN)


Key Metrics Derived from the Confusion Matrix:
Accuracy: (TP + TN) / (TP + TN + FP + FN) – It is the overall correctness of 
         the model.
Precision: TP / (TP + FP) – The proportion of correct positive predictions
          out of total predicted positives.
Recall (Sensitivity): TP / (TP + FN) – The proportion of actual positives that 
                     are correctly identified.
F1-Score: 2 * (Precision * Recall) / (Precision + Recall) – The harmonic mean 
             of precision and recall.
Specificity: TN / (TN + FP) – The proportion of actual negatives that are 
            correctly identified.


Confusion matrices are particularly useful in identifying where the model is
 making errors and whether those errors are false positives or false negatives. 
 They are especially important in imbalanced datasets where accuracy alone can 
 be misleading.'''
 
# More Standard deviation less precision

import numpy as np

# Let's define a true value that we want to measure
# We first define the true value of 50. This is the reference point.
true_value = 50

# Simulate some measurements
# Accurate but not precise (close to true value but spread out)

'''
Simulating Measurements
We simulate two sets of measurements:
    
Accurate but Not precise: These values are centered around the true value(50),
                          but there is some spread (random variation).
                          
                          This simulates measurements that are accurate 
                          (close to the true value) but not precise (spread out).
'''

accurate_measurements = np.random.normal(loc = true_value, scale = 5, size=10)

# Precise but not accurate  ( far from true value but tightly grouped)
'''
Precise but Not Accurate:
    These values are tightly clustered around 60, not near the true value of 50.
    This simulates measurements that are precise (closely grouped) but not 
    accurate (far from the true value).'''
    
precise_measurements = np.random.normal(loc=60, scale=1, size=10)

# Function to calculate accuracy
'''
We calculate the mean (average) of the measurements. Then, we calculate how close
this average is to the true value.
The closer the average is to the true value, the higher the accuracy.
The accuracy formula is 1-(difference/true_value).
This gives a number between 0 (low accuracy) and 1 (high accuracy)
'''

def calculate_accuracy(measurements, true_value):
    # Accuracy: How close the average measurements is to the true value
    average_measurement = np.mean(measurements)
    accuracy = 1-abs(average_measurement - true_value)/true_value
    return accuracy

# Function to calculate precision:
'''
Precision is determined by the standard deviation of the measurements.
Standard deviation measures how spread out the measurements are.
If the Standard deviation is small (measurements are close together),
precision will be high. We use 1/std_dev to represent precision, so a smaller
spread gives a higher value for precision.'''

def calculate_precision(measurements):
    # Precision: How close the measurements are close to each other
    #(low standard deviation means high precision)
    precision = 1/np.std(measurements) # High Standard deviation
    # means lower precision, so we invert it
    return precision

# Calculate accuracy and precision for both the sets
'''
Accurate Measurements: We calculate the accuracy and precision of the 
                measurements that are close to the true value but spread out.

Precise Measurements: We calculate the accuracy and precision of the 
              measurements that are closely grouped but for from the true value.
              '''
              
accuracy_of_accurate = calculate_accuracy(accurate_measurements, true_value)
precision_of_accurate = calculate_precision(accurate_measurements)

accuracy_of_precise = calculate_accuracy(precise_measurements, true_value)
precision_of_precise = calculate_precision(precise_measurements)

# Print  the results
print("Accurate but Not Precise Measurements:")
print(f"Measurements: {accurate_measurements}")
print(f"Accuracy: {accuracy_of_accurate:.2f}")
print(f"Precision: {precision_of_accurate:.2f}")

print("\nPrecise but Not Accurate Measurements:")
print(f"Measurements: {precise_measurements}")
print(f"Accuracy: {accuracy_of_precise:.2f}")
print(f"Precision: {precision_of_precise:.2f}")


##########################

