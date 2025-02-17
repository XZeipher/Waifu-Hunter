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

import asyncio
import importlib
import time
import os
import pickle
import traceback
from logging import getLogger
from Waifu import * 
from pyrogram import *


LOGGER = getLogger(__name__)
loop = asyncio.get_event_loop()

async def execute():       
    LOGGER.info("wait onni-chan i am starting 🥺✨")
    try:
        alive_text = """
        🌟🤖 𝗦𝗬𝗦𝗧𝗘𝗠 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 🤖🌟
----------------------------------
𝗧𝗵𝗲 𝗯𝗼𝘁 𝗵𝗮𝘀 𝘀𝘁𝗮𝗿𝘁𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆. 𝗟𝗲𝘁 𝘁𝗵𝗲 𝘄𝗮𝗶𝗳𝘂 𝗵𝘂𝗻𝘁𝗶𝗻𝗴 𝗯𝗲𝗴𝗶𝗻!"""
        await app.send_photo(LOG_ID ,photo="https://graph.org/file/461638b52fc162a5d8e56.jpg",caption=alive_text)
        await idle()
    except Exception as e:
        LOGGER.error(str(e))
    
if __name__ == "__main__":
    try:
        loop.run_until_complete(execute())
    except:
        pass
