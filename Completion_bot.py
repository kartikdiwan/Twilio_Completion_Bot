import os
from flask import Flask, request
import requests as req
from twilio.twiml.messaging_response import MessagingResponse
import openai

key = 'sk-1234567890xx...wehfb'
path = "D:\Python Projects\Open AI\OPENAI_API_KEY.txt"

#openai.api_key = key
#openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key_path = path

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    resp = MessagingResponse()
    msg = resp.message()
    prompt_var = request.values.get('Body', '').lower()
    
    response = openai.Completion.create(
    model="text-ada-001",
    prompt = prompt_var,
    max_tokens=256
    )
    msg.body(response.get("choices")[0].get("text"))
    return str(resp)

if __name__ == '__main__':
    app.run(port=4000)
