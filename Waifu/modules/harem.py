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

import random, asyncio
from Waifu import *
from pyrogram import *
from pyrogram.types import *
from Waifu.functions.char_db import *

user_data = {}
current_page = 1
user_current_pages = {}

async def get_user_characters(user_id):
    return await char(user_id)

@Client.on_message(filters.command(["harem","simp","simps"]))
async def harem(client, message):
    user_id = message.from_user.id
    user_current_pages[user_id] = 1
    all_user_characters = await get_user_characters(user_id)
    if not all_user_characters:
        return await message.reply_text("Sorry darling you haven't protecc'd any waifu 👀✨")
    result = await characters(str(user_id), page=1, characters_per_page=10)

    harem_text = f"**👑 {message.from_user.mention}'s Harem (Page 1)\n\n**"
    harem_text += "**⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋\n**"
    for item in result:
        id, user_id, name,anime,rarity, pic ,count= item
        if user_id not in user_data:
            user_data[user_id] = {"pics": []}
        user_data[user_id]["pics"].append(pic)
        harem_text += f"**➥ {id} | {rarity} | {name} [👶] x{count}\n**"

    inline_buttons = [
        InlineKeyboardButton("Harem 👑", switch_inline_query_current_chat=f"user_data_inline.{user_id}")
    ]
    inline_buttons.append(InlineKeyboardButton("➡️", callback_data="next_page"))
    reply_markup = InlineKeyboardMarkup([inline_buttons])
    await message.reply_photo(user_data[user_id]["pics"][0], caption=harem_text, reply_markup=reply_markup)
    user_data.pop(user_id)
