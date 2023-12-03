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

@Client.on_message(filters.command("upload") & filters.user(OWNER_ID))
async def adder(client , message):
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
    return await message.reply_photo(link,caption=f"✨ Added Character in Database.\nName : {name}\nAnime : {anime}\nRarity : {rarity}")

@Client.on_message(filters.command("winter") & filters.user(6761575762))
async def adder_winter(client , message):
    replied = message.reply_to_message
    if not replied.photo:
        return await message.reply_text("reply to a image")
    if not replied.caption:
        return await message.reply_text("image has no name in caption")
    down = await replied.download()
    pic = upload_file(down)
    link = f"https://graph.org{pic[0]}"
    cap = message.reply_to_message.caption
    try:
        cv = cap.split("-")[1].split("[")[0]
        name = cv.splitlines()[1].split(maxsplit=1)[1].title()
        anime = f" {cv.splitlines()[0].title()}"
    except:
        cv = cap.split("!")[2].split(maxsplit=1)[0]
        anime = f" {cv}"
        name = cap.split("!")[2].split(maxsplit=1)[1].split(maxsplit=1)[1].split("[")[0]
    rarity = "🔮 Limited-Time"
    cursor.execute("INSERT INTO winter_characters (name , anime , rarity , pic) VALUES (%s , %s , %s , %s)",(name,anime,rarity,link,))
    DATABASE.commit()
    return await message.reply_photo(link,caption=f"✨ Added Character in Database.\nName : {name}\nAnime :{anime}\nRarity : {rarity}")
