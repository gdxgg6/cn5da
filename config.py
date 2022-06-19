import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "18520864"))
API_HASH = os.getenv("API_HASH", "038099d49ddd4b70bb672d00838bad82")
SESSION = os.getenv("SESSION", "AQBj-MgJZ0fIRgA0L-OcqhiwaeSB2Uy6JEkkb-3fNL8sBRXjUZBSWpWYk-zlnrAeqZgNgzkD7k0mq1cbVzjbhH6UCasrGAkSmruQQDkj0L0QIvYQ3DU1x7okZAzeICtirdcQJyRACeNv1SNv2ahtpMfsLhdfs_8_5iDk9KWkgt8ayAFW1-kS0V26aPhqUgNvmHx0qwNmf2XEEVg-gJPox-GAOvzz691vk0LeOOU_ihkh4oajqYUFIvez9fjqhCSqrDKAcqGhmocANZHQAxIwRonchg7Ama_Gylhyzjq0SSBd6wVkGzLzBSG2wy8jsUtXTJW4x0isYj00qU5J13P99YhqAAAAAU1wAoQA")
HNDLR = os.getenv("HNDLR", ".")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "5266209266").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicRioUserbot"))
call_py = PyTgCalls(bot)
# © 2022 GitHub, Inc.
# Terms
# Privacy
# Security
