from Waifu import *
from Waifu.functions.harem_db import *
from pyrogram import *
from pyrogram.types import *


@Client.on_message(filters.command(["simp","simps","topusers","top","ranking"]) & filters.group)
async def ranking(client,message):
    temp = await message.reply_text("**fetching simps....**")
    chat_id = message.chat.id
    data = await grpharem(chat_id)
    text = "⛩️♪ • Leaderboard • ♪⛩️\n\n"
    for index, (user_id, count) in enumerate(data, start=1):
        user = await client.get_users(int(user_id))
        text += f"{index}. {user.mention} • {count}\n"
    keyboard = [
        [InlineKeyboardButton("⛩️ Global ⛩️", callback_data='globharem')],
    ]
    await temp.delete()
    return await message.reply_photo(photo="https://graph.org//file/c7fcf29877e07d1c4c2f2.png",caption=text,reply_markup=InlineKeyboardMarkup(keyboard))
