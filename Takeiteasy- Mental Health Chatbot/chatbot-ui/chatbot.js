const API_URL = "http://127.0.0.1:8000/chat"; // Local FastAPI endpoint
const session_id = "user_" + Math.floor(Math.random() * 10000); // Temporary user session

// Function to control chat UI visibility (from image_8a37b1.jpg)
function toggleChat() {
    const chatContainer = document.getElementById("chatContainer");
    chatContainer.style.display = chatContainer.style.display === "flex" ? "none" : "flex";
}

// Function to append a message to the chat box (from image_8a3810.png)
function appendMessage(role, text) {
    const box = document.getElementById("chatBox");
    const msg = document.createElement("div");
    
    // Format the message with the role (Human or AI/Bot)
    msg.innerHTML = `<strong>${role}:</strong> ${text}`;
    
    // Apply basic styling (as seen in image_8a3810.png)
    msg.style.margin = "6px 0";
    
    box.appendChild(msg);
    
    // Scroll to the bottom of the chat box
    box.scrollTop = box.scrollHeight; 
}

// Async function to handle user input and send message to the backend (from image_8a3b74.png & image_8a3bd0.png)
async function sendMessage() {
    const input = document.getElementById("userInput");
    const text = input.value.trim();

    // Do nothing if the input is empty
    if (!text) return;

    // 1. Display the user's message immediately
    appendMessage("You", text);
    
    // 2. Clear the input field
    input.value = "";
    
    try {
        // 3. Send the POST request to the FastAPI /chat endpoint
        const res = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            // The body matches the ChatRequest model (session_id, query) in your backend
            body: JSON.stringify({ session_id: session_id, query: text })
        });

        // 4. Parse the JSON response
        const data = await res.json();
        
        // 5. Display the response from the Bot
        appendMessage("AI", data.response);

    } catch (err) {
        // Error handling (from image_8a3c26.jpg)
        console.error("Fetch Error:", err);
        appendMessage("Bot", "Oops! Something went wrong.");
    }
}
// Function to manage the state of the send button
function toggleSendButton() {
    const input = document.getElementById("userInput");
    const button = document.querySelector("#inputArea button");

    // Disable if the input trimmed value is empty, otherwise enable
    button.disabled = input.value.trim() === "";
}