import os

def create_file(path, content):
    # Only try to create directories if the path contains a directory component
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created {path}")

# Create app.py
app_py = '''from flask import Flask, render_template, request, jsonify
from secret_ai_sdk.secret_ai import ChatSecret
from secret_ai_sdk.secret import Secret
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Initialize Secret AI client
secret_client = Secret()
models = secret_client.get_models()
urls = secret_client.get_urls(model=models[0])

# Initialize the ChatSecret instance
secret_ai_llm = ChatSecret(
    base_url=urls[0],
    model=models[0],
    temperature=0.7  # Slightly lower temperature for more consistent responses
)

# Store conversation history
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    # Add system message if this is the first message
    if not conversation_history:
        conversation_history.append(
            ("system", "You are a compassionate therapist. Help the user with their emotional and psychological concerns.")
        )
    
    # Add user message to history
    conversation_history.append(("human", user_message))
    
    # Get response from Secret AI - add error handling
    try:
        response = secret_ai_llm.invoke(conversation_history, stream=False)
        ai_response = response.content
    except Exception as e:
        print(f"Error from Secret AI: {str(e)}")
        ai_response = "I'm sorry, I encountered an error. Please try again."
    
    # Add AI response to history
    conversation_history.append(("assistant", ai_response))
    
    # Debug print
    print(f"User: {user_message}")
    print(f"AI: {ai_response}")
    
    return jsonify({'response': ai_response})

@app.route('/reset', methods=['POST'])
def reset_conversation():
    global conversation_history
    conversation_history = []
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
'''

# Create index.html with Tailwind CSS
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MindfulChat - AI Therapy Assistant</title>
    <!-- Tailwind CSS via CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Custom Tailwind Config -->
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: {
                            50: '#f0f9ff',
                            100: '#e0f2fe',
                            200: '#bae6fd',
                            300: '#7dd3fc',
                            400: '#38bdf8',
                            500: '#0ea5e9',
                            600: '#0284c7',
                            700: '#0369a1',
                            800: '#075985',
                            900: '#0c4a6e',
                        },
                        secondary: {
                            50: '#f0fdfa',
                            100: '#ccfbf1',
                            200: '#99f6e4',
                            300: '#5eead4',
                            400: '#2dd4bf',
                            500: '#14b8a6',
                            600: '#0d9488',
                            700: '#0f766e',
                            800: '#115e59',
                            900: '#134e4a',
                        },
                    }
                }
            }
        }
    </script>
    <!-- Custom styles -->
    <style>
        .message-appear {
            animation: fadeIn 0.5s ease-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .typing-indicator span {
            animation: blink 1.4s infinite both;
        }
        
        .typing-indicator span:nth-child(2) {
            animation-delay: 0.2s;
        }
        
        .typing-indicator span:nth-child(3) {
            animation-delay: 0.4s;
        }
        
        @keyframes blink {
            0% { opacity: 0.1; }
            20% { opacity: 1; }
            100% { opacity: 0.1; }
        }
    </style>
</head>
<body class="bg-gray-50 min-h-screen">
    <div class="container mx-auto px-4 py-8 max-w-4xl">
        <!-- Header -->
        <header class="mb-6">
            <div class="flex items-center justify-center mb-4">
                <div class="bg-gradient-to-r from-primary-600 to-secondary-500 p-3 rounded-full">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                    </svg>
                </div>
            </div>
            <h1 class="text-3xl font-bold text-center text-gray-800 mb-2">MindfulChat</h1>
            <p class="text-center text-gray-600 max-w-xl mx-auto">Your AI therapy assistant, providing compassionate support and guidance whenever you need it.</p>
        </header>
        
        <!-- Chat Container -->
        <div class="bg-white rounded-xl shadow-lg overflow-hidden">
            <!-- Chat Messages -->
            <div id="chat-container" class="p-4 h-[500px] overflow-y-auto">
                <div class="flex mb-4">
                    <div class="flex-shrink-0 mr-3">
                        <div class="w-10 h-10 rounded-full bg-gradient-to-r from-primary-600 to-secondary-500 flex items-center justify-center">
                            <span class="text-white font-bold">AI</span>
                        </div>
                    </div>
                    <div class="message-appear bg-gray-100 rounded-2xl py-3 px-4 max-w-[80%]">
                        <p class="text-gray-800">Hello, I'm your AI therapist. How are you feeling today?</p>
                    </div>
                </div>
            </div>
            
            <!-- Input Area -->
            <div class="border-t border-gray-200 p-4 bg-gray-50">
                <div class="flex items-center">
                    <input 
                        type="text" 
                        id="user-input" 
                        class="flex-1 border border-gray-300 rounded-l-lg py-3 px-4 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent" 
                        placeholder="Type your message here..."
                    >
                    <button 
                        id="send-btn" 
                        class="bg-gradient-to-r from-primary-600 to-primary-700 text-white py-3 px-6 rounded-r-lg hover:from-primary-700 hover:to-primary-800 transition duration-300 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
                    >
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
                        </svg>
                    </button>
                </div>
                <div class="flex justify-between mt-3">
                    <button 
                        id="reset-btn" 
                        class="text-gray-600 text-sm flex items-center hover:text-primary-600 transition duration-300"
                    >
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                        </svg>
                        Reset Conversation
                    </button>
                    <p class="text-xs text-gray-500">Powered by Secret AI</p>
                </div>
            </div>
        </div>
        
        <!-- Footer -->
        <footer class="mt-8 text-center text-gray-500 text-sm">
            <p>© 2023 MindfulChat. All conversations are private and secure.</p>
        </footer>
    </div>

    <script src="{{ url_for('static', filename='js/chat.js') }}"></script>
</body>
</html>
'''

# Create chat.js with enhanced functionality
chat_js = '''document.addEventListener('DOMContentLoaded', function() {
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
                    <span class="text-white font-bold">AI</span>
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
                        <span class="text-white font-bold">AI</span>
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
                    addMessage("Sorry, I received an empty response. Please try again.", false);
                }
            }, 500);
            
        } catch (error) {
            console.error('Error:', error);
            setTimeout(() => {
                addMessage('Sorry, there was an error processing your request.', false);
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
            addMessage('Hello, I\\'m your AI therapist. How are you feeling today?', false);
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
'''

# Create all files
create_file('app.py', app_py)
create_file('templates/index.html', index_html)
create_file('static/js/chat.js', chat_js)

print("\nSetup complete! Run the application with: python app.py")
print("The application now uses Tailwind CSS for a modern, responsive UI.") 