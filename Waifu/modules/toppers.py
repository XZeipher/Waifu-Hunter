from Waifu import *
from Waifu.functions.harem_db import *
from pyrogram import *
from pyrogram.types import *


@Client.on_message(filters.command(["simp","simps","topusers","top","ranking"]) & filters.group)
async def ranking(client,message):
    temp = await message.reply_text("**fetching simps....**")
    chat_id = message.chat.id
    data = await grpharem(chat_id)
    picture_count = {}
    for user_data_list in data:
        for item in user_data_list:
            user_id = item[1]
            if user_id in picture_count:
                picture_count[user_id] += 1
            else:
                picture_count[user_id] = 1
    sorted_users = sorted(picture_count.items(), key=lambda x: x[1], reverse=True)
    text = "⛩️♪ • Leaderboard • ♪⛩️\n\n"
    for index, (user_id, count) in enumerate(sorted_users, start=1):
        user = await client.get_users(int(user_id))
        text += f"{index}. {user.mention} • {count}\n"
    keyboard = [
        [InlineKeyboardButton("⛩️ Global ⛩️", callback_data='globharem')],
    ]
    await temp.delete()
    return await message.reply_photo(photo="https://graph.org//file/c7fcf29877e07d1c4c2f2.png",caption=text,reply_markup=InlineKeyboardMarkup(keyboard))
