// Script for handling chat interactions
document.getElementById("send-button").addEventListener("click", async function () {
    const userInput = document.getElementById("user-input").value.trim();
    const contentType = document.getElementById("search-options").value; // Get selected content type
    const chatLog = document.getElementById("chat-log");

    if (userInput) {
        // Append user message
        const userMessage = document.createElement("div");
        userMessage.className = "message user-message";
        userMessage.innerText = userInput;
        chatLog.appendChild(userMessage);

        // Clear input
        document.getElementById("user-input").value = "";

        // Scroll to the bottom
        chatLog.scrollTop = chatLog.scrollHeight;

        // Call the appropriate API
        try {
            const botResponse = await callAPI(userInput, contentType);
            
            // Handle API response and append bot message
            const botMessage = document.createElement("div");
            botMessage.className = "message bot-message";

            if (contentType === "text") {
                botMessage.innerText = botResponse.response; // Assuming API returns { response: "text" }
            } else if (contentType === "image") {
                const img = document.createElement("img");
                img.src = botResponse.response; // Assuming API returns { response: "image_url" }
                img.alt = "Generated Image";
                botMessage.appendChild(img);
            } else if (contentType === "video") {
                const video = document.createElement("video");
                video.src = botResponse.response; // Assuming API returns { response: "video_url" }
                video.controls = true;
                botMessage.appendChild(video);
            } else if (contentType === "all") {
                botMessage.innerText = JSON.stringify(botResponse, null, 2);
            } else {
                botMessage.innerText = "Unsupported content type.";
            }

            chatLog.appendChild(botMessage);
        } catch (error) {
            console.error("Error calling API:", error);

            const errorMessage = document.createElement("div");
            errorMessage.className = "message bot-message";
            errorMessage.innerText = "Sorry, something went wrong. Please try again.";
            chatLog.appendChild(errorMessage);
        }
    }
});

// Function to call the backend API
async function callAPI(query, contentType) {
    let apiUrl;

    // Select API endpoint based on contentType
    switch (contentType) {
        case "text":
            apiUrl = "http://192.168.100.9:5000/api/generate";
            break;
        case "image":
            apiUrl = "http://192.168.100.9:5000/api/meme";
            break;
        case "video":
            apiUrl = "http://192.168.100.9:5000/api/video";
            break;
        case "all":
            apiUrl = "http://192.168.100.9:5000/api/generate_all";
            break;
        default:
            throw new Error("Invalid content type selected");
    }

    const requestData = {
        query: query,
        content_type: contentType
    };

    const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(requestData)
    });

    if (!response.ok) {
        throw new Error(`API call failed with status: ${response.status}`);
    }

    return response.json(); // Assuming the API returns JSON
}

// Crypto Tip of the Day
const tips = [
    "Diversify your crypto investments to minimize risks!",
    "Always store your private keys securely.",
    "Research thoroughly before investing in any cryptocurrency.",
    "Use a hardware wallet for long-term storage.",
    "Keep an eye on market trends and news for informed decisions."
];

const randomTip = tips[Math.floor(Math.random() * tips.length)];
document.getElementById("tip-content").innerText = randomTip;
