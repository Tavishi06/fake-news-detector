from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load model & vectorizer
model = joblib.load("../model.pkl")
vectorizer = joblib.load("../vectorizer.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]

    # Transform & predict
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    # Convert to readable label
    label = "FAKE" if prediction == 0 else "REAL"

    return jsonify({
        "prediction": label
    })


@app.route("/")
def home():
    return "Fake News API Running"


if __name__ == "__main__":
    app.run(debug=True)