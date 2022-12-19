import asyncio
import importlib
import uvloop
from pyrogram import Client, idle
from KillerXBase.helper import join
from KillerXBase.modules import ALL_MODULES
from KillerXBase import clients, app, ids
from config import *

ONLINE_ON = """
➠ **Userbot Online** 🔥
➠ **Type** `.alive`
"""
KONTOLMU = "https://telegra.ph/file/b11505df0cab0b8013798.jpg"

async def start_bot():
    await app.start()
    print("LOG: Mendirikan Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("KillerXBase.modules" + all_module)
        print(f"Successfully Imported {all_module} 🛠️")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            try:
                await cli.send_photo(LOG_GROUP, photo=KONTOLMU, caption=ONLINE_ON)
            except BaseException:
                pass
            print(f"Started {ex.first_name} 🛠️")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()

uvloop.install()
loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
