import requests
from config.token import token


def get_update():
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    payload = {
        "offset": None,
        "timeout": None
    }
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    return response


def send_message(text, chat_id):
    req_url = f"https://api.telegram.org/bot{token}/sendMessage"
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


def set_webhook(host_link):

    url = f"https://api.telegram.org/bot{token}/setWebhook"

    payload = {
        "url": host_link,
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers, timeout=10)

    return response


def remove_webhook():

    url = f"https://api.telegram.org/bot{token}/setWebhook?remove="

    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, headers=headers, timeout=10)

    return response


def send_video(pth, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendVideo"

    my_file = open(pth, 'rb')

    parameters = {
        "caption": "Your file downloaded!",
        "disable_notification": False,
        "reply_to_message_id": None,
        "chat_id": chat_id
    }
    files = {
        "video": my_file,
    }

    response = requests.post(url, data=parameters, files=files, timeout=50)

    print(response.text)
