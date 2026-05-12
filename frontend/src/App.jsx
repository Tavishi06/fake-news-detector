import { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");

  const handleSubmit = async () => {
    try {
      const response = await axios.post(
        "http://localhost:3000/api/predict",
        { text }
      );

      setResult(response.data.prediction);
    } catch (error) {
      console.log(error);
      setResult("Error while predicting");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Fake News Detector</h1>

      <textarea
        rows="10"
        cols="50"
        placeholder="Enter news..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <br /><br />

      <button onClick={handleSubmit}>
        Check News
      </button>

      <h2>Result: {result}</h2>
    </div>
  );
}

export default App;