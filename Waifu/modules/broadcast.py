from Waifu import *
from config import OWNER_ID
from pyrogram import *


@Client.on_message(filters.command("bcast") & filters.user(OWNER_ID))
async def bcast(client,message):
    cursor.execute("SELECT chat_id FROM chats_db")
    chats = cursor.fetchall()
    for chat in chats:
        try:
            msg = await message.reply_to_message.forward(int(chat[0]))
            try:
                await msg.pin()
            except:
                continue
        except:
            continue
    cursor.execute("SELECT user_id FROM users_db")
    users = cursor.fetchall()
    for user in users:
        try:
            await message.reply_to_message.forward(int(user[0]))
        except:
            continue
    return
