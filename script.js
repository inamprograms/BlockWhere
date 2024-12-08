// Script for handling chat interactions
document.getElementById("send-button").addEventListener("click", function () {
    const userInput = document.getElementById("user-input").value.trim();
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

        // Add bot response (placeholder)
        const botMessage = document.createElement("div");
        botMessage.className = "message bot-message";
        botMessage.innerText = "This is a bot response.";
        chatLog.appendChild(botMessage);
    }
});

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
