import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load datasets
true_df = pd.read_csv(r"E:\fake news\dataset\True.csv")
fake_df = pd.read_csv(r"E:\fake news\dataset\Fake.csv")

# Labels
true_df["label"] = 1
fake_df["label"] = 0

print(f"True samples before merge: {len(true_df)}")
print(f"Fake samples before merge: {len(fake_df)}")

# Merge
df = pd.concat([true_df, fake_df], axis=0)

print(f"Total samples after merge: {len(df)}")

# Clean
df = df.dropna()

print(f"Samples after dropna: {len(df)}")
print(f"NaN values per column:\n{df.isnull().sum()}")

df = df.sample(frac=1, random_state=42)

# Features (VERY IMPORTANT)
X = df["title"].astype(str) + " " + df["text"].astype(str)
y = df["label"]

print(f"X length: {len(X)}, y length: {len(y)}")
print(f"Labels in y: {y.unique()}")
print(f"Class distribution before split:")
print(y.value_counts())

# TF-IDF (optimized)
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7,
    min_df=3,
    ngram_range=(1, 3),
    max_features=7000
)

X_vec = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# Check class distribution
print("Class distribution:")
print(y.value_counts())

# Model - Using LogisticRegression which works better for text
model = LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000)

model.fit(X_train, y_train)

# Evaluate
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print("\nClassification Report:")
print(classification_report(y_test, pred, target_names=['Fake (0)', 'Real (1)']))

# Test
print(model.predict(vectorizer.transform([
    "NASA confirms aliens exist on Mars"
])))

print(model.predict(vectorizer.transform([
    "Government releases new budget for education"
])))

test_samples = [
    "Government announces new policy",
    "Aliens control White House secretly",
    "Stock market rises today",
    "Scientists discover new virus"
]

for t in test_samples:
    print(t, model.predict(vectorizer.transform([t])))

# Save
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))