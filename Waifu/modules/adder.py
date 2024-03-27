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

import random
import string
from Waifu import *
from Waifu.functions.watch_db import new_code
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyromod import listen
from pyromod.listen.message import Message
from pyromod.helpers import ikb
from telegraph import Telegraph , upload_file
import psycopg2

cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_db (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        anime TEXT NOT NULL,
        rarity TEXT NOT NULL,
        pic TEXT NOT NULL
    )
""")
DATABASE.commit()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pending_task (
        id SERIAL PRIMARY KEY,
        username TEXT NOT NULL,
        key TEXT NOT NULL,
        name TEXT NOT NULL,
        anime TEXT NOT NULL,
        rarity TEXT NOT NULL,
        pic TEXT NOT NULL
    )
""")
DATABASE.commit()
telegraph = Telegraph()
new_user = telegraph.create_account(short_name="WaifuBot")
auth_url = new_user["auth_url"]
PROCESS = {}
keyboard = ikb([
    [('Common 🟢', 'common_rr'), ('Rare 🟣', 'rare_rr')],
    [('Legendary 🟡', 'legend_rr')]
])
pending = """
```Terminal
📸 {} requested to upload waifu
```
🌟 **Name ➔ {}**
🎬 **Anime ➔ {}**
💎 **Rarity ➔ {}**"""
create = """
```Terminal
📸 {}
```
🌟 **Name ➔ {}**
🎬 **Anime ➔ {}**
💎 **Code ➔** `{}`"""


@Client.on_message(filters.command("upload") & filters.private & filters.user(AUTH_USERS))
async def adder(client , message:Message):
    user_id = message.from_user.id
    bot = message.chat
    rarity = None
    try:
        response = await bot.ask('**Send The Waifu Picture 🖼️**',filters=filters.photo)
        down = await response.download()
        name = await bot.ask('**Send The Waifu Name 📛**',filters=filters.text)
        pic = upload_file(down)
        anime = await bot.ask('**Send The Waifu Anime Name 💮**',filters=filters.text)
        link = f"https://graph.org{pic[0]}"
        rare = await client.send_message(chat_id=user_id,text='**Choose Waifu Rarity 🌀**',reply_markup=keyboard)
        selection = await rare.wait_for_click(from_user_id=user_id)
        data = selection.data
        if data == 'common_rr':
            rarity = "🟢 Common"
        elif data == 'rare_rr':
            rarity = "🟣 Rare"
        elif data == 'legend_rr':
            rarity = "🟡 Legendary"
        await rare.edit_text('**Uploading....**')
        key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        cursor.execute("INSERT INTO pending_task (username , key , name , anime , rarity , pic) VALUES (%s , %s , %s , %s , %s , %s)",(message.from_user.mention,key,f"{name.text.title() }",f" {anime.text.title()} ",rarity,link,))
        DATABASE.commit()
        cli_keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Accept ✅",callback_data=f"accept_{key}"), InlineKeyboardButton("Reject ❌",callback_data=f"reject_{key}"),]
            ]
        )
        await client.send_photo(chat_id=-1002065871628,photo=link,caption=pending.format(message.from_user.mention,name.text.title(),anime.text.title(),rarity),reply_markup=cli_keyboard) 
        return await rare.edit_text('**Your Waifu Upload Request Sent To @WaifuHunterApproval\nAdmins Will Review Your Request As Soon As Possible.**')
    except Exception as e:
        return print(str(e))


@Client.on_message(filters.command("create") & filters.private & filters.user(6761575762))
async def adder_code(client , message:Message):
    user_id = message.from_user.id
    bot = message.chat
    rarity = None
    try:
        response = await bot.ask('**Send The Waifu Picture 🖼️**',filters=filters.photo)
        down = await response.download()
        name = await bot.ask('**Send The Waifu Name 📛**',filters=filters.text)
        pic = upload_file(down)
        anime = await bot.ask('**Send The Waifu Anime Name 💮**',filters=filters.text)
        link = f"https://graph.org{pic[0]}"
        count = await bot.ask('**Send The Number of waifus 💮**',filters=filters.text)
        key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        await new_code(key,user_id,name,anime,link,count)
        await client.send_photo(chat_id=message.chat.id,photo=link,caption=create.format(message.from_user.mention,name.text.title(),anime.text.title(),key),reply_markup=cli_keyboard) 
        return
    except Exception as e:
        return print(str(e))

@app.on_callback_query(filters.regex(r"^accept_") & filters.user(OMNI_USERS))
async def adder_callback(client,query):
    data = query.data
    key = data.split("_")[1]
    mention = query.from_user.mention
    cursor.execute("SELECT * FROM pending_task WHERE key = %s",(key,))
    result = cursor.fetchone()
    name = result[3]
    anime = result[4]
    rarity = result[5]
    pic = result[6]
    cursor.execute("INSERT INTO character_db (name , anime , rarity , pic) VALUES (%s , %s , %s , %s)",(name,anime,rarity,pic,))
    DATABASE.commit()
    cursor.execute("DELETE FROM pending_task WHERE key = %s",(key,))
    DATABASE.commit()
    await query.answer()
    cap = query.message.caption.html
    return await query.edit_message_caption(f"{cap}\n\n**Accepted By {mention} ✅**")


@app.on_callback_query(filters.regex(r"^reject_") & filters.user(OMNI_USERS))
async def adder_callback(client,query):
    data = query.data
    mention = query.from_user.mention
    key = data.split("_")[1]
    cursor.execute("DELETE FROM pending_task WHERE key = %s",(key,))
    DATABASE.commit()
    await query.answer()
    cap = query.message.caption.html
    return await query.edit_message_caption(f"{cap}\n\n**Rejected By {mention} ❌**")
'''
    replied = message.reply_to_message
    if not replied.photo:
        return await message.reply_text("reply to a image")
    if not replied.caption:
        return await message.reply_text("image has no name in caption")
    down = await replied.download()
    pic = upload_file(down)
    link = f"https://graph.org{pic[0]}"
    cap = replied.caption.split("+")
    name = cap[0].title()
    anime = cap[1].title()
    if cap[2] == " 🔮":
        rarity = "🔮 Limited-Time"
    elif cap[2] == " 🟡":
        rarity = "🟡 Legendary"
    elif cap[2] == " 🟣":
        rarity = "🟣 Rare"
    elif cap[2] == " 🟢":
        rarity = "🟢 Common"
    else:
        return await message.reply_text("Invalid Rarity.\nAllowed Rarity : [🟢,🟣,🟡,🔮]")
    cursor.execute("INSERT INTO character_db (name , anime , rarity , pic) VALUES (%s , %s , %s , %s)",(name,anime,rarity,link,))
    DATABASE.commit()
return await message.reply_photo(link,caption=f"✨ Added Character in Database.\nName : {name}\nAnime : {anime}\nRarity : {rarity}")'''

'''@app.on_message(filters.private)
async def processing(client,message):
    user_id = message.from_user.id
    if user_id not in PROCESS:
        return
    if message.photo:
        down = await message.download()
        pic = upload_file(down)
        link = f"https://graph.org{pic[0]}"
        PROCESS[user_id]['link'] = link
        return await message.reply_text("**Please tell me the character name.**")
    elif PROCESS[user_id]['link'] is not None:
        name = message.text
        PROCESS[user_id]['name'] = name
        return await message.reply_text("**Please tell me the anime name.**")
    elif PROCESS[user_id]['name'] is not None:
        anime = message.text
        PROCESS[user_id]['anime'] = anime
        return await message.reply_text("**Please tell me the rarity.**")
    await message.reply_photo(photo=PROCESS[user_id]['link'],caption=f"Name - {PROCESS[user_id]['name']}\nAnime - {PROCESS[user_id]['anime']}")
    return PROCESS.pop(user_id)'''
