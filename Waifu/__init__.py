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

import time
import logging
import asyncio
import psycopg2
from config import *
from pyrogram import Client
import pytz

loop = asyncio.get_event_loop()
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
LOGGER = logging.getLogger("Waifu")
StartTime = time.time()
TIME_ZONE = pytz.timezone("Asia/Kolkata")
BLOCK_DURATION = 10 * 60
BLOCKED_USERS = set()
BLOCK_DICT = {}
flood_limit = 0
app = Client(
    "WaifuxpytHunter",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Waifu/modules")
)

BOT_ID = 0
BOT_USERNAME = ""
BOT_NAME = ""
BOT_MENTION = ""
cursor = None
cusr = None
DB = None
DATABASE = None

async def init():
    global BOT_NAME,BOT_USERNAME,BOT_ID,BOT_MENTION,cursor,cusr,DB,DATABASE
    LOGGER.info("Activating Bot Please Wait 🥺")
    DB = psycopg2.connect(host='otto.db.elephantsql.com',
            port='5432',
            user='xvoyijqi',
            password='46CquJaKr7qFwJv_GpBB8s7n0HCfi1HG',
            database='xvoyijqi'
        )
    DATABASE = psycopg2.connect(host='otto.db.elephantsql.com',
            port='5432',
            user='sszitcfg',
            password='0hUnKVnPcZmBIHj3iKA0AHRiddW4lTGt',
            database='sszitcfg'
        )
    cursor = DATABASE.cursor()
    DATABASE.rollback()
    DATABASE.autocommit = True
    cusr = DB.cursor()
    DB.rollback()
    DB.autocommit = True
    await asyncio.sleep(1)
    apps = await app.get_me()
    BOT_ID = apps.id
    BOT_USERNAME = apps.username  
    BOT_NAME = apps.first_name
    MENTION_BOT = apps.mention
    LOGGER.info("Activated 🥰")
    await app.start()
    
loop.run_until_complete(init()) 
