const express = require('express');
const router = express.Router();


const exampleResponse = {
    text: "This is the response text based on your query.",
    image: "https://via.placeholder.com/150" // Replace with dynamic URL if needed
};

// Route to handle user query
router.post('/get-response', (req, res) => {
    const userQuery = req.body.query;

    // Perform processing based on userQuery (mock response here)
    console.log(`Received query: ${userQuery}`);
    
    // Respond with text and image
    res.json({
        success: true,
        data: exampleResponse
    });
});

module.exports = router;
