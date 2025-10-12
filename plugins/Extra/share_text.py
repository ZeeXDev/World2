# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import os
from pyrogram import Client, filters
from urllib.parse import quote
from info import CHNL_LNK
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["share_text", "share", "sharetext"]))
async def share_text(client, message):
    vj = await client.ask(chat_id = message.from_user.id, text = "📤 Envoyez-moi votre texte maintenant")
    if vj and (vj.text or vj.caption):
        input_text = vj.text or vj.caption
    else:
        await vj.reply_text(
            text=f"**📝 Notice :**\n\n1. Envoyez n'importe quel message texte\n2. Pas de support média\n\n**📢 Rejoignez la chaîne de mise à jour**",               
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📢 Chaîne des mises à jour", url=CHNL_LNK)]])
            )                                                   
        return
    await vj.reply_text(
        text=f"**🔗 Voici votre texte de partage 👇**\n\nhttps://t.me/share/url?url=" + quote(input_text),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📤 Partager", url=f"https://t.me/share/url?url={quote(input_text)}")]])       
    )