from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

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