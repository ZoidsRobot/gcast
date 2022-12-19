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

@ren.on_message(filters.commamd("naruto", cmd) & filters.me)
async def naruto(client: Client, message: Message):
    await client.send_sticker(message.chat.id, "CAACAgIAAx0EXYGnZgACgv9joHVJOT943wxKO-DRZ9ZimQYTtwACOwAD9PRuF1nL4v7O2YZqHgQ")
    await asyncio.sleep(1.5)
    try:
       await message.delete()
    except BaseException:
        pass
    await client.send_photo(message.chat.id, "https://user-images.githubusercontent.com/90479255/208452872-b6067a9c-43c2-4171-9e2f-bc1bc09208c7.jpg")
