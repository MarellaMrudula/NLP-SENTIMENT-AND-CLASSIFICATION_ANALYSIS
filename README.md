# NLP-SENTIMENT-AND-CLASSIFICATION_ANALYSIS

This project implements a Sentiment Analysis system using Support Vector Machine (SVM) for text classification, which has been deployed as a web application using Streamlit. The model is trained to classify text into Positive, Negative, and Neutral sentiments based on user-provided inputs.

Overview The goal of this project is to predict the sentiment of a given text review. It leverages the power of machine learning, particularly SVM, to analyze the sentiment of text data, and has been deployed as a user-friendly web application that takes input directly from users and provides instant predictions.

Features Sentiment Classification: Classifies user input as either Positive, Negative, or Neutral. Streamlit Deployment: A web-based app that allows users to interact with the sentiment analysis model via a simple text input. Model Training: The SVM model is fine-tuned to achieve optimal accuracy by applying hyperparameter tuning techniques. Preprocessing: Text data is preprocessed using techniques such as tokenization, removing stopwords, and vectorization using TF-IDF.

Tools & Libraries Google Colab: Used for model development and training. Streamlit: Used for deploying the web app. SVM (Support Vector Machine): The primary model used for sentiment classification. Sklearn: For model building and evaluation, including vectorization and SVM implementation. Pandas & Numpy: For data manipulation and analysis. Matplotlib & Seaborn: Used for visualizations during EDA (Exploratory Data Analysis).

Dataset The dataset used in this project consists of user reviews along with labeled sentiments, which are categorized as Positive, Negative, and Neutral. The data was preprocessed by removing special characters, tokenizing, and converting text to numerical format using TF-IDF for model training.

Key Components Exploratory Data Analysis (EDA): Visualized word frequencies, sentiment distributions, and most common words across different sentiments.

Model Building: Built and tuned the SVM model using GridSearchCV for hyperparameter optimization. Evaluated using performance metrics like accuracy, precision, recall, and F1-score. Deployment: Deployed the trained SVM model using Streamlit for real-time sentiment prediction.

Model Performance The SVM model achieved an accuracy of 92.9% after hyperparameter tuning. Below is the classification report for the final model:

Sentiment Precision Recall F1-Score Positive 93% 99% 96% Negative 81% 43% 56% Neutral 00% 00% 00%

Future Improvements Improve performance on the Neutral sentiment by collecting more balanced data or applying advanced techniques such as ensemble methods. Integrate other models (like Random Forest, Decision Trees) for comparison. Improve text preprocessing to better handle sarcasm, negations, and slang

License This project is licensed under the MIT License. See the LICENSE file for more details.
