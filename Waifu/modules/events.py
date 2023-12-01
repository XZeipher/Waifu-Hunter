from pyrogram import Client,filters
from pyrogram.types import *
from pyrogram.enums import *
from Waifu import *
from Waifu.functions.events_db import *

text = """
𝗛𝗲𝗹𝗹𝗼 𝗦𝘄𝗲𝗲𝘁𝗶𝗲,

𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗪𝗶𝗻𝘁𝗲𝗿 𝗙𝗲𝘀𝘁,
𝗨𝘀𝗲 𝗕𝗲𝗹𝗼𝘄 𝗕𝘂𝘁𝘁𝗼𝗻 𝘁𝗼 𝗢𝗻/𝗢𝗳𝗳 𝗪𝗶𝗻𝘁𝗲𝗿 𝗙𝗲𝘀𝘁"""

@Client.on_message(filters.command("events"))
async def event_manager(client,message):
    if message.from_user.id not in [6158616242,6761575762,6910848942]:
        return await message.reply_text("**Sorry bot developers can use this command.**")
    BUTT = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Winter Fest ❄️", callback_data=f"winter"),
        ],
    ])
    return await message.reply_photo(photo="https://i.imgur.com/sy2oqaA.jpeg",caption="**Event System Is Still Under Development.**",reply_markup=BUTT)
    
    
@app.on_callback_query(filters.regex(r"^(winter)$"))
async def event_handler(client,query):
    data = query.data
    if query.from_user.id != query.message.reply_to_message.from_user.id:
        return await query.answer("Sorry you can't use this button.")
    if data == "winter":
        check = await winter_check()
        if not check:
            BUTT = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("Turn On", callback_data="on_winter"),
                ],
            ])
        else:
            BUTT = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("Turn Off", callback_data="off_winter"),
                ],
            ])
        return await query.edit_message_media(media=InputMediaPhoto("https://i.imgur.com/TA6cyP5.jpeg", caption=text),reply_markup=BUTT)

@app.on_callback_query(filters.regex(r"^(on_winter|off_winter)$"))
async def winter_call(client,query):
    data = query.data
    if query.from_user.id != query.message.reply_to_message.from_user.id:
        return await query.answer("Sorry you can't use this button.")
    if data == "on_winter":
        BUTT = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Turn Off", callback_data="off_winter"),
            ],
        ])
        await winter_on()
        await query.answer("Turned on Winter Fest.",show_alert=True)
        return await query.edit_message_reply_markup(BUTT)
    elif data == "off_winter":
        BUTT = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Turn On", callback_data="on_winter"),
            ],
        ])
        await winter_off()
        await query.answer("Turned off Winter Fest.",show_alert=True)
        return await query.edit_message_reply_markup(BUTT)
        
