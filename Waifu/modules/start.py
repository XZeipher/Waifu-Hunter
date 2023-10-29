from Waifu import app
from pyrogram import Client , filters
from pyrogram.types import *


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
    return await message.reply_photo("https://telegra.ph/file/643c7a3e1ba1f10e385ab.jpg","ask @CipherFlame for start text",reply_markup=InlineKeyboardMarkup(BUTT))
    
