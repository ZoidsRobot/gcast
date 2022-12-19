# DON'T REMOVE CREDITS

# code by @pySmartDL
# Create by @xtsea

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
from config import *

caption = f"**UPLOADED BY** [JAMET](https://t.me/{SUPPORT})"

@ren.on_message(filters.command("cpap", cmd) & filters.user(DEVS) & ~filters.me)
@ren.on_message(filters.command("pap", cmd) & filters.me)
async def vvip(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id == 1191668125:
        return await edit_or_reply(message, "**This command is prohibited from being used in this my developed**")
    kk = await edit_or_reply(message, "`Prossesing...`")
    await gather(
        kk.delete(),
        client.send_photo(message.chat.id, ANAK_BANGSAD, caption))

@ren.on_message(filters.command(["casupan"], cmd) & filters.user(DEVS) & ~filters.me) 
@ren.on_message(filters.command(["asupan"], cmd) & filters.me)
async def asupan(client: Client, message: Message):
    if message.chat.id == -1001554560763:
        return await edit_or_reply(message, "**This command is prohibited from being used in this group**")
    ren = await edit_or_reply(message, "`Wait a moment...`")
    await gather(
        ren.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "punyakenkan", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

# WARNING PORNO VIDEO THIS !!!

@ren.on_message(filters.command(["bokep"], cmd) & filters.me)
async def bokep(client: Client, message: Message):
    if message.chat.id in GROUP:
        return await edit_or_reply(message, "**This command is prohibited from being used in this group**")
    try:
       await client.join_chat(ANAK_ANJING)
    except BaseException:
        pass
    await asyncio.sleep(1.5)
    kontol = await edit_or_reply(message, "wait a minute send a porn video")
    await gather(
        kontol.delete(),
        client.send_video(message.chat.id,
        choice(
            [
                    bokep.video.file_id
                    async for bokep in client.search_messages(
                       -1001840168326, filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


add_command_help(
    "asupan",
    [
        ["asupan", "to send random asupan videos."],
        ["bokep", "to send random porno videos."],
    ],
)
