import json , httpx , psycopg2 , requests , asyncio , random , time
from Waifu import *
from pyrogram import *
from pyrogram.types import *
from bs4 import BeautifulSoup

WATCH_DICT = {}
pop_text = """**A Waifu has appeared!
Add him/her to your harem by sending**
/protecc name"""

lost_text = """rip, the waifu has run away already...
His/Her name is {}, remember it next time!"""

catch_text = """✔️ OwO you caught {}.
This waifu has been added to your harem."""


@Client.on_message(filters.group, group=69)
async def _watchers(_, message):
    chat_id = message.chat.id
    if not message.from_user:
        return
    if chat_id not in WATCH_DICT:
        WATCH_DICT[chat_id] = {'count': 0, 'running_count': 0, 'name': None, 'pic': None, 'interval': 10}
    WATCH_DICT[chat_id]['count'] += 1
    if WATCH_DICT[chat_id]['count'] == WATCH_DICT[chat_id]['interval']:
        try:
            cursor.execute("SELECT * FROM character_db")
            result = cursor.fetchall()
            data = random.choice(result)
            name = data[1]
            anime = data[2]
            rarity = data[3]
            pic = data[4]
        except:
            return
        try:
            msg = await _.send_photo(chat_id, photo=pic, caption=pop_text)
            WATCH_DICT[chat_id]['name'] = name
            WATCH_DICT[chat_id]['pic'] = pic
        except errors.FloodWait as e:
            await asyncio.sleep(e.value)

    if WATCH_DICT[chat_id]['name']:
        WATCH_DICT[chat_id]['running_count'] += 1
        if WATCH_DICT[chat_id]['running_count'] == 15:
            try:
                character = WATCH_DICT[chat_id]['name']
                await _.send_message(chat_id, lost_text.format(character))
                WATCH_DICT.pop(chat_id)
            except errors.FloodWait as e:
                await asyncio.sleep(e.value)
"""
@app.on_message(filters.command("protecc") & filters.group)
async def protection(client , message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_id not in WATCH_DICT or not WATCH_DICT[chat_id]['name']:
        return await message.reply_text("No character to protecc at the moment. Keep an eye out for the next one!")
    guess = message.text.split(maxsplit=1)[1].lower()
    name = WATCH_DICT[chat_id]['name'].lower()
    if guess == name or guess in name.split():
        character_name = WATCH_DICT[chat_id]['name']
        character_pic = WATCH_DICT[chat_id]['pic']
        await insert(user_id, character_name, character_pic)
        WATCH_DICT.pop(chat_id)
        return await message.reply_text(catch_text.format(character_name))
    else:
        return await message.reply_text("❌ Rip, that's not quite right.")
"""
