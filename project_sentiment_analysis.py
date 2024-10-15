# -*- coding: utf-8 -*-
"""Project Sentiment analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dJl3twvnLpecRbz8AqLHy1yieOFxr8XE

NLP Sentiment and classification analysis:
"""

import pandas as pd

# Load the dataset
df = pd.read_csv('amazon_reviews.csv')

# View the first few rows
print(df.head())

# Check dataset structure
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Get basic statistics on numeric fields
print(df.describe())

# Check column names
print(df.columns)

# View a random sample of reviews
print(df.sample(5))

# Drop rows with missing review text
df = df.dropna(subset=['reviewerName'])

# Remove duplicates
df = df.drop_duplicates()

# Preview cleaned data
print(df.head())

# Drop rows with missing review text
df = df.dropna(subset=['reviewText'])

# Remove duplicates
df = df.drop_duplicates()

# Preview cleaned data
print(df.head())

print(df.columns)

# Rename the unnamed columns
df = df.rename(columns={'Unnamed: 0': 'Sno'})

print(df.columns)

df_cleaned = df.dropna()

# Check the result
print(df_cleaned)

import re

# Function to clean the review text
def clean_text(text):
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Apply the cleaning function to the review text column
df['cleaned_review'] = df['reviewText'].apply(clean_text)

from nltk.tokenize import word_tokenize
import nltk

# Download necessary NLTK resources
nltk.download('punkt')

# Tokenize the review text
df['tokenized_review'] = df['cleaned_review'].apply(word_tokenize)

from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Remove stopwords from the tokenized review
df['review_no_stopwords'] = df['tokenized_review'].apply(lambda x: [word for word in x if word not in stop_words])

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize words
df['lemmatized_review'] = df['review_no_stopwords'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

import matplotlib.pyplot as plt
import seaborn as sns

# Set the aesthetic style of the plots
sns.set(style='whitegrid')

# Histogram for numerical columns
df.hist(bins=30, figsize=(15, 10))
plt.tight_layout()
plt.show()

def sentiment_label(rating):
    if rating >= 4:
        return 'Positive'
    elif rating <= 2:
        return 'Negative'
    else:
        return 'Neutral'

# Create a new column for sentiment labels
df['sentiment'] = df['overall'].apply(sentiment_label)

print(df.sentiment)

# Count plot for a categorical column (e.g., 'sentiment')
sns.countplot(data=df, x='sentiment')
plt.title('Count of Sentiment')
plt.show()

# Drop the reviewer name column
df = df.drop(columns=['reviewerName'])

# Check the updated DataFrame
print(df.head())

# Box plot to analyze ratings by sentiment
sns.boxplot(data=df, x='sentiment', y='overall')
plt.title('Box Plot of Ratings by Sentiment')
plt.show()

from wordcloud import WordCloud

# Combine all reviews into one string
text = ' '.join(df['reviewText'].dropna())

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.show()

# Generate word cloud for Negative sentiment
negative_text = ' '.join(df[df['sentiment'] == 'Negative']['reviewText'])  # Replace with your actual column names
negative_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(negative_text)

plt.figure(figsize=(10, 6))
plt.imshow(negative_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Negative Sentiments')
plt.show()

# Generate word cloud for Neutral sentiment
neutral_text = ' '.join(df[df['sentiment'] == 'Neutral']['reviewText'])  # Replace with your actual column names
neutral_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(neutral_text)

plt.figure(figsize=(10, 6))
plt.imshow(neutral_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Neutral Sentiments')
plt.show()

# Generate word cloud for Positive sentiment
positive_text = ' '.join(df[df['sentiment'] == 'Positive']['reviewText'])  # Replace with your actual column names
positive_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_text)

plt.figure(figsize=(10, 6))
plt.imshow(positive_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Positive Sentiments')
plt.show()

from collections import Counter
import matplotlib.pyplot as plt
import re
def get_most_common_words(text_series, n=10):
    # Combine all texts into one string
    all_text = ' '.join(text_series)

    # Remove punctuation and make everything lowercase
    all_text = re.sub(r'[^\w\s]', '', all_text.lower())

    # Split into words
    words = all_text.split()

    # Count word frequencies
    word_counts = Counter(words)

    # Get the most common words
    return word_counts.most_common(n)

# Most repeated words for Negative sentiment
negative_common_words = get_most_common_words(df[df['sentiment'] == 'Negative']['reviewText'], n=10)
print("Most Common Words in Negative Sentiments:")
print(negative_common_words)

# Most repeated words for Neutral sentiment
neutral_common_words = get_most_common_words(df[df['sentiment'] == 'Neutral']['reviewText'], n=10)
print("Most Common Words in Neutral Sentiments:")
print(neutral_common_words)

# Most repeated words for Positive sentiment
positive_common_words = get_most_common_words(df[df['sentiment'] == 'Positive']['reviewText'], n=10)
print("Most Common Words in Positive Sentiments:")
print(positive_common_words)

# Step 5: Visualize the Most Common Words (Optional)
def plot_most_common_words(common_words, title):
    words, counts = zip(*common_words)
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.title(title)
    plt.xlabel('Words')
    plt.ylabel('Counts')
    plt.xticks(rotation=45)
    plt.show()

# Plot for Negative Sentiment
plot_most_common_words(negative_common_words, "Most Common Words in Negative Sentiments")

# Plot for Neutral Sentiment
plot_most_common_words(neutral_common_words, "Most Common Words in Neutral Sentiments")

# Plot for Positive Sentiment
plot_most_common_words(positive_common_words, "Most Common Words in Positive Sentiments")

"""Word Count Distribution
Description: A histogram to show the distribution of the number of words in reviews.
"""

df['word_count'] = df['reviewText'].apply(lambda x: len(x.split()))

plt.figure(figsize=(10, 5))
sns.histplot(df['word_count'], bins=30, kde=True, color='blue')
plt.title('Distribution of Word Count in Reviews')
plt.xlabel('Word Count')
plt.ylabel('Frequency')
plt.show()

"""Top N Words per Sentiment Class
Description: A horizontal bar plot for the most common words used in reviews for each sentiment category.
"""

def plot_top_n_words_per_sentiment(df, sentiment_label, n=10):
    words = ' '.join(df[df['sentiment'] == sentiment_label]['reviewText'])
    words = re.sub(r'[^\w\s]', '', words.lower()).split()
    word_counts = Counter(words).most_common(n)

    words, counts = zip(*word_counts)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(counts), y=list(words), palette='viridis')
    plt.title(f'Top {n} Words in {sentiment_label} Sentiment')
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.show()

# Plotting for each sentiment separately
# For Negative Sentiment
plot_top_n_words_per_sentiment(df, 'Negative', n=10)

# For Neutral Sentiment
plot_top_n_words_per_sentiment(df, 'Neutral', n=10)

# For Positive Sentiment
plot_top_n_words_per_sentiment(df, 'Positive', n=10)

df['review_length'] = df['reviewText'].apply(lambda x: len(x.split()))

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='review_length', y='sentiment', hue='sentiment', alpha=0.5)
plt.title('Review Length vs Sentiment')
plt.xlabel('Review Length (Number of Words)')
plt.ylabel('Sentiment')
plt.show()

print(df.columns)

# Pair plot for selected numerical columns
sns.pairplot(df[['overall', 'sentiment']], hue='sentiment')
plt.show()

"""0ct 1st
Text preprocessing..

"""

print(df.columns)

import pandas as pd
import nltk
import re
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')

# Example preprocess function with handling for missing or non-string values
def preprocess_text(text):
    # Check if the text is a string, if not return an empty string
    if not isinstance(text, str):
        return ''

    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d+', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])

    return text

# Apply preprocessing to the review text column
df['cleaned_review_text'] = df['reviewText'].apply(preprocess_text)

# Check the cleaned text
print(df[['reviewText', 'cleaned_review_text']].head())

"""Text Vectorization (Unstructured to Structured)
You can use TF-IDF (Term Frequency-Inverse Document Frequency) or CountVectorizer to convert the preprocessed text data into a structured format (numerical vectors).

Here we use TF-IDF:


"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize TF-IDF Vectorizer
tfidf = TfidfVectorizer(max_features=1000)  # Adjust max_features as needed

# Transform the cleaned text into structured data
X = tfidf.fit_transform(df['cleaned_review_text'])

# Convert the result into a DataFrame for easier understanding
X_df = pd.DataFrame(X.toarray(), columns=tfidf.get_feature_names_out())

# Check the structured data
print(X_df.head())

"""Sentiment Analysis
For sentiment analysis, you'll need labeled data (with sentiment tags like "positive", "negative", "neutral"). Here’s how to use the cleaned text and a basic classifier like Logistic Regression to classify the sentiment.
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Assuming your dataset has a 'sentiment' column with labels (0: negative, 1: positive, etc.)

y = df['sentiment']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the classifier (Logistic Regression)
clf = LogisticRegression()

# Train the classifier
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the classifier
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

print(df.columns)

"""0.9287 (around 93%) is the overall accuracy, which means that 93% of the predictions made by our model are correct.

** Class-wise Performance:**
The classification report shows the performance metrics for each class (Negative, Neutral, Positive):

# a. Negative Class:
Precision: 0.93
This means that when the model predicts "Negative," 93% of the time, it is correct.
Recall: 0.37
This means that out of all actual "Negative" instances, the model only correctly identifies 37%.
F1-Score: 0.53
The F1-Score is the harmonic mean of precision and recall, indicating that while the model is good at predicting "Negative" when it does, it struggles to recall them correctly, leading to a low F1-Score.
# b. Neutral Class:
Precision: 0.00
This means the model never correctly predicted a "Neutral" instance. Either it doesn't predict this class or misclassifies it.
Recall: 0.00
Out of all the actual "Neutral" instances, the model failed to correctly identify any of them.
F1-Score: 0.00
Since both precision and recall are 0, the F1-score is also 0, indicating the model completely failed to identify "Neutral" reviews.
# c. Positive Class:
Precision: 0.93
When the model predicts "Positive," it is 93% accurate.
Recall: 1.00
The model identified all actual "Positive" instances perfectly.
F1-Score: 0.96
This high F1-score shows that the model performs exceptionally well at identifying positive reviews.

**Macro Avg vs. Weighted Avg:**
# Macro Avg:
The macro average is simply the unweighted mean of precision, recall, and F1-score across all classes. Since the model performed poorly for "Neutral" and "Negative," these scores are much lower (precision: 0.62, recall: 0.46, F1: 0.50).
# Weighted Avg:
The weighted average takes class imbalance into account, giving more weight to the "Positive" class (since it dominates the dataset). Thus, the weighted averages (precision: 0.91, recall: 0.93, F1: 0.91) are higher, closer to the overall accuracy.
"""

print(df.columns)

"""Random forest

"""

# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split



# Assuming the dataset has columns 'reviewText' for reviews and 'sentiment' for labels
X = df['reviewText']  # Input features (text data)
y = df['sentiment']   # Target labels (sentiments)

# Convert text data into numerical form using TF-IDF
tfidf = TfidfVectorizer(max_features=1000, stop_words='english')
X_vectorized = tfidf.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Initialize the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest Model Accuracy: {accuracy}")

# Classification report for detailed performance metrics
print("Classification Report:")
print(classification_report(y_test, y_pred))

"""SVM"""

# Step 1: Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import GridSearchCV

# Step 2: Prepare your data
# Assuming 'reviewText' contains the text reviews and 'sentiment' contains the sentiment labels
X = df['reviewText']  # Input features (text data)
y = df['sentiment']   # Target labels (sentiments)

# Step 3: Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vectorized = vectorizer.fit_transform(X)

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Step 5: Build and train the SVM model
# Initialize the SVM model
svm_model = SVC(kernel='linear', class_weight='balanced', random_state=42)

# Train the model
svm_model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = svm_model.predict(X_test)

# Step 7: Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Optional: Hyperparameter tuning using GridSearchCV
param_grid = {
    'C': [0.1, 1, 10, 100],
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 'auto']
}

# Initialize GridSearchCV for hyperparameter tuning
grid_search = GridSearchCV(SVC(), param_grid, cv=3, scoring='accuracy', verbose=2, n_jobs=-1)

# Train with GridSearchCV
grid_search.fit(X_train, y_train)

# Output the best parameters
print(f"Best parameters: {grid_search.best_params_}")

# Get the best model
best_svm_model = grid_search.best_estimator_

# Evaluate the best model
y_pred_best = best_svm_model.predict(X_test)
print("Accuracy after tuning:", accuracy_score(y_test, y_pred_best))
print("Classification Report after tuning:")
print(classification_report(y_test, y_pred_best))

"""Decision Tree

"""

# Step 1: Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import GridSearchCV

# Step 2: Prepare your data
# Assuming 'reviewText' contains the text reviews and 'sentiment' contains the sentiment labels
X = df['reviewText']  # Input features (text data)
y = df['sentiment']   # Target labels (sentiments)

# Step 3: Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vectorized = vectorizer.fit_transform(X)

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Step 5: Build and train the Decision Tree model
# Initialize the Decision Tree model
dt_model = DecisionTreeClassifier(random_state=42)

# Train the model
dt_model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = dt_model.predict(X_test)

# Step 7: Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Optional: Hyperparameter tuning using GridSearchCV
param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Initialize GridSearchCV for hyperparameter tuning
grid_search = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=3, scoring='accuracy', verbose=2, n_jobs=-1)

# Train with GridSearchCV
grid_search.fit(X_train, y_train)

# Output the best parameters
print(f"Best parameters: {grid_search.best_params_}")

# Get the best model
best_dt_model = grid_search.best_estimator_

# Step 8: Evaluate the best model after tuning
y_pred_best = best_dt_model.predict(X_test)
print("Accuracy after tuning:", accuracy_score(y_test, y_pred_best))
print("Classification Report after tuning:")
print(classification_report(y_test, y_pred_best))

"""Naive bayes

"""

# Step 1: Import necessary libraries
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

# Step 2: Prepare your data
X = df['reviewText']
y = df['sentiment']

# Step 3: Vectorize the text data
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vectorized = vectorizer.fit_transform(X)

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Step 5: Train a Naive Bayes model
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)

# Step 6: Make predictions and evaluate
y_pred = nb_model.predict(X_test)
print("Naive Bayes Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report for Naive Bayes:")
print(classification_report(y_test, y_pred))

"""KNN"""

# Step 1: Import necessary libraries
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

# Step 2: Prepare your data
X = df['reviewText']
y = df['sentiment']

# Step 3: Vectorize the text data
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vectorized = vectorizer.fit_transform(X)

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Step 5: Train a K-Nearest Neighbors model
knn_model = KNeighborsClassifier(n_neighbors=5)  # You can adjust 'n_neighbors'
knn_model.fit(X_train, y_train)

# Step 6: Make predictions and evaluate
y_pred = knn_model.predict(X_test)
print("KNN Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report for KNN:")
print(classification_report(y_test, y_pred))

"""Model Evaluation (SVM - Tuned)
Accuracy:

Before tuning: 92.27%
After tuning: 92.98%
There's a slight improvement in accuracy after hyperparameter tuning with the SVM model.
Precision, Recall, and F1-score (Class-wise):

Negative Class:

Before tuning:
Precision: 0.67
Recall: 0.71
F1-Score: 0.69
After tuning:
Precision: 0.81 (improved)
Recall: 0.43 (significant drop)
F1-Score: 0.56 (decreased due to recall)
Evaluation: Tuning has improved the precision..

Overall SVM has got the highest accuracy..
"""
