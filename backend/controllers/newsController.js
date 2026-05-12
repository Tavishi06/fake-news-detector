const axios = require("axios");

const predictNews = async (req, res) => {
  try {
    const { text } = req.body;

    console.log("Received text:", text);

    const response = await axios.post(
      "http://127.0.0.1:5000/predict",
      {
        text: text,
      }
    );

    console.log("Flask response:", response.data);

    res.json({
      prediction: response.data.prediction,
    });

  } catch (error) {
    console.log("Backend Error:", error.message);

    res.status(500).json({
      error: "Prediction failed",
    });
  }
};

module.exports = {
  predictNews,
};