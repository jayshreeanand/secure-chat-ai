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

# Create index.html
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Therapist Chat</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <h1>AI Therapist Chat</h1>
    <div class="chat-container" id="chat-container">
        <div class="message ai-message">
            Hello, I'm your AI therapist. How are you feeling today?
        </div>
    </div>
    <div class="input-container">
        <input type="text" id="user-input" placeholder="Type your message here...">
        <button id="send-btn">Send</button>
        <button id="reset-btn" class="reset-btn">Reset Chat</button>
    </div>

    <script src="{{ url_for('static', filename='js/chat.js') }}"></script>
</body>
</html>
'''

# Create styles.css
styles_css = '''body {
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f5f5f5;
}

.chat-container {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    padding: 20px;
    height: 500px;
    overflow-y: auto;
    margin-bottom: 20px;
}

.message {
    margin-bottom: 15px;
    padding: 10px 15px;
    border-radius: 18px;
    max-width: 70%;
}

.user-message {
    background-color: #e3f2fd;
    margin-left: auto;
    text-align: right;
}

.ai-message {
    background-color: #f1f1f1;
}

.input-container {
    display: flex;
    gap: 10px;
}

#user-input {
    flex-grow: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

button {
    padding: 10px 15px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

h1 {
    color: #333;
    text-align: center;
}

.reset-btn {
    background-color: #f44336;
}

.reset-btn:hover {
    background-color: #d32f2f;
}
'''

# Create chat.js
chat_js = '''document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.getElementById('chat-container');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const resetBtn = document.getElementById('reset-btn');

    function addMessage(message, isUser) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(isUser ? 'user-message' : 'ai-message');
        messageDiv.textContent = message;
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        addMessage(message, true);
        userInput.value = '';
        userInput.disabled = true;
        sendBtn.disabled = true;

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
            
            if (data && data.response) {
                addMessage(data.response, false);
            } else {
                addMessage("Sorry, I received an empty response. Please try again.", false);
            }
        } catch (error) {
            console.error('Error:', error);
            addMessage('Sorry, there was an error processing your request.', false);
        } finally {
            userInput.disabled = false;
            sendBtn.disabled = false;
            userInput.focus();
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
create_file('static/css/styles.css', styles_css)
create_file('static/js/chat.js', chat_js)

print("\nSetup complete! Run the application with: python app.py") 