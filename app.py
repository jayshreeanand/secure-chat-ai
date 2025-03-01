from flask import Flask, render_template, request, jsonify
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
