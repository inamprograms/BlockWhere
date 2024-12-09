// Event Listener for Send Button
document.getElementById("send-button").addEventListener("click", function () {
    // Get the selected option from the dropdown
    const selectedOption = document.getElementById("search-options").value;

    // Prepare the data to send
    const dataToSend = {
        type: selectedOption, // Send the selected type (e.g., text, image, video, meme, or all)
    };

    // Send the data to the backend
    fetch("/api/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dataToSend), // Send the data as JSON
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then((data) => {
        if (data.success) {
            alert(`Request for ${selectedOption} sent successfully!`);
        } else {
            alert(`Failed to send request for ${selectedOption}. Please try again.`);
        }
    })
    .catch((error) => {
        console.error("Error:", error);
        alert("An error occurred while sending the request.");
    });
});

// Event Listeners for Dropdown Items
document.querySelectorAll(".dropdown-item").forEach((item) => {
    item.addEventListener("click", function (event) {
        const userMessage = document.getElementById("user-input").value.trim(); // Get the user's message
        const platformId = event.target.id; // Get the ID of the clicked item

        if (userMessage) {
            let platform = ""; // Initialize the platform variable

            // Determine the platform based on the clicked item's ID
            if (platformId === "linkedin-post") {
                platform = "LinkedIn";
            } else if (platformId === "x-post") {
                platform = "X";
            } else if (platformId === "instagram-post") {
                platform = "Instagram";
            } else {
                alert("Invalid platform selected!");
                return;
            }

            const postContent = `🌟 ${platform} Post 🌟\n\n"${userMessage}"\n\n#CryptoChat #Blockchain`;

            // Send data to the backend
            fetch("/api/post", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ platform, message: postContent }), // Send platform and content
            })
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then((data) => {
                if (data.success) {
                    alert(`${platform} Post sent successfully!`);
                } else {
                    alert(`Failed to send ${platform} Post. Please try again.`);
                }
            })
            .catch((error) => {
                console.error("Error:", error);
                alert("An error occurred while sending the post.");
            });

            // Optionally copy the content to clipboard for user convenience
            navigator.clipboard.writeText(postContent).catch((err) => {
                console.error("Clipboard copy failed:", err);
            });
        } else {
            alert("Please type a message to create a social media post!");
        }
    });
});

// Function to Append Messages
function appendMessage(chatLog, message, className) {
    try {
        const newMessage = document.createElement("div");
        newMessage.className = `message ${className}`;
        newMessage.innerText = message;
        chatLog.appendChild(newMessage);
    } catch (error) {
        console.error("Error appending message:", error);
    }
}

// Function to Append Bot Response
function appendBotResponse(chatLog, botResponse, contentType) {
    try {
        const botMessage = document.createElement("div");
        botMessage.className = "message bot-message";

        if (contentType === "text") {
            botMessage.innerText = botResponse.response;
        } else if (contentType === "image") {
            const img = document.createElement("img");
            img.src = botResponse.response;
            img.alt = "Generated Image";
            botMessage.appendChild(img);
        }
        chatLog.appendChild(botMessage);
    } catch (error) {
        console.error("Error appending bot response:", error);
    }
}

// Function to Call API
async function callAPI(query, contentType, platformType) {
    const apiUrl = `https://blockwhere.onrender.com/api/${contentType}`;
    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                query: query,
                content_type: contentType,
                platform_type: platformType, // Pass platform type correctly
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json(); // Parse and return the JSON response
    } catch (error) {
        console.error("Error calling API:", error);
        throw error; // Re-throw the error for further handling if needed
    }
}

// Show a Random Tip
const tips = ["Diversify investments!", "Secure private keys!", "Use a hardware wallet!", "Track market trends!"];
document.getElementById("tip-content").innerText = tips[Math.floor(Math.random() * tips.length)];
