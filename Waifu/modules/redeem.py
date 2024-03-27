from pyrogram import Client,filters
from Waifu import *
from Waifu.functions.watch_db import redeem_code


@Client.on_message(filters.command("redeem") & filters.private)
async def redeemer(client,message):
    user_id = message.from_user.id
    name = None
    temp = await message.reply_text("processing....")
    try:
        code = message.text.split(maxsplit=1)[1].strip()
    except:
        return await temp.edit_text("Enter the redeem code.")
    
    try:
        cusr.execute("SELECT * FROM codes WHERE code = %s",(code,))
        esep = cusr.fetchone()
        name = esep[2]
        cusr.execute("SELECT * FROM user_data WHERE name = %s",(name,))
        result = cusr.fetchone()
    except:
        return await temp.edit_text("Invalid Code")
    if result:
        return await temp.edit_text("Already redeemed.")
    request = await redeem_code(code,user_id)
    if not request:
        return await temp.edit_text("Invalid Code")
    return await temp.edit_text(f"Successfully Redeemed {name}")
