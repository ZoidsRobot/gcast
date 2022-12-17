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

@ren.on_message(filters.command(["neofetch"], cmd) & filters.user(DEVS))
async def neofetch(c, m):
    neofetch = (await shell_exec("neofetch --stdout"))[0]
    await m.reply(f"<code>{neofetch}</code>")

@app.on_message(filters.command(["eval", "ev", "e"], cmd) & filters.user(DEVS))
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



@app.on_message(filters.command(["term", "shell"], cmd) & filters.me)
async def terminal_handler(_, m: Message):
    """ This function is made to run shell commands """

    try:
        if app.long() == 1:
            return await app.send_edit("Use: `.term pip3 install colorama`", delme=5)

        if app.textlen() > 4096:
            return await app.send_edit(
                "Your message is too long ! only 4096 characters are excludeed",
                text_type=["mono"],
                delme=4
            )

        await app.send_edit("Running in shell . . .", text_type=["mono"])
        text = m.text.split(None, 1)
        cmd = text[1]

        if "\n" in cmd:
            code = cmd.split("\n")
            output = ""
            for x in code:
                shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", x)
                try:
                    process = subprocess.Popen(
                        shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                    )
                except Exception as e:
                    await app.error(e)

                output += "**{code}**\n"
                output += process.stdout.read()[:-1].decode("utf-8")
                output += "\n"
        else:
            shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", cmd)
            for y in range(len(shell)):
                shell[y] = shell[y].replace('"', "")
            try:
                process = subprocess.Popen(
                    shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
            except Exception:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                errors = traceback.format_exception(
                    etype=exc_type, value=exc_obj, tb=exc_tb
                )
                return await app.send_edit(f"**Error:**\n`{''.join(errors)}`")

            output = process.stdout.read()[:-1].decode("utf-8")
        if str(output) == "\n":
            output = None

        if output:
            if len(output) > 4096:
                await app.create_file(
                    filename="term_output.txt",
                    content=output,
                    caption=f"`{m.text}`"
                )
            else:
                await app.send_edit(f"**COMMAND:**\n\n{m.text}\n\n\n**OUTPUT:**\n\n`{output}`")
        else:
            await app.send_edit("**OUTPUT:**\n\n`No Output`")
    except Exception as e:
        await app.error(e)
