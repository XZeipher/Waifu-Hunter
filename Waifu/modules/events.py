from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from Waifu import *
from Waifu.functions.events_db import winter_check

text = """
𝗛𝗲𝗹𝗹𝗼 𝗦𝘄𝗲𝗲𝘁𝗶𝗲,

𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗪𝗶𝗻𝘁𝗲𝗿 𝗙𝗲𝘀𝘁,
𝗜𝗻𝗱𝘂𝗹𝗴𝗲 𝗶𝗻 𝘁𝗵𝗲 𝘄𝗶𝗻𝘁𝗲𝗿 𝗺𝗮𝗴𝗶𝗰 𝘄𝗶𝘁𝗵 𝗼𝘂𝗿 𝗲𝘅𝗰𝗹𝘂𝘀𝗶𝘃𝗲 𝗟𝗶𝗺𝗶𝘁𝗲𝗱 𝗧𝗶𝗺𝗲 𝗪𝗮𝗶𝗳𝘂𝘀, 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗼𝗻𝗹𝘆 𝗱𝘂𝗿𝗶𝗻𝗴 𝘁𝗵𝗲 𝗲𝗻𝗰𝗵𝗮𝗻𝘁𝗶𝗻𝗴 𝗪𝗶𝗻𝘁𝗲𝗿 𝗙𝗲𝘀𝘁 𝗲𝘃𝗲𝗻𝘁! 𝗧𝗵𝗲𝘀𝗲 𝘀𝗽𝗲𝗰𝗶𝗮𝗹 𝗰𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿𝘀 𝗯𝗿𝗶𝗻𝗴 𝗮 𝘁𝗼𝘂𝗰𝗵 𝗼𝗳 𝘀𝗲𝗮𝘀𝗼𝗻𝗮𝗹 𝗰𝗵𝗮𝗿𝗺 𝗮𝗻𝗱 𝘄𝗮𝗿𝗺𝘁𝗵 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗰𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻. 𝗘𝗺𝗯𝗿𝗮𝗰𝗲 𝘁𝗵𝗲 𝘀𝗽𝗶𝗿𝗶𝘁 𝗼𝗳 𝘁𝗵𝗲 𝘄𝗶𝗻𝘁𝗲𝗿 𝘀𝗲𝗮𝘀𝗼𝗻 𝗮𝘀 𝘆𝗼𝘂 𝘂𝗻𝗹𝗼𝗰𝗸 𝘁𝗵𝗲𝘀𝗲 𝘂𝗻𝗶𝗾𝘂𝗲 𝗰𝗼𝗺𝗽𝗮𝗻𝗶𝗼𝗻𝘀, 𝗲𝗮𝗰𝗵 𝘄𝗶𝘁𝗵 𝘁𝗵𝗲𝗶𝗿 𝗼𝘄𝗻 𝗱𝗲𝘀𝗶𝗴𝗻. 𝗗𝗼𝗻'𝘁 𝗺𝗶𝘀𝘀 𝘁𝗵𝗲 𝗰𝗵𝗮𝗻𝗰𝗲 𝘁𝗼 𝗮𝗱𝗱 𝘁𝗵𝗲𝘀𝗲 𝗱𝗲𝗹𝗶𝗴𝗵𝘁𝗳𝘂𝗹 𝘄𝗮𝗶𝗳𝘂𝘀 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗹𝗶𝗻𝗲𝘂𝗽, 𝗮𝘀 𝘁𝗵𝗲𝘆 𝗮𝗿𝗲 𝗵𝗲𝗿𝗲 𝗳𝗼𝗿 𝗮 𝗹𝗶𝗺𝗶𝘁𝗲𝗱 𝘁𝗶𝗺𝗲 𝗼𝗻𝗹𝘆. 𝗝𝗼𝗶𝗻 𝘂𝘀 𝗶𝗻 𝗰𝗲𝗹𝗲𝗯𝗿𝗮𝘁𝗶𝗻𝗴 𝘁𝗵𝗲 𝗷𝗼𝘆 𝗼𝗳 𝘄𝗶𝗻𝘁𝗲𝗿 𝘄𝗶𝘁𝗵 𝘁𝗵𝗲𝘀𝗲 𝗲𝘅𝘁𝗿𝗮𝗼𝗿𝗱𝗶𝗻𝗮𝗿𝘆 𝗮𝗱𝗱𝗶𝘁𝗶𝗼𝗻𝘀 𝘁𝗼 𝘆𝗼𝘂𝗿 𝘄𝗮𝗶𝗳𝘂 𝗰𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻 𝗱𝘂𝗿𝗶𝗻𝗴 𝗪𝗶𝗻𝘁𝗲𝗿 𝗙𝗲𝘀𝘁!"""

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
