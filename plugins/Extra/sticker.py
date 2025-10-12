from pyrogram import Client, filters

@Client.on_message(filters.command("stickerid") & filters.private)
async def stickerid(bot, message):
    s_msg = await bot.ask(chat_id = message.from_user.id, text = "📤 Envoyez-moi votre sticker maintenant")
    if s_msg.sticker:
        await s_msg.reply_text(f"**🆔 ID du sticker :**  \n `{s_msg.sticker.file_id}` \n \n **🔐 ID unique :** \n\n`{s_msg.sticker.file_unique_id}`")
    else: 
        await s_msg.reply_text("❌ Oops !! Ce n'est pas un fichier sticker")