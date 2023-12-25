from pyrogram import *
from Waifu import *

@Client.on_message(filters.command("ok")&filters.private)
async def asking(client,message):
    name = None
    await message.reply_text("say name")
    @Client.on_message(filters.user(message.from_user.id) & filters.private)
    async def get_name(_,msg):
        if msg.text:
            name = msg.text
    if name is None:
        return await message.reply_text("give name bruh")
    return await message.reply_text(f"Your name is - {name}")
