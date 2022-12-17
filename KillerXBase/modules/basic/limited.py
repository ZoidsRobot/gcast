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

@ren.on_message(filters.command(["limit", "limited"], cmd) & filters.me)
async def spamban(client: Client, m: Message):
    await client.unblock_user("spambot")
    start = "/start"
    bot = "@spambot"
    await client.send_message(bot, start)
    await asyncio.sleep(2)
    async for test in client.get_chat_history(bot, 1):
       await test.copy(message.chat.id)
       await test.delete()

add_command_help(
    "limited",
    [
        ["limit", "Check Limit telegram from @SpamBot."],
    ],
)
