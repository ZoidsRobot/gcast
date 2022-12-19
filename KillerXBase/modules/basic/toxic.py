# CREDITS @xtsea

import asyncio
from pyrogram import Client as ren
from pyrogram.types import *
from pyrogram import Client
from KillerXBase.helper.basic import *
from KillerXBase.helper.adminHelpers import *
from KillerXBase.helper.cmd import *
from KillerXBase.helper.dev import *
from KillerXBase.helper.misc import *
from KillerXBase.modules.help import *

@ren.on_message(filters.command("pp", cmd) & filters.me)
async def ppkntl(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(message, "**This command is prohibited to use to my developers**")
    if message.chat.id in GROUP:
        return await edit_or_reply(message, "**This command is prohibited from being used in this group**")
    await asyncio.gather(message.delete(), client.send_message(message.chat.id, "PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU 😆", reply_to_message_id=ReplyCheck(message),),)

@ren.on_message(filters.command("kont", cmd) & filters.me)
async def toxic1(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(message, "**This command is prohibited to use to my developers**")
    toxic = await edit_or_reply(message, "**KONTOLL**")
    await asyncio.sleep(1.5)
    await toxic.edit("**LU ANAK KONTOL**")
    await asyncio.sleep(1.5)
    await toxic.edit("**DI BIKIN DARI KONTOLL**")
    await asyncio.sleep(1.5)
    await toxic.edit("**MUKALU PERSIS KONTOLL**")
    await asyncio.sleep(1.5)
    await toxic.edit("**DASAR ANAK NGONTOLLLL**")
    await asyncio.sleep(1.5)
    await toxic.edit("**NOLEP KONTOLL**")
    await asyncio.sleep(1.5)
    await toxic.edit("**NGERUSUH KONTOLL**")
    await asyncio.sleep(1.5)
    await toxic.edit("**BENER BENER KONTOLL**")
    await asyncio.sleep(1.5)
    await toxic.edit("**PADAHAL LO GAPUNYA KONTOLL**")
    await asyncio.sleep(1.5)
    await toxic.edit("**MENDING LO OPERASI KONTOLL**")
    await asyncio.sleep(1.5)
    await toxic.edit("**BIAR LO PUNYA KONTOLL**")
    await asyncio.sleep(1.5)
    await toxic.edit("**KASIAN CACAD GAPUNYA KONTOLL**")
    

@ren.on_message(filters.command("an", cmd) & filters.me)
async def toxic2(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(message, "**This command is prohibited to use to my developers**")
    await asyncio.gather(message.delete(), client.send_message(message.chat.id, "**LO KAN HASIL ZINAH HASIL HUB TERLARANG NAH LO DI BUANG DI TONGSAMPAH NAH MAK LO YG SKRG KASIAN SAMA LO MKNY DI PUNGUT UDH LO CACAT KAKI CACAT TANGAN CACAT MUKA CACAT SEMUAHNY PARAH BET SI KONTOL LO JUGA CACATAN PASTI NANAHAN JUGA,UDH MENDING LO BUNDIR DEH JADI BEBAN ORG DOANG BEGO NGERUGIN MASYARKAT BEGO BOCAH HINA BOCAH HARAM BOCAH AUTIS KEK LO MENDING MATI AJA**", reply_to_message_id=ReplyCheck(message),),)

add_command_help(
    "toxic",
    [
        ["pp", "ngenyek telegram jamet sing ora nganggo foto profil"],
    ],
)
