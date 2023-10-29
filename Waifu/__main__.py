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
        await app.send_message(LOG_ID ,"I am started 🥺✨")
        await idle()
    except Exception as e:
        LOGGER.error(str(e))
    
if __name__ == "__main__":
    try:
        loop.run_until_complete(execute())
    except:
        pass
