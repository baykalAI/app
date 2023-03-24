import openai
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

@app.route('/webhook', methods=['POST'])
def webhook():
    # Gelen mesajı alın ve işleyin
    incoming_message = request.form.get('Body')

    # ChatGPT API'sini kullanarak cevap alın
    response_message = generate_response(incoming_message)

    # Cevabı Twilio ile geri gönderin
    twilio_response = MessagingResponse()
    twilio_response.message(response_message)
    return str(twilio_response)

if __name__ == '__main__':
    app.run(debug=True)
