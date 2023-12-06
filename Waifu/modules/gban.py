import time 
import asyncio
from Waifu import *
from pyrogram import *
from io import BytesIO
from pyrogram.errors import Unauthorized, FloodWait 
from Waifu.functions.events_db import *


SUPREME_USERS = [6910848942,6158616242,6761575762]

@Client.on_message(filters.command("gban"))
async def _gban(_, message):
    if message.from_user.id not in SUPREME_USERS:
        return await message.reply_text("**You aren't Developer of this Bot! Exiting...**")
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("**reply to an user to gban!**")
    try:
        reason = message.text.split(maxsplit=1)[1]
    except:
        reason = None
    gban_id = replied.from_user.id
    gban_username = replied.from_user.username
    if gban_id == 6962219103:
        return await message.reply_text("**ofc i won't ban myself!**")
    if gban_id in SUPREME_USERS:
        return await message.reply_text("**This is a developer can't ban him.**")
    msg = await message.reply_text(f"**Executing global ban on @{gban_username}**")
    gchrck = await gban_check(gban_id)
    if gchrck:
        return await msg.edit_text("**User already gbanned!**")
    await add_gban(gban_id,gban_username,reason)
    await msg.edit_text("**Gban Applied!**")
    cursor.execute("SELECT chat_id FROM chats_db")
    results = cursor.fetchall()
    for chat in results:
        try:
            await _.ban_chat_member(int(chat[0]), gban_id)
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            pass
    try:
        await _.send_message(gban_id,f"**You Have been Gbanned By {message.from_user.mention}\nYou Can Appeal This Gban From @WaifuHunterSupport**")            
    except Unauthorized:
        pass
    return

    
