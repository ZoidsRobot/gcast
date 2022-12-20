from asyncio import *
from random import *
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren 
from pyrogram import Client
from KillerXBase.helper.cmd import *
from KillerXBase.helper.basic import *
from KillerXBase.helper.PyroHelpers import *
from KillerXBase.modules.help import *
from KillerXBase.helper.dev import *
from KillerXBase.helper.misc import *
from KillerXBase.helper.goblok import *

# code by @xtsea

@ren.on_message(filters.command("readpm", cmd) & filters.me)
async def readpm(client: Client, message: Message):
    p = await message.edit("`Prossingg....`")
    read = get_arg(message)
    try:
       asyncio.sleep(1.5)
       await p.delete()
       async for r in client.get_chat_history(read, read):
           await r.copy(message.chat.id)
           await r.delete()
    except BaseException:
        pass
