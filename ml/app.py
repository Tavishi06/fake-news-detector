from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))

@app.route("/")
def home():
    return "Fake News API Running"

@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        text = data["text"]

        transformed_text = vectorizer.transform([text])

        prediction = model.predict(transformed_text)[0]

        result = "Real" if prediction == 1 else "Fake"

        return jsonify({
            "prediction": result
        })

    except Exception as e:

        print("Flask Error:", str(e))

        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(port=5000)