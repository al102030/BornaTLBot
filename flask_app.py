from flask import Flask, request, Response
from TLMethods import Methods


url = "al102030.pythonanywhere.com"
Methods.remove_webhook()
Methods.set_webhook(url)

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id = msg['message']['chat']['id']
        txt = msg['message']['text']
        Methods.send_message(txt, chat_id)
        return Response('ok', status=200)
    else:
        return '<h1>No OK</h1>'
