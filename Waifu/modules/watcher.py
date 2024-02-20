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
from Waifu.functions.watch_db import insert,updaters,delete
from Waifu.functions.currency_db import add_fragments
from Waifu.functions.stats_db import add_chat
from Waifu.functions.exp_modeling import WaifuClient
from Waifu.functions.events_db import winter_check
from pyrogram import *
from pyrogram.types import *

WATCH_DICT = {}
spawn_rates = {"Common": 0.90, "Legendary": 0.005, "Rare": 0.10}
pop_text = """**{} Waifu has popped out from nowhere!
Bring her to your bed by sending**
/hunt name"""

new_chat = """
{} 
#NEWCHAT
CHAT : {}
"""

lost_text = """rip, the waifu has run away already...
His/Her name is **{}**, remember it next time!"""

catch_text = """✔️ OwO you caught a {} waifu **{}**.
This waifu has been added to your harem."""
frg_text = "**You received** `˗ˏˋ𓆩†𓆪ˊˎ˗ {}` **Celestial Fragments for hunting down {} waifu.**"

'''
async def randomized_choice():
    choices = ["winter", "normal"]
    probabilities = [0.3, 0.7]
    result = random.choices(choices, weights=probabilities)[0]
    return result
'''

@Client.on_message(filters.group, group=69)
async def _watchers(_, message):
    chat_id = message.chat.id
    if not message.from_user:
        return
    if chat_id not in WATCH_DICT:
        WATCH_DICT[chat_id] = {'count': 0, 'running_count': 0, 'name': None, 'pic': None,'anime':None,'rarity':None, 'interval': 100}
    WATCH_DICT[chat_id]['count'] += 1
    if WATCH_DICT[chat_id]['count'] == WATCH_DICT[chat_id]['interval']:
        rand_num = random.random()
        rate_detector = next((category for category, rate in spawn_rates.items() if rand_num < rate), "Rare")
        rate_waifu = {"Common": "🟢 Common", "Legendary": "🟡 Legendary", "Rare": "🟣 Rare"}.get(rate_detector)
        cursor.execute("SELECT * FROM character_db WHERE rarity =%s",(rate_waifu,))
        result = cursor.fetchall()
        data = random.choice(result)
        name = data[1]
        anime = data[2]
        rarity = data[3]
        pic = data[4]
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
    if not message.text.split(maxsplit=1)[1]:
        return await message.reply_text("❌ Rip, that's not quite right.")
    guess = message.text.split(maxsplit=1)[1].lower()
    name = WATCH_DICT[chat_id]['name'].lower()
    sorted_guess = ' '.join(sorted(guess.split()))
    sorted_name = ' '.join(sorted(name.split()))
    if (len(sorted_guess.split()) > 1 and sorted_guess == sorted_name) or (len(sorted_guess.split()) == 1 and sorted_guess in sorted_name.split()):
        character_name = WATCH_DICT[chat_id]['name']
        character_pic = WATCH_DICT[chat_id]['pic']
        anime = WATCH_DICT[chat_id]['anime']
        rarity = WATCH_DICT[chat_id]['rarity']
        amount = random.randint(*{'🟣 Rare': (4, 7), '🟡 Legendary': (8, 15), '🟢 Common': (1, 3)}.get(rarity, (0, 0)))
        updated = await updaters(user_id, character_pic)
        if updated:
            WATCH_DICT.pop(chat_id)
            return await message.reply_text(catch_text.format(rarity,character_name))
        await insert(user_id, character_name, anime,rarity,character_pic,"0")
        WATCH_DICT.pop(chat_id)
        await message.reply_text(catch_text.format(rarity,character_name))
        await add_fragments(user_id,amount)
        waifu_client = WaifuClient(user_id)
        await waifu_client.handle_waifu_catch()
        return await message.reply_text(frg_text.format(amount,rarity))
    else:
        return await message.reply_text("❌ Rip, that's not quite right.")
