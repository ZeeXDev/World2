# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("vie", CMD))
async def check_alive(_, message):
    await message.reply_text("**Vᴏᴜs ᴀᴠᴇᴢ ʙᴇᴀᴜᴄᴏᴜᴘ ᴅᴇ ᴄʜᴀɴᴄᴇ 🤞 ᴊᴇ sᴜɪs ᴇɴ ᴠɪᴇ ❤️\nAᴘᴘᴜʏᴇᴢ sᴜʀ /start ᴘᴏᴜʀ ᴍ'ᴜᴛɪʟɪsᴇʀ!**")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
