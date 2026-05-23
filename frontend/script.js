async function checkNews() {
  const news = document.getElementById("newsInput").value;

  if (!news.trim()) {
    alert("Enter news text");
    return;
  }

  const response = await fetch(
    "https://fake-news-ml-ax7x.onrender.com/predict",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: news })
    }
  );

  const data = await response.json();

  document.getElementById("result").innerText =
    "Prediction: " + data.prediction;
}