from pyrogram import Client,filters
from Waifu import *
#from Waifu.functions import *

@Client.on_message(filters.command("events"))
async def event_manager(client,message):
    if message.from_user.id not in [6158616242,6761575762,6910848942]:
        return await message.reply_text("**Sorry bot developers can use this command.**")
