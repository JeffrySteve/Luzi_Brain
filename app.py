from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Load FAQ data once
with open('faq.json', encoding='utf-8') as f:
    faq_data = json.load(f)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message', '').lower()
    response = "Sorry, I don't understand that yet."

    for keyword, answer in faq_data.items():
        if keyword in user_message:
            response = answer
            break

    return jsonify({'response': response})

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
