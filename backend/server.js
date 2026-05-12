require("dotenv").config();

const connectDB = require("./config/db");
const express = require("express");
const cors = require("cors");

const newsRoutes = require("./routes/newsRoutes");

const app = express();

app.use(cors());
app.use(express.json());

app.use("/api", newsRoutes);

connectDB();

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
