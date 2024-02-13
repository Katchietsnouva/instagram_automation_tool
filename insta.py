from instabot import Bot

try:
    bot = Bot()
    bot.login(username="pascalslaw009", password="Operapassword111gaaq7")
    # Your Instabot operations here

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up or perform any necessary tasks
    bot.logout()

# from instabot import Bot
# from instabot.exceptions import (InstaBotException, ConnectionError, RequestsError)

# try:
#     bot = Bot()
#     bot.login(username="your_username", password="your_password")

#     # Your Instabot operations here

# except InstaBotException as e:
#     print(f"InstaBotException: {e}")

# except (ConnectionError, RequestsError) as e:
#     print(f"Connection error: {e}")

# finally:
#     # Clean up or perform any necessary tasks
#     bot.logout()
