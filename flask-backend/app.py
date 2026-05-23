from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# 🔥 LOAD MODEL HERE (TOP LEVEL)
model = joblib.load("../model.pkl")
vectorizer = joblib.load("../vectorizer.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text")

    # convert text into vector
    vector = vectorizer.transform([text])

    # prediction
    prediction = model.predict(vector)[0]

    return jsonify({
        "prediction": str(prediction)
    })


if __name__ == "__main__":
    app.run(debug=True)