from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load model and vectorizer from ml folder
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
vectorizer_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    print("✓ Model and vectorizer loaded successfully")
except FileNotFoundError as e:
    print(f"⚠ Error: {e}")
    print("⚠ Make sure you have run ml/train.py first to generate model.pkl and vectorizer.pkl")

@app.route("/")
def home():
    return "API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text")

    # 🛑 safety check
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # convert text to vector
    vector = vectorizer.transform([text])

    # prediction
    prediction = model.predict(vector)[0]

    # convert to readable label
    label = "FAKE" if prediction == 0 else "REAL"

    prob = model.predict_proba(vector)[0]
    confidence = max(prob)

    return jsonify({
        "prediction": label,
        "confidence": round(float(confidence), 2)
    })