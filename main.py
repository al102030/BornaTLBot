from TLBot.Methods import Methods
from config.token import token


if __name__ == "__main__":
    # secret = "jlg754bvjhv9k8bmvfd"
    # url = "al102030.pythonanywhere.com"
    bot_method = Methods(token)
    bot_method.send_message("ok", "112042461")
    # print(bot_method.send_video(".mp4", "112042461"))
