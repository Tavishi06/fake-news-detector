const mongoose = require("mongoose");

const newsSchema = new mongoose.Schema({

    text: {
        type: String
    },

    prediction: {
        type: String
    }

});

module.exports = mongoose.model("News", newsSchema);