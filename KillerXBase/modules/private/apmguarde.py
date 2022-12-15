from pyrogram import filters, Client
from pyrogram import Client as ren
import asyncio
from KillerXBase import SUDO_USER
from KillerXBase.modules.help import *
from pyrogram.methods import messages
from .pmguard import get_arg, denied_users

from KillerXBase.database.pmpermitdb as KillerXBase



@ren.on_message(filters.command("pmguard", ["."]) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**I only understand on or off**")
        return
    if arg == "off":
        await KillerXBase.set_pm(False)
        await message.edit("**PM Guard Deactivated**")
    if arg == "on":
        await KillerXBase.set_pm(True)
        await message.edit("**PM Guard Activated**")

@ren.on_message(filters.command("setpmmsg", ["."]) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await KillerXBase.set_permit_message(KillerXBase.PMPERMIT_MESSAGE)
        await message.edit("**Anti_PM message set to default**.")
        return
    await KillerXBase.set_permit_message(f"`{arg}`")
    await message.edit("**Custom anti-pm message set**")


add_command_help(
    "antipm",
    [
        [".pmguard [on or off]", " -> Activates or deactivates anti-pm."],
        [".setpmmsg [message or default]", " -> Sets a custom anti-pm message."],
        [".setblockmsg [message or default]", "-> Sets custom block message."],
        [".setlimit [value]", " -> This one sets a max. message limit for unwanted PMs and when they go beyond it, bamm!."],
        [".allow", " -> Allows a user to PM you."],
        [".deny", " -> Denies a user to PM you."],
    ],
)
