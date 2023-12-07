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
        return await message.reply_text("Sorry darling you haven't hunted any waifu 👀✨")
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
    if query.from_user.id == 1242173932:
        return
    if query.query.startswith("user_data_inline."):
        user_id = query.query[17:]
        user = await is_player(user_id)
        try:
            first = (await app.get_users(int(user_id))).first_name
        except:
            first = "User"
        if user:
            character_data = await is_player(user_id)
            results = []
            for item in character_data:
                character_id, user_id, character_name, anime, rarity, character_pic, count = item
                caption = f"✨OwO! Check out {first}'s harem\n\n🆔: {character_id}\n💮 Waifu: {character_name} x{count}\n🌅 Anime:{anime}\n🎌 Rarity : {rarity}"
                results.append(InlineQueryResultPhoto(
                    photo_url=character_pic,
                    thumb_url=character_pic,
                    caption=caption
                ))
            total_results = len(results)
            current_page = int(query.offset) if query.offset else 0
            items_per_page = 50
            next_offset = current_page + items_per_page if current_page + items_per_page < total_results else None
            await query.answer(results[current_page:current_page+items_per_page], cache_time=0, is_gallery=True, next_offset=str(next_offset))
        else:
            message = "You have no characters."
            await query.answer([InlineQueryResultArticle(
                title="Not Found",
                input_message_content=InputTextMessageContent(message)
            )], cache_time=0)
    elif query.query.lower().startswith("chri"):
        cursor.execute("SELECT * FROM winter_characters")
        fetched = cursor.fetchall()
        results = []
        for rex in fetched:
            id,name,anime,rarity,pic = rex
            cap = "**OwO! Check out this qt waifu!\n\n**"
            cap += f"**🌅{anime}\n**"
            cap += f"**💮 Name : {name}\n**"
            cap += f"**🫧 Rarity : {rarity}\n**"
            results.append(InlineQueryResultPhoto(
                photo_url=pic,
                thumb_url=pic,
                caption=cap
            ))
        total_results = len(results)
        current_page = int(query.offset) if query.offset else 0
        items_per_page = 50
        next_offset = current_page + items_per_page if current_page + items_per_page < total_results else None
        await query.answer(results[current_page:current_page+items_per_page], cache_time=0, is_gallery=True, next_offset=str(next_offset))
    else:
        cursor.execute("SELECT * FROM character_db")
        fetched = cursor.fetchall()
        results = []
        for rex in fetched:
            id,name,anime,rarity,pic = rex
            BUTT = InlineKeyboardMarkup([[InlineKeyboardButton(text="❓ Who is this waifu ❓",callback_data=f"wdata.{id}.{query.from_user.id}"),]])
            cap = "**OwO! Check out this qt waifu!\n\n**"
            cap += f"**🌅{anime}\n**"
            cap += f"**🫧 Rarity : {rarity}\n**"
            results.append(InlineQueryResultPhoto(
                photo_url=pic,
                thumb_url=pic,
                caption=cap,
                reply_markup=BUTT
            ))
        total_results = len(results)
        current_page = int(query.offset) if query.offset else 0
        items_per_page = 50
        next_offset = current_page + items_per_page if current_page + items_per_page < total_results else None
        await query.answer(results[current_page:current_page+items_per_page], cache_time=0, is_gallery=True, next_offset=str(next_offset))
    
            

@app.on_callback_query(filters.regex(r"^wdata."))
async def caller_data(client,query):
    data = query.data
    id = data.split(".")[1]
    user_id = data.split(".")[2]
    if query.from_user.id != int(user_id):
        return await query.answer("You can't use others inline.",show_alert=True)
    cursor.execute("SELECT * FROM character_db WHERE id = %s",(id,))
    results = cursor.fetchone()
    name = results[1]
    anime = results[2]
    rarity = results[3]
    text = f"""🎆 Anime:{anime}
    💮 Name : {name}
    🫧 Rarity : {rarity}"""
    return await query.answer(text,show_alert=True)





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
