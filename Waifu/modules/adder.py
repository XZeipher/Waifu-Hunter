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
from pyrogram import *
from pyromod import listen
from pyromod.listen.message import Message
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
telegraph = Telegraph()
new_user = telegraph.create_account(short_name="WaifuBot")
auth_url = new_user["auth_url"]
PROCESS = {}

@Client.on_message(filters.command("upload") & filters.private & filters.user(AUTH_USERS))
async def adder(client , message:Message):
    user_id = message.from_user.id
    #chat = message.chat
    try:
        response = await message.chat.ask('**Send the waifu picture**',filters=filters.photo)
        bruh = client.download_media(response.photo.file_id)
        return await message.reply_photo(bruh)
    except Exception as e:
        return await message.reply(str(e))
    
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
