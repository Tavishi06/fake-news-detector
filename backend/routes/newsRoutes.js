const express = require("express");

const router = express.Router();

const {
  predictNews,
} = require("../controllers/newsController");

router.post("/predict", predictNews);

module.exports = router;