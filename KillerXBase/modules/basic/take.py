import asyncio
from pyrogram.types import *
from pyrogram import *
from pyrogram import Client as ren
from pyrogram import Client
from KillerXBase.helper.cmd import *
from KillerXBase.helper.basic import *
from KillerXBase.helper.PyroHelpers import *
from KillerXBase.helper.misc import *
from KillerXBase.modules.help import *

@ren.on_message(filters.command("take", cmd) & filters.me)
async def take(client: Client, message: Message):
    c = await message.edit("`Prossing...`")
    link = get_arg(message)
    if link:
        try:
           await c.delete()
           await client.copy_message(message.chat.id, from_chat_id="RendyProjects", link)
        except BaseException:
            pass
     
