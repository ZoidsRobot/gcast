import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from KillerXBase.helper.cmd import cmd
from KillerXBase.helper.basic import edit_or_reply
from KillerXBase.helper.PyroHelpers import ReplyCheck
from KillerXBase.modules.help import add_command_help


@Client.on_message(filters.command("p", cmd) & filters.me)
async def salam(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum",
            reply_to_message_id=ReplyCheck(message),
        ),
    )

@Client.on_message(filters.command("l", cmd) & filters.me)
async def wslm(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam",
            reply_to_message_id=ReplyCheck(message),
        ),
    )

add_command_help(
    "salam",
    [
        ["p", "Assalamualaikum."],
        ["l", "Wa'alaikumsalam."],
    ],
)
