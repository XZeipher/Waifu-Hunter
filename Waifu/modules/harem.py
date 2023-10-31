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
    return await is_player(user_id)

@Client.on_message(filters.command("harem"))
async def harem(client, message):
    user_id = message.from_user.id
    user_current_pages[user_id] = 1
    all_user_characters = await get_user_characters(user_id)
    if not all_user_characters:
        return await message.reply_text("Sorry darling you haven't protecc'd any waifu 👀✨")
    result = await characters(str(user_id), page=1, characters_per_page=10)
    
    harem_text = f"**👑 {message.from_user.mention}'s Harem (Page 1)\n\n**"
    for item in result:
        id, user_id, name,anime,rarity, pic ,count= item
        if user_id not in user_data:
            user_data[user_id] = {"pics": []}
        user_data[user_id]["pics"].append(pic)
        harem_text += f"**🌅{anime}-**"
        harem_text += "**⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋\n**"
        harem_text += f"**🆔 {id} |🫧 {rarity} |💮 {name} [👀] x{count}\n**"
        harem_text += "**⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋\n\n**"

    inline_buttons = [
        InlineKeyboardButton("Harem 👑", switch_inline_query_current_chat=f"user_data_inline.{user_id}")
    ]
    inline_buttons.append(InlineKeyboardButton("➡️", callback_data="next_page"))
    reply_markup = InlineKeyboardMarkup([inline_buttons])
    await message.reply_photo(user_data[user_id]["pics"][0], caption=harem_text, reply_markup=reply_markup)
    user_data.pop(user_id)


async def handle_inline_query(query):
    if query.query.startswith("user_data_inline."):
        user_id = query.query[17:]
        user = await is_player(user_id)
        if user:
            character_data = await is_player(user_id)
            results = []
            for item in character_data:
                character_id, user_id, character_name,anime,rarity, character_pic,count = item
                caption = f"✨OwO! Check out {query.from_user.mention}'s harem\n\n🆔: {character_id}\n💮 Waifu: {character_name} x{count}\n🌅 Anime:{anime}\n🎌 Rarity : {rarity}"
                
                results.append(InlineQueryResultPhoto(
                    photo_url=character_pic,
                    thumb_url=character_pic,
                    caption=caption
                ))
            await query.answer(results, cache_time=0, is_gallery=True)
        else:
            message = "You have no characters."
            await query.answer([InlineQueryResultArticle(
                title="Not Found",
                input_message_content=InputTextMessageContent(message)
            )], cache_time=0)

@app.on_inline_query()
async def inline_query(client, query):
    await handle_inline_query(query)

@app.on_callback_query(filters.regex(r"^(next_page|prev_page)$"))
async def page_inline(client, query):
    data = query.data
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    current_page = user_current_pages.get(user_id, 1)
    if user_id != query.message.reply_to_message.from_user.id:
        return await query.answer("Soory darling 👀 but it's not your harem.",show_alert=True)

    if data == "next_page":
        current_page += 1
    elif data == "prev_page" and current_page > 1:
        current_page -= 1

    result = await characters(str(user_id), page=current_page, characters_per_page=10)

    if result:
        harem_text = f"**👑 {query.from_user.mention}'s Harem (Page {current_page})\n\n**"
        for item in result:
            id, user_id, name, anime,rarity,pic,count = item
            if user_id not in user_data:
                user_data[user_id] = {"pics": []}
            harem_text += f"**🌅{anime}-**"
            harem_text += "**⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋\n**"
            harem_text += f"**🆔 {id} |🫧 {rarity} |💮 {name} [👀] x{count}\n**"
            harem_text += "**⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋\n\n**"

        inline_buttons = []

        if current_page > 1:
            inline_buttons.append(InlineKeyboardButton("«", callback_data="prev_page"))

        if await characters(str(user_id), page=current_page + 1, characters_per_page=2):
            inline_buttons.append(InlineKeyboardButton("»", callback_data="next_page"))

        if current_page == 1:
            inline_buttons.append(InlineKeyboardButton("Harem 👑", switch_inline_query_current_chat=f"user_data_inline.{user_id}"))

        reply_markup = InlineKeyboardMarkup([inline_buttons])
        await client.edit_message_caption(chat_id, query.message.id, harem_text, reply_markup=reply_markup)
        user_current_pages[user_id] = current_page
    else:
        await query.answer("You have no more waifus darling.", show_alert=True)
