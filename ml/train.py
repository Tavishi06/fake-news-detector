import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv(r"E:\Fake news\ml\FakeNewsNet.csv")

# Input text
X = df["title"]

# Labels
y = df["real"]

# Convert text to vectors
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()

model.fit(X_vectorized, y)

# Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained successfully")