import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load datasets
true_df = pd.read_csv(r"E:\fake news\dataset\True.csv")
fake_df = pd.read_csv(r"E:\fake news\dataset\Fake.csv")

# Labels
true_df["label"] = 1
fake_df["label"] = 0

# Merge
df = pd.concat([true_df, fake_df], axis=0)

# Clean
df = df.dropna()
df = df.sample(frac=1, random_state=42)

# Features (VERY IMPORTANT)
X = df["title"].astype(str) + " " + df["text"].astype(str)
y = df["label"]

# TF-IDF (optimized)
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7,
    min_df=3,
    ngram_range=(1, 2),
    max_features=7000
)

X_vec = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# Model
model = LinearSVC()
model.fit(X_train, y_train)

# Evaluate
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

# Test
print(model.predict(vectorizer.transform([
    "Aliens control the White House secretly"
])))

# Save
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))