from Waifu import app
from pyrogram import Client , filters
from Waifu import cursor as cusr , DATABASE as DB

@Client.on_message(filters.command("stats") & filters.user([6393014348,6227314727]))
async def stats(client,message):
    text = "Users : {}\nChats : {}"
    cusr.execute("SELECT * FROM chats_db")
    chats = len(cusr.fetchall())
    cusr.execute("SELECT * FROM users_db")
    users = len(cusr.fetchall())
    return await message.reply_text(text.format(users,chats))
