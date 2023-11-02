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

trade_text = """
🤝 {} has sent you a trade offer!

They would like:
{}

In return, you will receive:
{}

will you accept {}?
"""


@Client.on_message(filters.command("trade") & filters.group)
async def trade(client,message):
    try:
        id1 = message.text.split()[1]
        id2 = message.text.split()[2]
    except:
        return await message.reply_text("Eg. /trade {your_character_id} {other_users_character_id}")
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("reply to an user to trade waifus")
    replied_user = message.reply_to_message.from_user
    check1 = await select(int(id1))
    if not check1:
        return await message.reply_text("Your waifu ID doesn't exists")
    check2 = await select(int(id2))
    if not check2:
        return await message.reply_text("Other User's waifu ID doesn't exists")
    for info1 in check1:
        ids1,user_id1,name1,anime1,rarity1,pic1,count1 = info1
    for info2 in check2:
        ids2,user_id2,name2,anime2,rarity2,pic2,count2 = info2
    if int(user_id1) != message.from_user.id:
        return await message.reply_text(f"You don't have {name}\nso you can't trade it yet!")
    if int(user_id2) != message.reply_to_message.from_user.id:
        return await message.reply_text(f"Other user don't have {name}\nso they can't gift it yet!")
    BUTT = InlineKeyboardMarkup([[InlineKeyboardButton("Accept", callback_data=f"accept_{replied_user.id}_{id1}_{id2}")],[InlineKeyboardButton("Reject", callback_data=f"reject_{replied_user.id}")]])
    return await message.reply_to_message.reply_photo(photo="https://graph.org//file/3a2356afe27763f8dc52d.png",caption=trade_text.format(message.from_user.mention,name2,name1,replied_user.mention),reply_markup=BUTT)


@app.on_callback_query(filters.regex(r"^reject_"))
async def reject_trade(client, query):
    data = query.data
    user = data.split("_")[1]
    if query.from_user.id != int(user):
        return await query.answer("Sorry dear you can't reject it.",show_alert=True)
    return await query.edit_message_caption("**Trade Rejected ❌**")


@app.on_callback_query(filters.regex(r"^accept_"))
async def accept_call(client,query):
    user_id = query.from_user.id
    data = query.data
    id1 = data.split("_")[2]
    id2 = data.split("_")[3]
    replied_id = data.split("_")[1]
    if user_id != int(replied_id):
        return await query.answer("You dear you can't accept it.",show_alert=True)
    user_info = await select(int(id1))
    reply_info = await select(int(id2))
    for u in user_info:
        ids1,user1,name1,anime1,rarity1,pic1,count1 = u
    for r in reply_info:
        ids2,user2,name2,anime2,rarity2,pic2,count2 = r
    trying = await decrease(user1,pic1)
    if not trying:
        await delete(user1,name1,anime1,rarity1,pic1,count1)
    trying2 = await updaters(user1,pic2)
    if not trying2:
        await insert(user1,name2,anime2,rarity2,pic2,count2)
    tryingx = await decrease(user2,pic2)
    if not tryingx:
        await delete(user2,name2,anime2,rarity2,pic2,count2)
    tryingx2 = await updaters(user2,pic1)
    if not tryingx2:
        await insert(user2,name1,anime1,rarity1,pic1,count1)
    return await query.edit_message_caption("✅🤝 Trade completed!")
