# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os, string, logging, random, asyncio, time, datetime, re, sys, json, base64
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import *
from database.ia_filterdb import col, sec_col, get_file_details, unpack_new_file_id, get_bad_files, db as vjdb, sec_db
from database.users_chats_db import db, delete_all_referal_users, get_referal_users_count, get_referal_all_users, referal_add_user
from database.join_reqs import JoinReqs
from info import *
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from utils import get_settings, pub_is_subscribed, get_size, is_subscribed, save_group_settings, temp, verify_user, check_token, check_verification, get_token, get_shortlink, get_tutorial, get_seconds
from database.connections_mdb import active_connection, mydb

@Client.on_message(filters.new_chat_members & filters.group)
async def save_group(bot, message):
    r_j_check = [u.id for u in message.new_chat_members]
    if temp.ME in r_j_check:
        if not await db.get_chat(message.chat.id):
            total=await bot.get_chat_members_count(message.chat.id)
            r_j = message.from_user.mention if message.from_user else "Anonyme" 
            await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, r_j))       
            await db.add_chat(message.chat.id, message.chat.title)
        if message.chat.id in temp.BANNED_CHATS:
            # Inspiré d'un bateau fait d'un bananier
            buttons = [[
                InlineKeyboardButton('Support', url=f'https://t.me/{SUPPORT_CHAT}')
            ]]
            reply_markup=InlineKeyboardMarkup(buttons)
            k = await message.reply(
                text='<b>CHAT NON AUTORISÉ 🐞\n\nMes administrateurs m\'ont interdit de travailler ici ! Si vous voulez en savoir plus, contactez le support..</b>',
                reply_markup=reply_markup,
            )
            try:
                await k.pin()
            except:
                pass
            await bot.leave_chat(message.chat.id)
            return
        buttons = [[
            InlineKeyboardButton('👥 Groupe de support', url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton('📢 Chaîne des mises à jour', url=CHNL_LNK)
        ],[
            InlineKeyboardButton("👑 Propriétaire du bot", url=OWNER_LNK)
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=f"<b>Merci de m'avoir ajouté dans {message.chat.title} ❣️\n\nSi vous avez des questions ou des doutes sur mon utilisation, contactez le support.</b>",
            reply_markup=reply_markup
        )
    else:
        settings = await get_settings(message.chat.id)
        if settings["welcome"]:
            for u in message.new_chat_members:
                if (temp.MELCOW).get('welcome') is not None:
                    try:
                        await (temp.MELCOW['welcome']).delete()
                    except:
                        pass
                button = [[
                    InlineKeyboardButton('👥 Groupe de support', url=f'https://t.me/{SUPPORT_CHAT}'),
                    InlineKeyboardButton('📢 Chaîne des mises à jour', url=CHNL_LNK)
                ],[
                    InlineKeyboardButton("👑 Propriétaire du bot", url=OWNER_LNK)
                ]]
                temp.MELCOW['welcome'] = await message.reply_text(
                    text=(script.MELCOW_ENG.format(u.mention, message.chat.title)),
                    reply_markup=InlineKeyboardMarkup(button),
                    parse_mode=enums.ParseMode.HTML
                )  
        if settings["auto_delete"]:
            await asyncio.sleep(600)
            await (temp.MELCOW['welcome']).delete()

@Client.on_message(filters.command('leave') & filters.user(ADMINS))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Donnez-moi un ID de chat')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('👥 Groupe de support',url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("👑 Propriétaire du bot", url=OWNER_LNK)
        ],[
            InlineKeyboardButton('🤖 Utilisez-moi ici', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text='<b>Bonjour les amis, \nMon administrateur m\'a dit de quitter le groupe, donc je pars ! Si vous voulez m\'ajouter à nouveau, contactez mon groupe de support ou mon propriétaire</b>',
            reply_markup=reply_markup,
        )

        await bot.leave_chat(chat)
        await message.reply(f"a quitté le chat `{chat}`")
    except Exception as e:
        await message.reply(f'Erreur - {e}')

@Client.on_message(filters.command('disable') & filters.user(ADMINS))
async def disable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Donnez-moi un ID de chat')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "Aucune raison fournie"
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Donnez-moi un ID de chat valide')
    cha_t = await db.get_chat(int(chat_))
    if not cha_t:
        return await message.reply("Chat non trouvé dans la base de données")
    if cha_t['is_disabled']:
        return await message.reply(f"Ce chat est déjà désactivé:\nRaison-<code> {cha_t['reason']} </code>")
    await db.disable_chat(int(chat_), reason)
    temp.BANNED_CHATS.append(int(chat_))
    await message.reply('Chat désactivé avec succès')
    try:
        buttons = [[
            InlineKeyboardButton('👥 Support', url=f'https://t.me/{SUPPORT_CHAT}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat_, 
            text=f'<b>Bonjour les amis, \nMon administrateur m\'a dit de quitter le groupe donc je pars ! Si vous voulez m\'ajouter à nouveau, contactez mon groupe de support.</b> \nRaison : <code>{reason}</code>',
            reply_markup=reply_markup)
        await bot.leave_chat(chat_)
    except Exception as e:
        await message.reply(f"Erreur - {e}")

@Client.on_message(filters.command('enable') & filters.user(ADMINS))
async def re_enable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Donnez-moi un ID de chat')
    chat = message.command[1]
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Donnez-moi un ID de chat valide')
    sts = await db.get_chat(int(chat))
    if not sts:
        return await message.reply("Chat non trouvé dans la base de données !")
    if not sts.get('is_disabled'):
        return await message.reply('Ce chat n\'est pas encore désactivé.')
    await db.re_enable_chat(int(chat_))
    temp.BANNED_CHATS.remove(int(chat_))
    await message.reply("Chat réactivé avec succès")

@Client.on_message(filters.command('stats') & filters.incoming)
async def get_ststs(bot, message):
    rju = await message.reply('Récupération des statistiques..')
    try:
        total_users = await db.total_users_count()
        totl_chats = await db.total_chat_count()
        filesp = col.count_documents({})
        stats = vjdb.command('dbStats')
        used_dbSize = (stats['dataSize']/(1024*1024))+(stats['indexSize']/(1024*1024))
        free_dbSize = 512-used_dbSize
        
        if MULTIPLE_DATABASE == False:
            await rju.edit(script.SEC_STATUS_TXT.format(total_users, totl_chats, filesp, round(used_dbSize, 2), round(free_dbSize, 2)))
            return 
            
        totalsec = sec_col.count_documents({})   
        stats2 = sec_db.command('dbStats')
        used_dbSize2 = (stats2['dataSize']/(1024*1024))+(stats2['indexSize']/(1024*1024))
        free_dbSize2 = 512-used_dbSize2
        stats3 = mydb.command('dbStats')
        used_dbSize3 = (stats3['dataSize']/(1024*1024))+(stats3['indexSize']/(1024*1024))
        free_dbSize3 = 512-used_dbSize3
        await rju.edit(script.STATUS_TXT.format((int(filesp)+int(totalsec)), total_users, totl_chats, filesp, round(used_dbSize, 2), round(free_dbSize, 2), totalsec, round(used_dbSize2, 2), round(free_dbSize2, 2), round(used_dbSize3, 2), round(free_dbSize3, 2)))
    except Exception as e:
        await rju.edit(f"Erreur - {e}")

@Client.on_message(filters.command('invite') & filters.user(ADMINS))
async def gen_invite(bot, message):
    if len(message.command) == 1:
        return await message.reply('Donnez-moi un ID de chat')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('Donnez-moi un ID de chat valide')
    try:
        link = await bot.create_chat_invite_link(chat)
    except ChatAdminRequired:
        return await message.reply("Échec de la génération du lien d'invitation, je n'ai pas les droits suffisants")
    except Exception as e:
        return await message.reply(f'Erreur {e}')
    await message.reply(f'Voici votre lien d\'invitation {link.invite_link}')

@Client.on_message(filters.command('ban') & filters.user(ADMINS))
async def ban_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('Donnez-moi un ID utilisateur / nom d\'utilisateur')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "Aucune raison fournie"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("Ceci est un utilisateur invalide, assurez-vous que je l'ai rencontré auparavant.")
    except IndexError:
        return await message.reply("Ceci pourrait être un canal, assurez-vous que c'est un utilisateur.")
    except Exception as e:
        return await message.reply(f'Erreur - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if jar['is_banned']:
            return await message.reply(f"{k.mention} est déjà banni\nRaison: {jar['ban_reason']}")
        await db.ban_user(k.id, reason)
        temp.BANNED_USERS.append(k.id)
        await message.reply(f"Utilisateur {k.mention} banni avec succès")
    
@Client.on_message(filters.command('unban') & filters.user(ADMINS))
async def unban_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('Donnez-moi un ID utilisateur / nom d\'utilisateur')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "Aucune raison fournie"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("Ceci est un utilisateur invalide, assurez-vous que je l'ai rencontré auparavant.")
    except IndexError:
        return await message.reply("Ceci pourrait être un canal, assurez-vous que c'est un utilisateur.")
    except Exception as e:
        return await message.reply(f'Erreur - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if not jar['is_banned']:
            return await message.reply(f"{k.mention} n'est pas encore banni.")
        await db.remove_ban(k.id)
        temp.BANNED_USERS.remove(k.id)
        await message.reply(f"Utilisateur {k.mention} débanni avec succès")
    
@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    # https://t.me/GetTGLink/4184
    raju = await message.reply('Obtention de la liste des utilisateurs')
    users = await db.get_all_users()
    out = "Les utilisateurs enregistrés dans la base de données sont:\n\n"
    async for user in users:
        out += f"<a href=tg://user?id={user['id']}>{user['name']}</a>"
        if user['ban_status']['is_banned']:
            out += '( Utilisateur banni )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="Liste des utilisateurs")

@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def list_chats(bot, message):
    raju = await message.reply('Obtention de la liste des chats')
    chats = await db.get_all_chats()
    out = "Les chats enregistrés dans la base de données sont:\n\n"
    async for chat in chats:
        out += f"**Titre:** `{chat['title']}`\n**- ID:** `{chat['id']}`"
        if chat['chat_status']['is_disabled']:
            out += '( Chat désactivé )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="Liste des chats")