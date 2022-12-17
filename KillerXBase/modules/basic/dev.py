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
from KillerXBase import *


@app.on_message(filters.command(["eval", "e"], cmd) & filters.me)
async def evaluate_handler(_, m: Message):
    """ This function is made to execute python codes """

    try:

        if app.textlen() > 4096:
            return await app.send_edit(
                "Your message is too long ! only 4096 characters are excludeed",
                text_type=["mono"],
                delme=3
            )

        if app.long() == 1:
            return await app.send_edit(
                "Give me some text (code) to execute . . .",
                text_type=["mono"],
                delme=4
            )
        if m.sudo_message:
            text = m.sudo_message.text
        else:
            text = m.text

        cmd = text.split(None, 1)[1]

        msg = await app.send_edit("Executing . . .", text_type=["mono"])

        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        redirected_error = sys.stderr = StringIO()
        stdout, stderr, exc = None, None, None

        try:
            await app.aexec(cmd)
        except Exception:
            exc = traceback.format_exc()

        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        evaluation = exc or stderr or stdout or "Success"
        final_output = f"**• COMMAND:**\n\n`{cmd}`\n\n**• OUTPUT:**\n\n`{evaluation.strip()}`"

        if len(final_output) > 4096:
            await app.create_file(
                filename="eval_output.txt",
                content=str(final_output),
                caption=f"`{m.text}`"
            )
            await msg.delete()
        else:
            await app.send_edit(final_output)
    except Exception as e:
        await app.error(e)




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
