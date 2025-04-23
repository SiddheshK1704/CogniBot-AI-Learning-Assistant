from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

# Basic greeting responses for the chatbot
greeting_patterns = {
    "hello": ["Hello! How can I help you today?", "Hi there! What can I assist you with?"],
    "hi": ["Hi! How can I help you today?", "Hello there! What can I do for you?"],
    "hey": ["Hey! What can I do for you today?", "Hello! How can I assist you?"],
    "good morning": ["Good morning! How can I help you start your day?"],
    "good afternoon": ["Good afternoon! What can I help you with today?"],
    "good evening": ["Good evening! How can I assist you tonight?"],
    "how are you": ["I'm doing well, thank you! How can I help you?", "I'm functioning perfectly! How can I assist you today?"],
    "thanks": ["You're welcome!", "Glad I could help!", "No problem!"],
    "thank you": ["You're welcome! Let me know if you need anything else.", "Anytime! Happy to help."],
    "bye": ["Goodbye! Feel free to chat again anytime.", "See you later! Have a great day!"],
    "goodbye": ["Bye! Come back if you have more questions.", "Goodbye! It was nice chatting with you."]
}

# General responses for when no specific pattern is matched
general_responses = [
    "That's interesting. Could you tell me more?",
    "I'm here to help with your learning needs. Could you elaborate?",
    "I'm designed to assist with educational topics. What specifically would you like to know?",
    "I'm not sure I understand. Could you rephrase that?",
    "Let me think about that... Can you provide more details?"
]

@app.route('/')
def home():
    return render_template('chatbot.html')  # Serves your chatbot UI

@app.route('/send-message', methods=['POST'])
def send_message():
    user_message = request.json.get('message', '').lower().strip()
    
    if not user_message:
        return jsonify({'response': "I didn't catch that. Could you please rephrase?"})
    
    # Simulate processing time to make it feel more natural (0.5-1.5 seconds)
    time.sleep(random.uniform(0.5, 1.5))
    
    # Check for greeting patterns first
    for pattern, responses in greeting_patterns.items():
        if pattern in user_message:
            return jsonify({'response': random.choice(responses)})
    
    # If no greeting pattern matched, use a general response
    bot_response = random.choice(general_responses)
    
    return jsonify({'response': bot_response})

@app.route('/mic-status', methods=['POST'])
def mic_status():
    status = request.json.get('status')
    
    # Here you would implement actual speech recognition functionality
    # For demo purposes, we're just acknowledging the status change
    
    if status == 1:
        return jsonify({'status': 'Microphone activated'})
    else:
        return jsonify({'status': 'Microphone deactivated'})

if __name__ == '__main__':
    app.run(debug=True)