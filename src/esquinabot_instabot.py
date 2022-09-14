from dotenv import dotenv_values
from instabot import Bot

config = dotenv_values()

bot = Bot()
bot.login(
    username=config.get("USERNAME"),
    password=config.get("PASSWORD")
)

# ToDo: Get it from a list, randomly
bot.upload_photo(
    "photo.jpg",
    caption="hello how are you #bot #rom"
)