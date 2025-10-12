# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client, filters

# AESTHETIC------------ https://telegram.me/Josprojects ------------ #

def aesthetify(string):
    PRINTABLE_ASCII = range(0x21, 0x7f)
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@Client.on_message(
    filters.command(["ae"]))
async def aesthetic(client, message):
    status_message = await message.reply_text("...")
    text = "".join(str(e) for e in message.command[1:])
    text = "".join(aesthetify(text))
    await status_message.edit(text)

# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
# EMOJI CONSTANTS


@Client.on_message(
    filters.command(["throw", "dart"])
)
async def throw_dart(client, message):
    """ /throw un @AnimatedDart """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DART_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# EMOJI CONSTANTS
DICE_E_MOJI = "🎲"
# EMOJI CONSTANTS


@Client.on_message(
    filters.command(["roll", "dice"])
)
async def roll_dice(client, message):
    """ @RollADie """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DICE_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# EMOJI CONSTANTS
TRY_YOUR_LUCK = "🎰"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["luck", "cownd"])
)
async def luck_cownd(client, message):
    """ /luck un @animatedluck """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=TRY_YOUR_LUCK,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


# EMOJI CONSTANTS
GOAL_E_MOJI = "⚽"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["goal", "shoot"])
)
async def roll_dice(client, message):
    """ @Goal """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=GOAL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


import random

RUN_STRINGS = (
    "Un être brisé rempli de ténèbres \
    Pourquoi es-tu venu le rappeler",
    "Nous sommes devenus les vies pour être l'underwater à l'underwater que nous ne connaissons pas.",
    "Tu veux le mauvais appel ... mais tu as besoin du bon tonnerre ....",
    "Oh sanglantes vertus de Grama !",
    "Mer MUGGie, je vais payer la facture.",
    "Viens avec moi !",
    "Tu n'es pas un mâle chaff !!",
    "Je l'ai verrouillé, et la bonne plage est faite par la bonne plage.",
    "Kindi ... Kindi ...!",
    "Donner les tiges puis montrer une et montrer la marque ISI",
    "Dayveyeese, Kingfisher ... Childe ...!.",
    "As-tu fait ton père pour la moitié de minuit ?",
    "C'est le Roi de notre travail.",
    "Je suis fetts pour nourrir ....",
    "Mumak est chaque Bearby Kachyo ...",
    "Oh ça bouge .... Quand on le bouge ...",
    "Le soi du charpentier est la vertu d'un charpentier.",
    "Pourquoi ne pas sentir cette intelligence à Da Vijaya ...!",
    "Où était ce temps ....",
    "Sauve-moi seulement ....",
    "Je sais que le nom de son père est Bhavaniami ....",
    "Da Dasa ...",
    "L'arbre à mangues au sel anglais d'Uppukam .....",
    "Enfants ..",
    "Ton père à Paul ....",
    "Moteur de voiture complètement en panne .....",
    "C'est l'œil ou le magnety ...",
    "Avant de tomber dans le 4ème piquetage, j'y arriverai.",
    "Les pluies ivres et le gaspillage ....",
    "Pour me dire je t'aime ....",
    "Non, la Meenaka de Verbapur n'est pas ....",
)


@Client.on_message(
    filters.command("runs")
)
async def runs(_, message):
    """ /runs chaînes """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)