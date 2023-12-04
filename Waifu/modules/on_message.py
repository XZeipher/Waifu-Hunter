"""
MIT License

Copyright (c) 2023 XZeipher

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from pyrogram import *
from Waifu import *
from Waifu.functions.stats_db import add_chat

new_chat = """
{} 
#NEWCHAT
CHAT : {}
"""

@Client.on_message(filters.new_chat_members)
async def new_mem(_,message):
    chat_id = message.chat.id
    for member in message.new_chat_members:
        id = member.id
    apps = await app.get_me()
    bot_id = apps.id
    bot_name = apps.first_name
    if int(bot_id) == int(id):
        chatting = await add_chat(chat_id)
        if chatting:
            return await app.send_message(-1002103089465,new_chat.format(bot_name,message.chat.username))
        return
    return
