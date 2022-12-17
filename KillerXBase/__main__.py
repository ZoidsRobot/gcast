import asyncio
import importlib
from pyrogram import Client, idle
from KillerXBase.helper import join
from KillerXBase.modules import ALL_MODULES
from KillerXBase import clients, app, ids
from conifg import *

ONLINE_ON = """
➠ Userbot Online 🔥
➠ Type .alive
"""
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
            print(f"Started {ex.first_name} 🛠️")
            ids.append(ex.id)
            try:
                await cli.send_message(LOG_GROUP, ONLINE_ON)
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
