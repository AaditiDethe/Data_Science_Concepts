# Recommendation System

This folder contains implementations of different recommendation system techniques, including Association Rule Mining, Content-Based Filtering, and Collaborative Filtering.

### 1.Association Rules
   Implementation Steps:

      -> Convert dataset to one-hot encoded format using TransactionEncoder.

      -> Apply the Apriori algorithm to identify frequent itemsets.

      -> Generate association rules based on the chosen metric (lift or confidence).

      -> Output results including frequent itemsets and association rules.

   Example Use Cases:

      -> Retail: Discover frequently purchased items together (e.g., Milk & Bread).

      -> Healthcare: Identify common symptom-disease associations.

      -> E-commerce: Analyze product bundling patterns.

### 2. Entertainment Recommendation (Content-Based Filtering)
   Implementation Steps:

      -> Load dataset containing entertainment titles and categories.

      -> Convert textual data into numerical representation using TF-IDF.

      -> Compute cosine similarity between different titles.

      -> Retrieve and recommend top-N similar items based on a given title.

   Example Use Cases:

      -> Suggesting similar movies based on genre.

      -> Recommending TV shows based on past preferences.
