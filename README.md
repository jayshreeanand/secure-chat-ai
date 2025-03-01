# SecureChat AI

![SecureChat AI Logo](static/images/logo.png)

## Overview

SecureChat AI is a secure, privacy-focused chat application powered by AI and built on the Secret Network. It provides end-to-end encrypted communication with intelligent AI assistance while maintaining the highest standards of privacy and security.

## Features

- **End-to-End Encryption**: All messages are encrypted on your device and can only be decrypted by the intended recipient.
- **AI-Powered Assistance**: Intelligent responses powered by Secret AI technology.
- **Privacy-First Design**: No message storage on centralized servers - your conversations remain private.
- **Secret Network Integration**: Built on the Secret Network, a privacy-focused blockchain that enables confidential smart contracts and secure data processing.
- **User-Friendly Interface**: Clean, intuitive design for seamless communication.
- **No Registration Required**: Start chatting instantly without creating an account.
- **Cross-Platform Compatibility**: Access from any device with a web browser.

## Technology Stack

- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Backend**: Python, Flask
- **AI**: Secret AI SDK
- **Security**: Secret Network, end-to-end encryption

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/securechat-ai.git
   cd securechat-ai
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   ```bash
   # Create a .env file with your Secret AI API keys
   touch .env
   # Add the following to the .env file:
   # SECRET_AI_API_KEY=your_api_key_here
   ```

5. Run the application:

   ```bash
   python app.py
   ```

6. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure
