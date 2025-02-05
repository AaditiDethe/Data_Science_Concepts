# Recommendation System

This folder contains implementations of different recommendation system techniques, including Association Rule Mining, Content-Based Filtering and Collaborative Filtering.

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

### 3. Game Recommendation (Collaborative Filtering)
   Implementation Steps:

      -> Load dataset containing user-game ratings.

      -> Create a user-item matrix where rows represent users and columns represent games.

      -> Fill missing values (assume unrated games as 0).

      -> Compute cosine similarity between users.

      -> Generate recommendations by aggregating ratings from similar users.

   Example Use Cases:

      -> Recommending video games based on user preferences.

      -> Suggesting games to new users based on similar user behaviors.

   How to Run

      -> Install required libraries: pip install pandas numpy sklearn mlxtend

      -> Run the respective scripts based on the recommendation type:
      python association_rules.py
      python entertainment_recommendation.py
      python game_recommendation.py

   Dependencies

      -> pandas for data manipulation.

      -> numpy for numerical operations.

      -> mlxtend for implementing the Apriori algorithm.

      -> sklearn for TF-IDF vectorization and cosine similarity computation.
