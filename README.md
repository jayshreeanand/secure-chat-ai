# SecureChat AI

<img width="357" alt="Screenshot 2025-03-01 at 8 54 13 PM" src="https://github.com/user-attachments/assets/8bc2968d-317a-45f7-a09a-13f44bb9f7ae" />


## Overview

SecureChat AI is a secure, privacy-focused chat application powered by AI and built on the Secret Network. It provides end-to-end encrypted communication with intelligent AI assistance while maintaining the highest standards of privacy and security.

<img width="1252" alt="Screenshot 2025-03-01 at 8 52 36 PM" src="https://github.com/user-attachments/assets/dc894475-1135-43ed-880c-9630df1c9400" />


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

## Screenshots

Home Page
<img width="1654" alt="Screenshot 2025-03-01 at 8 43 42 PM" src="https://github.com/user-attachments/assets/215dfa49-2f7a-4169-b594-e59403671fac" />

Features
<img width="1680" alt="Screenshot 2025-03-01 at 8 43 52 PM" src="https://github.com/user-attachments/assets/f2f66d2f-1d9b-493c-9f33-1d535f284f65" />

<img width="1640" alt="Screenshot 2025-03-01 at 8 57 05 PM" src="https://github.com/user-attachments/assets/a38b6fb7-5c3c-44af-af8d-bd4bd8a27ddb" />

Chat Window
<img width="1187" alt="Screenshot 2025-03-01 at 8 52 50 PM" src="https://github.com/user-attachments/assets/82624fd4-a8d9-41d0-bcf2-8c355866c7c0" />
<img width="1252" alt="Screenshot 2025-03-01 at 8 52 36 PM" src="https://github.com/user-attachments/assets/670a93c6-387a-46da-9581-7ef03f10e18b" />

###Use Cases
- Personal Privacy-Focused Chat – Communicate securely without exposing personal data.
- Business Communications – Enable confidential discussions without risk of data leakage.
- Anonymous Therapy & Support – Offer encrypted mental health or crisis support services.
- Decentralized Customer Support – Automate customer service while ensuring private user interactions.
- Whistleblower & Anonymous Reporting – Report misconduct securely with no identity trace.
- Decentralized Work Collaboration – Enable private team discussions for sensitive projects.

## Getting Started



### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- 
#### Install Requirements
To follow along with the guide, we will be using Anaconda and Python 3.12. 

Install Anaconda for Windows, Mac, or Linux.

Clone the Secret AI getting started repository here:


```git clone https://github.com/SecretFoundation/secret-ai-getting-started.git```
Create Anaconda virtual environment
In your text editor, create an Anaconda virtual environment with Python 3.12:


```conda create -n menv python=3.12```
Activate the virtual environment: 


```conda activate menv```
Install Secret AI dependencies

```pip install -r requirements.txt && pip install 'secret-sdk>=1.8.1' && pip install secret-ai-sdk```
Set developer key

```export SECRET_AI_API_KEY=YOUR API KEY```

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

