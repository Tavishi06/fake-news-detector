# Fake News Detector

An AI-powered full-stack web application that detects whether a news headline or article is **REAL** or **FAKE** using TF-IDF feature extraction and Logistic Regression.

## Overview

The project combines a machine learning classification pipeline, a Flask inference API, a Node.js/Express backend with MongoDB persistence, and a web frontend:

- **ML Pipeline (`ml/`)**: Trains a `LogisticRegression` classifier (`class_weight="balanced"`) over TF-IDF features (`1–3` n-grams, `max_features=7000`) on `dataset/True.csv` and `dataset/Fake.csv`.
- **Flask ML API (`flask-backend/`)**: Serves `POST /predict` using the serialized `model.pkl` and `vectorizer.pkl`, returning both the predicted label (`FAKE` or `REAL`) and a confidence score.
- **Node.js Backend (`backend/`)**: Exposes `POST /api/predict`, forwards requests to the Flask ML service, and stores analyzed news texts and predictions in MongoDB via Mongoose.
- **Frontend (`frontend/`)**: Clean glassmorphism UI (`index.html`, `style.css`, `script.js`) for submitting news headlines or article text and viewing predictions.

## Tech Stack

- **Machine Learning**: Python, scikit-learn, pandas, NumPy, joblib / pickle
- **ML Inference API**: Flask, Flask-CORS, Gunicorn
- **Application Backend**: Node.js, Express 5, Mongoose, Axios, CORS, dotenv
- **Database**: MongoDB
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

## Project Structure

```text
fake-news-detector/
├── backend/                     # Node.js + Express API & MongoDB integration
│   ├── config/db.js             # Mongoose connection using MONGO_URI
│   ├── controllers/             # newsController.js (predictNews)
│   ├── models/News.js           # News schema (text, prediction)
│   ├── routes/newsRoutes.js     # POST /api/predict
│   ├── server.js                # Express app entrypoint (port 3000)
│   └── package.json
├── dataset/                     # Training data
│   ├── Fake.csv
│   └── True.csv
├── flask-backend/               # Deployable Flask ML service
│   ├── app.py                   # / and /predict routes
│   ├── model.pkl                # Trained LogisticRegression model
│   ├── vectorizer.pkl           # Fitted TfidfVectorizer
│   └── requirements.txt
├── frontend/                    # Web interface
│   ├── index.html
│   ├── script.js
│   └── style.css
├── ml/                          # Model training and local scripts
│   ├── train.py                 # TF-IDF + LogisticRegression training script
│   ├── app.py                   # Standalone local Flask script
│   └── requirements.txt
├── model.pkl                    # Root copy of trained model
└── vectorizer.pkl               # Root copy of fitted vectorizer
```

## Getting Started

### Prerequisites

- Python 3.x & `pip`
- Node.js & `npm`
- MongoDB instance (required for `backend/`)

### 1. Run the Flask ML API

```bash
cd flask-backend
pip install -r requirements.txt
python -m flask --app app run --port 5000
```

For production with Gunicorn:

```bash
cd flask-backend
gunicorn app:app
```

### 2. Run the Node.js / Express Backend

Ensure `backend/.env` contains your MongoDB connection string (`MONGO_URI`), then install dependencies and start the server:

```bash
cd backend
npm install
node server.js
```

The Express server listens on `http://localhost:3000`.

### 3. Open the Frontend

Open `frontend/index.html` directly in your browser or serve the `frontend/` directory with any static HTTP server.

> **Note:** `frontend/script.js` and `backend/controllers/newsController.js` are configured to call the deployed Render ML service URLs. To test completely locally, update those endpoints to `http://localhost:5000/predict` (or `http://localhost:3000/api/predict`).

### 4. Retrain the Model (Optional)

Update the CSV paths in `ml/train.py` to point to your local `dataset/True.csv` and `dataset/Fake.csv`, then run:

```bash
cd ml
python train.py
```

This outputs updated `model.pkl` and `vectorizer.pkl` artifacts and prints test accuracy and a classification report.

## API Reference

### Flask ML Service

#### `GET /`
Health check endpoint.

**Response:** `API is running`

#### `POST /predict`
Classifies news text as `FAKE` or `REAL`.

**Request Body:**
```json
{
  "text": "Government releases new budget for education"
}
```

**Response (`200 OK`):**
```json
{
  "prediction": "REAL",
  "confidence": 0.92
}
```

**Error (`400 Bad Request`):**
```json
{
  "error": "No text provided"
}
```

### Express Backend

#### `POST /api/predict`
Forwards `{ "text": "..." }` to the Flask ML service, persists `{ text, prediction }` in MongoDB, and returns the prediction payload.

## Contributors

| Contributor | GitHub | Role |
| --- | --- | --- |
| **Tavishi** | [@Tavishi06](https://github.com/Tavishi06) | Project Creator, ML Pipeline, Backend & Frontend |
| **Tanish Jaswal** | [@WARRIORXR](https://github.com/WARRIORXR) | Documentation & Repository Contributor |
