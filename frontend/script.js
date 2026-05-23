async function checkNews() {

    const news = document.getElementById("newsInput").value;

    if(news.trim() === "") {
        alert("Please enter some news text");
        return;
    }

    document.getElementById("result").innerText = "Analyzing with AI...";

    try {

        const response = await fetch("http://localhost:3000/api/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: news
            })
        });

        const data = await response.json();

        document.getElementById("result").innerText =
            "Prediction: " + data.prediction;

    }
    catch(error) {

        document.getElementById("result").innerText =
            "Server connection error";

        console.log(error);
    }
}
