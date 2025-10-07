from flask import Flask, request, jsonify
from chatbot.logic import get_career_advice

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_career_advice(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)