from Waifu import *
from Waifu.functions.watch_db import select,insert,delete,updaters
from pyrogram import *
from pyrogram.types import *



@Client.on_message(filters.command("gift") & filters.group)
async def gifting(client,message):
    try:
        id = message.text.split(maxsplit=1)[1]
    except:
        return await message.reply_text("provide an waifu id")
    if not int(id):
        return await message.reply_text("provide valid id")
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("reply to an user to gift waifus")
    replied_user = message.reply_to_message.from_user
    check = await select(int(id))
    if not check:
        return await message.reply_text("Waifu with this ID doesn't exists")
    for info in check:
        ids,user_id,name,anime,rarity,pic,count = info
    if int(user_id) != message.from_user.id:
        return await message.reply_text(f"You don't have {name}\nso you can't gift it yet!")
    confirmation_text = f"Are you sure you want to gift {name} to {replied_user.mention}?"
    confirmation_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("Yes", callback_data=f"confirmgift_{user_id}_{id}")],
            [InlineKeyboardButton("No", callback_data=f"cancel_{user_id}")]
        ])
    return await message.reply_photo(photo="https://graph.org//file/cd9dadc930fc140623377.png",caption=confirmation_text,reply_markup=confirmation_markup)
    
