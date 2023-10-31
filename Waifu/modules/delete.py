from Waifu.functions.dev_oops import waifu_delete
from pyrogram import Client, filters


DEV_OOPS = [6393014348,6227314727]


@Client.on_message(filters.command("delete") & filters.user(DEV_OOPS))
async def deleting_waifu(_,message):
    id = message.text.split(" ")[1]
    watcher = await waifu_delete(id)
    if not watcher:
        return await message.reply_text(f"ID {id} doesn't exists")
    return await message.reply_text("Deleted.")
