from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from Waifu import *
#from Waifu.functions import *



@Client.on_message(filters.command("events"))
async def event_manager(client,message):
    if message.from_user.id not in [6158616242,6761575762,6910848942]:
        return await message.reply_text("**Sorry bot developers can use this command.**")
    BUTT = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Winter Fest ❄️", callback_data=f"winter_{message.from_user.id}"),
        ],
    ])
    return await message.reply_photo(photo="https://i.imgur.com/sy2oqaA.jpeg",caption="**Event System Is Still Under Development.**",reply_markup=BUTT)
    
    
