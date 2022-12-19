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
    lol = await message.edit("`Prossing...`")
    link = get_arg(message)
    bot = "SangMataInfo_bot"
    if link:
        try:
           a = await client.send_message(bot, link)
           await asyncio.sleep(3)
           await a.delete()
        except YouBlockedUser:
            await client.unblock_user(bot)
            b = await client.send_message(bot, link)
            await asyncio.sleep(2)
            await b.delete()
    async for i in client.get_chat_history(bot, 2):
        await i.copy(message.chat.id)
        await i.delete()
