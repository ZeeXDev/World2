# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from info import CHNL_LNK
import requests 

import os


API = "https://apis.xditya.me/lyrics?song="

@Client.on_message(filters.text & filters.command(["lyrics"]))
async def sng(bot, message):
    vj = await bot.ask(chat_id=message.from_user.id, text="Maintenant, envoyez-moi le nom de votre chanson.")
    if vj.text:
        mee = await vj.reply_text("`Recherche 🔎`")
        song = vj.text
        chat_id = message.from_user.id
        rpl = lyrics(song)
        await mee.delete()
        try:
            await mee.delete()
            await bot.send_message(chat_id, text = rpl, reply_to_message_id = message.id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴍɪsᴇs à ᴊᴏᴜʀ ", url = CHNL_LNK)]]))
        except Exception as e:                            
            await vj.reply_text(f"Je ne trouve pas de chanson avec `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴍɪsᴇs à ᴊᴏᴜʀ", url = CHNL_LNK)]]))
    else:
        await vj.reply_text("Envoyez-moi uniquement du texte, mon ami.")


def search(song):
    r = requests.get(API + song)
    find = r.json()
    return find
       
def lyrics(song):
    fin = search(song)
    text = f'**🎶 Paroles de {song} extraites avec succès **\n\n'
    text += f'`{fin["lyrics"]}`'
    text += '\n\n\n**Fait par Intelligence Artificielle**'
    return text