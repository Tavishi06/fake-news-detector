const axios = require("axios");

const predictNews = async (req, res) => {
  try {
    const { text } = req.body;

    console.log("Received text:", text);

    const flaskResponse = await axios.post(
      "https://fake-news-ml-kpt9.onrender.com/predict",
      {
        text: text
      }
    );

    console.log("Flask response:", flaskResponse.data);

    res.json(flaskResponse.data);

  } catch (error) {
    console.log("Backend Error:", error.message);

    res.status(500).json({
      error: "Prediction failed"
    });
  }
};

module.exports = { predictNews };