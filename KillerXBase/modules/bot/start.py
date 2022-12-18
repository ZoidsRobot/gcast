# Credits: @xtsea
# please do not remove credits 
# copyright https://github.com/TeamKillerX

from pyrogram import *
from KillerXBase import app
from pyrogram.types import *
from text import *

@app.on_message(filters.command(["start"]) & filters.private)
async def start(_, message):
    try:
        await message.reply_text(
            text=kntl.KONTOL.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🛠️ Repo Source",
                            url="https://github.com/TeamKillerX/KillerX-Base",
                        )
                   ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass
