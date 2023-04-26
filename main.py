from TLBot.Methods import Methods
from config.token import token


if __name__ == "__main__":
    bot_method = Methods(token)
    print(bot_method.get_user_profile_photos("11111111"))
