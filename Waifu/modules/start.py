"""
MIT License

Copyright (c) 2023 XZeipher

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from Waifu import app,BOT_NAME
from Waifu.functions.stats_db import add_user
from pyrogram import Client , filters
from pyrogram.types import *
from pyrogram.enums import ChatType

new_user = """
{} 
#NEWUSER
User : {}
"""


@Client.on_message(filters.command("start"))
async def start(client,message):
    user_id = message.from_user.id
    BUTT = [
        [
            InlineKeyboardButton("Updates ⚕️", url="https://t.me/WaifuHunterUpdates"),
            InlineKeyboardButton("Support 🆘", url="https://t.me/WaifuHunterSupport"),
        ],
        [
            InlineKeyboardButton("➕ Add Me To Your Group ➕", url="http://t.me/WaifuHunterXBot?startgroup=True"),
        ],
    ]
    bot = await app.get_me()
    name = bot.first_name
    if message.chat.type != ChatType.PRIVATE:
        TEXT = f"""Hi! I'm {name} , If you want , I can send lustrous waifus in the group just for you.

📥 get your waifu on bed by guessing their names using /protecc name"""
    else:
        user = await add_user(user_id)
        if user:
            await app.send_message(-1002103089465,new_user.format(name,message.from_user.mention))
        TEXT = f"Hey {message.from_user.mention}, I know you can't wait to be with your favourite waifus but I only function in a group , so add me there and watch the magic."
    return await message.reply_photo(photo="https://graph.org//file/e6143909bef2d121d6407.png",caption=TEXT,reply_markup=InlineKeyboardMarkup(BUTT))
    
