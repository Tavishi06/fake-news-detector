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

    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]

    return jsonify({"prediction": str(prediction)})
