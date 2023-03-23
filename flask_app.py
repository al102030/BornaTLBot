from flask import Flask, request, Response
from TLBot.Methods import Methods
from config.token import token


url = "al102030.pythonanywhere.com"
bot_methods = Methods(token)
bot_methods.remove_webhook()
bot_methods.set_webhook(url)

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id = msg['message']['chat']['id']
        # txt = msg['message']['text']
        from_chat_id = msg['message']['from']['id']
        message_id = msg['message']['message_id']
        bot_methods.forward_message(message_id, chat_id, from_chat_id)
        return Response('ok', status=200)
    else:
        return '<h1>No OK</h1>'
