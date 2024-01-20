from Waifu import *
from pyrogram import *
from pyrogram.types import *

text = """
**Feedback Received ✅**

**USER** : {}
**Information:**
```{}```
"""


@Client.on_message(filters.command(["report","feedback","suggest"]))
async def reporting(client,message):
    if not message.text.split(maxsplit=1)[1] and not message.reply_to_message.text:
        return await message.reply_text("**you haven't provided your feedback.**")
    if not message.reply_to_message:
        feedback = message.text.split(maxsplit=1)[1].title()
        user = message.from_user.mention
        link = message.link
        markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Subject",url=link),]
            ]
        )
        await app.send_photo("WaifuHunterSupport",photo="https://i.imgur.com/rhuejQC.jpg",caption=text.format(user,feedback),reply_markup=markup)
        return await message.reply_text("**Feedback Sent To Admins.**")
    else:
        feedback = message.reply_to_message.text
        user = message.from_user.mention
        link = message.reply_to_message.link
        markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Subject",url=link),]
            ]
        )
        await app.send_photo("WaifuHunterSupport",photo="https://i.imgur.com/rhuejQC.jpg",caption=text.format(user,feedback),reply_markup=markup)
        return await message.reply_text("**Feedback Sent To Admins.**")
