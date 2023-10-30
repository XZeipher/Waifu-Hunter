from Waifu import app,BOT_NAME
from pyrogram import Client , filters
from pyrogram.types import *
from pyrogram.enums import ChatType


@Client.on_message(filters.command("start"))
async def start(client,message):
    BUTT = [
        [
            InlineKeyboardButton("Primes ⚕️", url="https://t.me/PrimesDivision"),
            InlineKeyboardButton("Support 🆘", url="https://t.me/PrimesSupport"),
        ],
        [
            InlineKeyboardButton("➕ Add Me To Your Group ➕", url="http://t.me/WaifuHunterXBot?startgroup=true"),
        ],
    ]
    if message.chat.type != ChatType.PRIVATE:
        TEXT = f"""Hi! I'm {BOT_NAME} , If you want , I can send lustrous waifus in the group just for you.

📥 get your waifu on bed by guessing their names using /protecc name"""
    else:
        TEXT = f"Hey {message.from_user.mention}, I know you can't wait to be with your favourite waifus but I only function in a group , so add me there and watch the magic."
    return await message.reply_photo(photo="https://telegra.ph/file/77397f9d86278d8d0b519.jpg",caption=TEXT,reply_markup=InlineKeyboardMarkup(BUTT))
    
