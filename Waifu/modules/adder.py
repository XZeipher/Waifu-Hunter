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

@Client.on_message(filters.command("upload"))
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
    cusr.execute("INSERT INTO character_db (name , anime , rarity , pic) VALUES (%s , %s , %s , %s)",(name,anime,rarity,link,))
    DB.commit()
    return await message.reply_photo(link,caption=f"✨ Added Character in Database.\nName : {name}\nAnime : {anime}\nRarity : {rarity}")
