# Confusion Matrix

A Confusion Matrix is a performance measurement tool used to evaluate the accuracy of a classification algorithm. It provides a summary of the prediction results by comparing the actual labels with the predicted labels.

### Key Metrics Derived from the Confusion Matrix

   -> Accuracy: Measures overall correctness of the model.
      (TP+TN)/(TP+TN+FP+FN)


   -> Precision: Measures the proportion of correct positive predictions.
      Precision = (TP)/(TP+FP)


   -> Recall (Sensitivity): Measures the proportion of actual positives correctly identified.
      Recall = (TP)/(TP+FN)


   -> F1-Score: The harmonic mean of precision and recall.
      F1-Score = 2*((Precision*Recall)/(Precision+Recall))


   -> Specificity: Measures the proportion of actual negatives correctly identified.
      Specificity = (TN)/(TN+FP)

### Importance of Confusion Matrix
   -> Identifies where the model is making errors (false positives vs. false negatives).

   -> Helps in adjusting model performance, especially for imbalanced datasets where accuracy 
   alone can be misleading.

   -> Provides a comprehensive evaluation compared to just using accuracy.

### Practical Usage

   -> Confusion matrices are widely used in:

   -> Medical diagnostics (detecting diseases)

   -> Fraud detection (identifying fraudulent transactions)

   -> Sentiment analysis (classifying reviews as positive or negative)

   -> Spam classification (distinguishing spam from legitimate emails)

Understanding and analyzing the confusion matrix is essential for improving model performance and making informed decisions about model adjustments.
