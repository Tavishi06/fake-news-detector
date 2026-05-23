import requests

res = requests.post(
    "https://fake-news-ml-ax7x.onrender.com/predict",
    json={"text": "This is fake news"}
)

print(res.json())