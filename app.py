from flask import Flask, request, jsonify
import google.generativeai as ai
from datetime import datetime

# Configure API key for Google generative AI
API_KEY = 'YOUR_API_KEY_HERE'  # Replace with your own API key
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel('gemini-pro')
chat = model.start_chat()

app = Flask(__name__)

# Function to handle commands
def process_command(command):
    command = command.lower()
    
    if "your name" in command:
        return "My name is Ajay."
    elif "my name" in command:
        return "I don't know your name."
    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif "bye" in command:
        return "Goodbye!"
    else:
        # If no specific commands are detected, interact with Google generative AI
        response = chat.send_message(command).text
        return response

# Route to handle voice commands from the front-end
@app.route('/process_command', methods=['POST'])
def process_command_route():
    data = request.json
    command = data.get('command', '')
    response = process_command(command)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)