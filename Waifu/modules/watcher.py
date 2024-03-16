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

import json , httpx , psycopg2 , requests , asyncio , random , time
from Waifu import *
from Waifu.functions.watch_db import insert,updaters,delete,add_exploit,explode
from Waifu.functions.stats_db import add_chat
from Waifu.functions.events_db import winter_check
from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import ChatMembersFilter

WATCH_DICT = {}
pop_text = """**{} Waifu has popped out from nowhere!
Bring her to your bed by sending**
/hunt name"""

new_chat = """
{} 
#NEWCHAT
CHAT : {}
"""
exploit_text = """**{} has been caught using a cheat bot.
If you attempt to cheat again, your harem will be reset.**"""

lost_text = """rip, the waifu has run away already...
His/Her name is **{}**, remember it next time!"""

catch_text = """✔️ OwO you caught a {} waifu **{}**.
This waifu has been added to your harem."""


async def randomized_choice():
    choices = ["winter", "normal"]
    probabilities = [0.3, 0.7]
    result = random.choices(choices, weights=probabilities)[0]
    return result


@Client.on_message(filters.group, group=69)
async def _watchers(_, message):
    chat_id = message.chat.id
    msg = None
    if not message.from_user:
        return
    if chat_id not in WATCH_DICT:
        bots = []
        async for bot in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
            bots.append(bot.user.id)
        if 6355945378 in bots:
            WATCH_DICT[chat_id] = {'count': 0, 'running_count': 0, 'name': None, 'pic': None,'anime':None,'rarity':None, 'interval': 100, 'exploit': True}
        else:
            WATCH_DICT[chat_id] = {'count': 0, 'running_count': 0, 'name': None, 'pic': None,'anime':None,'rarity':None, 'interval': 100, 'exploit': False}
    WATCH_DICT[chat_id]['count'] += 1
    if WATCH_DICT[chat_id]['count'] == WATCH_DICT[chat_id]['interval']:
        event = await winter_check()
        if not event:
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
        else:
            toss_event = await randomized_choice()
            if toss_event == "winter":
                try:
                    cursor.execute("SELECT * FROM winter_characters")
                    result = cursor.fetchall()
                    data = random.choice(result)
                    name = data[1]
                    anime = data[2]
                    rarity = data[3]
                    pic = data[4]
                except:
                    return
            else:
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
            rrr = rarity.split(maxsplit=1)[0]
            msg = await _.send_photo(chat_id, photo=pic, caption=pop_text.format(rrr),protect_content=True)
            WATCH_DICT[chat_id]['name'] = name
            WATCH_DICT[chat_id]['pic'] = pic
            WATCH_DICT[chat_id]['anime'] = anime
            WATCH_DICT[chat_id]['rarity'] = rarity
        except errors.FloodWait as e:
            await asyncio.sleep(e.value)

    if WATCH_DICT[chat_id]['name']:
        if WATCH_DICT[chat_id]['exploit']:
            if message.text and message.reply_to_message:
                endings_to_check = ["waifu", "@collect_waifu_cheats_bot"]
                if any(message.text.lower().endswith(ending) for ending in endings_to_check) and message.reply_to_message:
                    await _.send_message(chat_id, lost_text.format(WATCH_DICT[chat_id]['name']))
                    WATCH_DICT.pop(chat_id)
                    run_chk = await explode(user_id)
                    if run_chk:
                        return await message.reply_text("**Your harem has been reset for using cheat bots.**")
                    await message.reply_text(exploit_text.format(message.from_user.mention))
                    await _.send_message(-1002103089465,text=f"{message.from_user.id} user caught cheating.")
                    return await add_exploit(user_id)
        WATCH_DICT[chat_id]['running_count'] += 1
        if WATCH_DICT[chat_id]['running_count'] == 15:
            try:
                character = WATCH_DICT[chat_id]['name']
                await _.send_message(chat_id, lost_text.format(character))
                WATCH_DICT.pop(chat_id)
            except errors.FloodWait as e:
                await asyncio.sleep(e.value)

@app.on_message(filters.command("hunt") & filters.group)
async def protecc(client , message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_id not in WATCH_DICT or not WATCH_DICT[chat_id]['name']:
        return await message.reply_text("No waifu to protecc at the moment. Keep an eye out for the next one!")
    guess = message.text.split(maxsplit=1)[1].lower()
    guess2 = message.text.split(" ")[1].lower()
    name = WATCH_DICT[chat_id]['name'].lower()
    if guess == name or guess2 in name.split() or guess in name:
        character_name = WATCH_DICT[chat_id]['name']
        character_pic = WATCH_DICT[chat_id]['pic']
        anime = WATCH_DICT[chat_id]['anime']
        rarity = WATCH_DICT[chat_id]['rarity']
        updated = await updaters(user_id, character_pic)
        if updated:
            WATCH_DICT.pop(chat_id)
            return await message.reply_text(catch_text.format(rarity,character_name))
        await insert(user_id, character_name, anime,rarity,character_pic,"0")
        WATCH_DICT.pop(chat_id)
        return await message.reply_text(catch_text.format(rarity,character_name))
    else:
        return await message.reply_text("❌ Rip, that's not quite right.")
