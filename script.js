document.getElementById("send-button").addEventListener("click", async function () {
    const userInput = document.getElementById("user-input").value.trim();
    const contentType = document.getElementById("search-options").value;
    const chatLog = document.getElementById("chat-log");

    if (userInput) {
        appendMessage(chatLog, userInput, "user-message");

        document.getElementById("user-input").value = ""; // Clear input
        chatLog.scrollTop = chatLog.scrollHeight; // Scroll down

        try {
            const botResponse = await callAPI(userInput, contentType);
            appendBotResponse(chatLog, botResponse, contentType);
        } catch (error) {
            appendMessage(chatLog, "Error: Try again later.", "bot-message");
        }
    }
});

document.getElementById("social-post-button").addEventListener("click", function () {
    const userMessage = document.getElementById("user-input").value.trim();
    if (userMessage) {
        const postContent = `🌟 Crypto Update 🌟\n\n"${userMessage}"\n\n#CryptoChat #Blockchain`;
        alert(`Social Post: ${postContent}`);
        navigator.clipboard.writeText(postContent);
    } else {
        alert("Type a message to create a social post!");
    }
});

function appendMessage(chatLog, message, className) {
    const newMessage = document.createElement("div");
    newMessage.className = `message ${className}`;
    newMessage.innerText = message;
    chatLog.appendChild(newMessage);
}

function appendBotResponse(chatLog, botResponse, contentType) {
    const botMessage = document.createElement("div");
    botMessage.className = "message bot-message";

    if (contentType === "text") {
        botMessage.innerText = botResponse.response;
    } else if (contentType === "image") {
        const img = document.createElement("img");
        img.src = botResponse.response;
        img.alt = "Generated Image";
        botMessage.appendChild(img);
    } else if (contentType === "video") {
        const video = document.createElement("video");
        video.src = botResponse.response;
        video.controls = true;
        botMessage.appendChild(video);
    }
    chatLog.appendChild(botMessage);
}

async function callAPI(query, contentType) {
    const apiUrl = `http://192.168.100.9:5000/api/${contentType}`;
    const response = await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query, content_type: contentType })
    });
    return response.json();
}

const tips = ["Diversify investments!", "Secure private keys!", "Use a hardware wallet!", "Track market trends!"];
document.getElementById("tip-content").innerText = tips[Math.floor(Math.random() * tips.length)];
