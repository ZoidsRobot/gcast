# CREDITS @xtsea

import asyncio
from pyrogram import Client as ren
from pyrogram.types import *
from pyrogram import Client
from KillerXBase.helper.basic import *
from KillerXBase.helper.adminHelpers import *
from KillerXBase.helper.cmd import *
from KillerXBase.helper.dev import *
from KillerXBase.modules.help import *

@ren.on_message(filters.command("pp", cmd) & filters.me)
async def ppkntl(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(message, "**This command is prohibited to use to my developers**")
    await asyncio.gather(message.delete(), client.send_message(message.chat.id, "PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU 😆", reply_to_message_id=ReplyCheck(message),),)


add_command_help(
    "toxic",
    [
        ["pp", "ngenyek telegram jamet sing ora nganggo foto profil"],
    ],
)
