from TLBot.Methods import Methods
from config.token import token


if __name__ == "__main__":
    # secret = "jlg754bvjhv9k8bmvfd"
    # url = "al102030.pythonanywhere.com"
    photo = "https://img.freepik.com/premium-vector/young-girl-anime-style-character-vector-illustration-design-manga-anime-girl_147933-100.jpg?w=740"
    bot_method = Methods(token)
    print(bot_method.send_photo("112042461", photo, "ok").text)
    # bot_method.send_message("ok", "112042461")
    # print(bot_method.send_video(".mp4", "112042461"))
