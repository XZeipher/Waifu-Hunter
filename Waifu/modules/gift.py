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

from Waifu import *
from Waifu.functions.watch_db import *
from pyrogram import *
from pyrogram.types import *



@Client.on_message(filters.command("gift") & filters.group)
async def gifting(client,message):
    try:
        id = message.text.split(maxsplit=1)[1]
    except:
        return await message.reply_text("provide an waifu id")
    if not int(id):
        return await message.reply_text("provide valid id")
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("reply to an user to gift waifus")
    replied_user = message.reply_to_message.from_user
    check = await select(int(id))
    if not check:
        return await message.reply_text("Waifu with this ID doesn't exists")
    for info in check:
        ids,user_id,name,anime,rarity,pic,count = info
    if int(user_id) != message.from_user.id:
        return await message.reply_text(f"You don't have {name}\nso you can't gift it yet!")
    confirmation_text = f"Are you sure you want to gift {name} to {replied_user.mention}?"
    confirmation_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("Yes", callback_data=f"confirmgift_{user_id}_{id}_{replied_user.id}")],
            [InlineKeyboardButton("No", callback_data=f"cancel_{user_id}")]
        ])
    return await message.reply_photo(photo="https://graph.org//file/cd9dadc930fc140623377.png",caption=confirmation_text,reply_markup=confirmation_markup)

@app.on_callback_query(filters.regex(r"^cancel_"))
async def cancel(client,query):
    data = query.data
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    user_ids = data.split("_")[1]
    if int(user_ids) != user_id:
        return await query.answer("Sorry dear,\nbut this isn't your waifu.",show_alert=True)
    return await query.edit_message_caption("**Cancelled ❌**")

@app.on_callback_query(filters.regex(r"^confirmgift_"))
async def confim_fuf(client,query):
    data = query.data
    user_ids = data.split("_")[1]
    replied_id = data.split("_")[3]
    chat_id = query.message.chat.id
    ids = data.split("_")[2]
    check = await select(int(ids))
    if int(user_ids) != query.from_user.id:
        return await query.answer("Sorry dear,\nbut this isn't your waifu.",show_alert=True)
    for info in check:
        id,user_id,name,anime,rarity,pic,count = info
    trying = await decrease(user_id,pic)
    if not trying:
        await delete(user_id,name,anime,rarity,pic,count)
    trying2 = await updaters(replied_id,pic)
    if not trying2:
        await insert(replied_id,name,anime,rarity,pic,count)
    return await query.edit_message_caption(f"**✅ {name} Gifted Successfully.**")
