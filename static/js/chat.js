document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.getElementById('chat-container');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const resetBtn = document.getElementById('reset-btn');
    
    // Focus input on page load
    userInput.focus();

    function createTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'flex mb-4 typing-indicator-container';
        typingDiv.innerHTML = `
            <div class="flex-shrink-0 mr-3">
                <div class="w-10 h-10 rounded-full bg-gradient-to-r from-primary-600 to-secondary-500 flex items-center justify-center">
                    <span class="text-white font-bold">TC</span>
                </div>
            </div>
            <div class="bg-gray-100 rounded-2xl py-3 px-4 max-w-[80%]">
                <div class="typing-indicator flex space-x-1">
                    <span class="w-2 h-2 bg-gray-500 rounded-full"></span>
                    <span class="w-2 h-2 bg-gray-500 rounded-full"></span>
                    <span class="w-2 h-2 bg-gray-500 rounded-full"></span>
                </div>
            </div>
        `;
        return typingDiv;
    }

    function removeTypingIndicator() {
        const indicator = document.querySelector('.typing-indicator-container');
        if (indicator) {
            indicator.remove();
        }
    }

    function addMessage(message, isUser) {
        removeTypingIndicator();
        
        // Process the message to remove <think> tags if present
        if (!isUser) {
            message = processAIResponse(message);
        }
        
        const messageDiv = document.createElement('div');
        messageDiv.className = 'flex mb-4';
        
        if (isUser) {
            messageDiv.innerHTML = `
                <div class="flex-grow"></div>
                <div class="message-appear bg-primary-100 rounded-2xl py-3 px-4 max-w-[80%] text-right">
                    <p class="text-gray-800">${escapeHtml(message)}</p>
                </div>
                <div class="flex-shrink-0 ml-3">
                    <div class="w-10 h-10 rounded-full bg-gray-300 flex items-center justify-center">
                        <span class="text-white font-bold">You</span>
                    </div>
                </div>
            `;
        } else {
            messageDiv.innerHTML = `
                <div class="flex-shrink-0 mr-3">
                    <div class="w-10 h-10 rounded-full bg-gradient-to-r from-primary-600 to-secondary-500 flex items-center justify-center">
                        <span class="text-white font-bold">TC</span>
                    </div>
                </div>
                <div class="message-appear bg-gray-100 rounded-2xl py-3 px-4 max-w-[80%]">
                    <p class="text-gray-800">${formatMessage(message)}</p>
                </div>
            `;
        }
        
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
    
    function processAIResponse(response) {
        // Remove content between <think> tags
        return response.replace(/<think>[\s\S]*?<\/think>/g, '').trim();
    }
    
    function escapeHtml(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
    
    function formatMessage(message) {
        // Convert line breaks to <br> tags
        return escapeHtml(message).replace(/\\n/g, '<br>');
    }

    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        addMessage(message, true);
        userInput.value = '';
        userInput.disabled = true;
        sendBtn.disabled = true;
        
        // Show typing indicator
        chatContainer.appendChild(createTypingIndicator());
        chatContainer.scrollTop = chatContainer.scrollHeight;

        try {
            console.log("Sending message:", message);
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            console.log("Received response:", data);
            
            // Small delay to make the typing indicator visible
            setTimeout(() => {
                if (data && data.response) {
                    addMessage(data.response, false);
                } else {
                    addMessage("Sorry, I received an empty response. Please try again or contact us directly at support@techconnect.com.", false);
                }
            }, 500);
            
        } catch (error) {
            console.error('Error:', error);
            setTimeout(() => {
                addMessage('Sorry, there was an error processing your request. Please try again or contact us at support@techconnect.com.', false);
            }, 500);
        } finally {
            setTimeout(() => {
                userInput.disabled = false;
                sendBtn.disabled = false;
                userInput.focus();
            }, 500);
        }
    }

    async function resetChat() {
        try {
            await fetch('/reset', { method: 'POST' });
            chatContainer.innerHTML = '';
            addMessage('Hello! Welcome to TechConnect Support. How can I help you today?', false);
        } catch (error) {
            console.error('Error resetting chat:', error);
        }
    }

    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') sendMessage();
    });
    resetBtn.addEventListener('click', resetChat);
});
