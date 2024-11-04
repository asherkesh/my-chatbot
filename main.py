import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')  
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    return jsonify({"response": response['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
