import requests


class Methods:
    def __init__(self, tltoken):
        self.token = tltoken

    def get_me(self):
        url = f"https://api.telegram.org/bot{self.token}/getMe"

        headers = {"accept": "application/json"}

        response = requests.post(url, headers=headers, timeout=20)

        return response

    def get_update(self):
        url = f"https://api.telegram.org/bot{self.token}/getUpdates"
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        payload = {
            "offset": None,
            "timeout": None
        }
        response = requests.post(
            url, json=payload, headers=headers, timeout=20)
        return response

    def send_message(self, text, chat_id):
        req_url = f"https://api.telegram.org/bot{self.token}/sendMessage"
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
                                 headers=headers, timeout=20)
        return response

    def forward_message(self, message_id, chat_id, from_chat_id):

        url = f"https://api.telegram.org/bot{self.token}/forwardMessage"

        payload = {
            "message_id": message_id,
            "disable_notification": False,
            "chat_id": chat_id,
            "from_chat_id": from_chat_id
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response

    def send_photo(self, chat_id, photo, caption=""):

        url = f"https://api.telegram.org/bot{self.token}/sendPhoto"

        payload = {
            "photo": photo,
            "caption": caption,
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id": chat_id
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response

    def set_webhook(self, host_link):

        url = f"https://api.telegram.org/bot{self.token}/setWebhook"

        payload = {
            "url": host_link,
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response

    def remove_webhook(self):

        url = f"https://api.telegram.org/bot{self.token}/setWebhook?remove="

        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(url, headers=headers, timeout=20)

        return response

    def send_video(self, pth, chat_id, caption=""):
        url = f"https://api.telegram.org/bot{self.token}/sendVideo"

        my_file = open(pth, 'rb')

        parameters = {
            "caption": caption,
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id": chat_id
        }
        files = {
            "video": my_file,
        }

        response = requests.post(url, data=parameters, files=files, timeout=30)

        return response.text

    def send_audio(self, pth, chat_id, caption=""):

        url = f"https://api.telegram.org/bot{self.token}/sendAudio"

        my_file = open(pth, 'rb')
        parameters = {
            "caption": caption,
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id": chat_id
        }
        files = {
            "audio": my_file
        }

        response = requests.post(url, data=parameters, files=files, timeout=30)

        return response.text

    def send_document(self, pth, chat_id, caption=""):

        url = f"https://api.telegram.org/bot{self.token}/sendDocument"

        my_file = open(pth, 'rb')
        parameters = {
            "caption": caption,
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id": chat_id
        }
        files = {
            "document": my_file
        }

        response = requests.post(url, data=parameters, files=files, timeout=30)

        return response.text

    def send_sticker(self, sticker, chat_id):

        url = f"https://api.telegram.org/bot{self.token}/sendSticker"

        payload = {
            "sticker": sticker,
            "chat_id": chat_id,
            "disable_notification": False,
            "reply_to_message_id": None
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response.text

    def send_voice(self, voice, chat_id):

        url = f"https://api.telegram.org/bot{self.token}/sendVoice"

        payload = {
            "voice": voice,
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id": chat_id
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response.text

    def send_location(self, lat, lan, chat_it):

        url = f"https://api.telegram.org/bot{self.token}/sendLocation"

        payload = {
            "latitude": lat,
            "longitude": lan,
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id": chat_it
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response.text

    # typing, upload_photo, record_video, upload_video, record_video_note, upload_video_note
    # record_voice, upload_voice, upload_document, choose_sticker, find_location

    def send_chat_action(self, action, chat_id):

        url = f"https://api.telegram.org/bot{self.token}/sendChatAction"

        payload = {
            "action": action,
            "chat_id": chat_id
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        print(response.text)

    def get_user_profile_photos(self, user_id):

        url = f"https://api.telegram.org/bot{self.token}/getUserProfilePhotos"

        payload = {
            "user_id": user_id,
            "offset": None,
            "limit": None
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response.text

    def get_file(self, file_id):

        url = f"https://api.telegram.org/bot{self.token}/getFile"

        payload = {
            "file_id": file_id}
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, json=payload, headers=headers, timeout=20)

        return response.text

    def download_file(self, file_path):
        url = f"https://api.telegram.org/file/bot{self.token}/{file_path}"

        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(
            url, headers=headers, timeout=20)

        return response.text
