from pyrogram import *
from Waifu import *
import asyncio

@Client.on_message(filters.command("ok")&filters.private)
async def asking(client,message):
    name = None
    count = 0
    await message.reply_text("say name")
    @Client.on_message(filters.text & filters.user(message.from_user.id) & filters.private)
    async def get_name(_,msg):
        while not msg.text:
            if count == 15:
                break
            count += 1
            await asyncio.sleep(1)
        if msg.text:
            name = msg.text
        else:
            return await message.reply_text("give name bruh")
    if name is None:
        return await message.reply_text("cry bro timeout")
    return await message.reply_text(f"Your name is - {name}")
