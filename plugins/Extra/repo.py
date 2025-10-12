# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import logging
import os
import requests
from info import CHNL_LNK
from pyrogram import Client, filters


@Client.on_message(filters.command('repo'))
async def git(bot, message):
    pablo = await message.reply_text("`Traitement en cours...`")
    args = message.text.split(None, 1)[1]
    if len(message.command) == 1:
        await pablo.edit("Aucune entrée trouvée")
        return
    r = requests.get("https://api.github.com/search/repositories", params={"q": args})
    lool = r.json()
    if lool.get("total_count") == 0:
        await pablo.edit("Dépôt non trouvé")
        return
    else:
        lol = lool.get("items")
        qw = lol[0]
        txt = f"""
<b>📁 Nom :</b> <i>{qw.get("name")}</i>

<b>📂 Nom complet :</b> <i>{qw.get("full_name")}</i>

<b>🔗 Lien :</b> {qw.get("html_url")}

<b>🍴 Forks :</b> <i>{qw.get("forks_count")}</i>

<b>⚠️ Issues ouvertes :</b> <i>{qw.get("open_issues")}</i>

<b>⚡ Propulsé par : {CHNL_LNK}</b>

"""
        if qw.get("description"):
            txt += f'<b>📝 Description :</b> <code>{qw.get("description")}</code>\n\n'

        if qw.get("language"):
            txt += f'<b>💻 Langage :</b> <code>{qw.get("language")}</code>\n\n'

        if qw.get("size"):
            txt += f'<b>📦 Taille :</b> <code>{qw.get("size")} KB</code>\n\n'

        if qw.get("score"):
            txt += f'<b>⭐ Score :</b> <code>{qw.get("score")}</code>\n\n'

        if qw.get("created_at"):
            txt += f'<b>📅 Créé le :</b> <code>{qw.get("created_at")}</code>\n\n'

        if qw.get("archived") == True:
            txt += f"<b>🚫 Ce projet est archivé</b>"
        await pablo.edit(txt, disable_web_page_preview=True)