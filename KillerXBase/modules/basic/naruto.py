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

@ren.on_message(filters.command("naruto", cmd) & filters.me)
async def naruto(client: Client, message: Message):
    a = await client.send_sticker(message.chat.id, "CAADBQADEwIAAkceYVabauGjzQ4OUgI")
    await asyncio.sleep(1)
    await a.delete()
    e = await client.send_sticker(message.chat.id, "CAADBQADeQMAAj28YFb0CAvlSjuV5gI")
    await asyncio.sleep(1)
    await e.delete()
    b = await client.send_sticker(message.chat.id, "CAADBQADPwIAAlyRYVamvYbqTt3XjQI")
    await asyncio.sleep(1)
    await b.delete()
    c = await client.send_sticker(message.chat.id, "CAADBQADlAIAAnW1WVaorC7sMkfgKQI")
    await asyncio.sleep(1)
    await c.delete()
    d = await client.send_sticker(message.chat.id, "CAADAgADXwAD9PRuFwpjuaddBSAcAg")
    await asyncio.sleep(1)
    await d.delete()
    f = await client.send_sticker(message.chat.id, "CAADBQADdgIAAg62YVZOh1Z4kDVrfQI")
    await asyncio.sleep(1)
    await f.delete()
    p = await client.send_message(message.chat.id, "summoning jutsu!!!!!!!!!")
    await asyncio.sleep(1)
    await p.delete()
    await client.send_photo(message.chat.id, "https://telegra.ph/file/78c05f1d42e16c61990ca.jpg")
