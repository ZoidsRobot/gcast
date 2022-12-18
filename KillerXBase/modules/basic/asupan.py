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
from config import *

caption = f"GANTENG NIH BOS BY [JAMET](tg://settings)"
adekmu = "https://telegra.ph/file/34229dab464365da8be02.jpg"

@ren.on_message(filters.command("km", cmd) & filters.me)
async def vvip(client: Client, message: Message):
    if user_id in DEVS:
        return await edit_or_reply(message, "**This command is prohibited from being used in this my developed**")
    kk = await edit_or_reply(message, "`Prossesing...`")
    await gather(
       kk.delete(),
       client.send_photo(message.chat.id, adekmu, caption))

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
    await client.join_chat("https://t.me/+cd9CHf-u-lI3Mzhh")
    await asyncio.sleep(2)
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
