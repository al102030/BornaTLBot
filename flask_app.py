import json
import requests
from flask import Flask, request, Response
# from TLMethods import Methods


# secret = "jlg754bvjhv9k8bmvfd"
# url = "al102030.pythonanywhere.com"+secret
# Methods.remove_webhook()
# Methods.set_webhook(url)


def write_json(data, filename='response.json'):
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# def parse_message(message):
#     chat_id = message['message']['chat']['id']
#     txt = message['message']['text']


def send_message(text, chat_id):
    req_url = "https://api.telegram.org/bot6235055313:AAFWlbsqG3Ck3wP6_dwKjXHZdGRBuxBuSn0/sendMessage"
    payload = {
        "text": text,
        "chat_id": chat_id,
        "disable_web_page_preview": False,
        "disable_notification": False,
        "reply_to_message_id": None
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    response = requests.post(req_url, json=payload,
                             headers=headers, timeout=10)
    return response


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        # write_json(msg, '1.json')
        chat_id = msg['message']['chat']['id']
        txt = msg['message']['text']
        send_message(txt, chat_id)
        return Response('ok', status=200)
    else:
        return '<h1>No OK</h1>'
