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

# credits @xtsea

@ren.on_message(filters.command("copy", cmd) & filters.me)
async def sosmed(client: Client, message: Message):
    mmk = await message.edit("`Processing . . .`")
    link = get_arg(message)
    bot = "kangcopybot"
    if link:
        try:
            await asyncio.sleep(2)
            await mmk.delete()
            a = await client.send_message(bot, link)
            await asyncio.sleep(2)
            await a.delete()
            async for c in client.get_chat_history(bot, 1):
                await c.copy(message.chat.id)
                await c.delete()
        except BaseException:
            pass

add_command_help(
    "copy",
    [
        [f"copy <link>", "stealing media from the channel",],
    ],
)
