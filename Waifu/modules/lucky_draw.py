import random
from Waifu import *
from Waifu.functions.watch_db import insert
from pyrogram import *
from pyrogram.types import *
from telegraph import Telegraph , upload_file

telegraph = Telegraph()
new_user = telegraph.create_account(short_name="WaifuBot")
auth_url = new_user["auth_url"]


@Client.on_message(filters.command("draw") & filters.user([6910848942,6761575762]))
async def draw_lucky(client,message):
    try:
        number_of_winners = int(message.text.split(maxsplit=1)[1])
    except:
        return await message.reply_text("**Draw Format :- /draw {number_of_winners}**")
    msg = await message.reply_text("**checking data....**")
    if not message.reply_to_message:
        return await msg.edit_text("**data not found reply to waifu data.**")
    caption = message.reply_to_message.caption
    name = caption.split("+")[0].title()
    anime = caption.split("+")[1].title()
    rarity = "💮 Mythical"
    down = await message.reply_to_message.download()
    pic = upload_file(down)
    link = f"https://graph.org{pic[0]}"
    cursor.execute("SELECT user_id FROM users_db")
    result = cursor.fetchall()
    sorted_users = random.sample(result,number_of_winners)
    for user in sorted_users:
        pass
