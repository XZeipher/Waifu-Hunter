import time
import logging
import asyncio
from config import *
from database import *
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
    "WaifuHunter",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Waifu/modules")
)

BOT_ID = 0
BOT_USERNAME = ""
BOT_NAME = ""
BOT_MENTION = ""

async def init():
    global BOT_NAME,BOT_USERNAME,BOT_ID,BOT_MENTION
    LOGGER.info("Activating Bot Please Wait 🥺")
    await app.start()
    apps = await app.get_me()
    BOT_ID = apps.id
    BOT_USERNAME = apps.username  
    BOT_NAME = apps.first_name
    MENTION_BOT = apps.mention
    LOGGER.info("Activated 🥰")
    
loop.run_until_complete(init()) 
