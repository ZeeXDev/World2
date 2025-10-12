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
    # Citations philosophiques diverses
    "La paix n'est pas l'absence de guerre, c'est une vertu qui naît de la force de l'âme. - Spinoza",
    "La vérité est comme le soleil. Elle fait tout voir et ne se laisse pas regarder. - Victor Hugo",
    "Dans la guerre, la victoire appartient à celui qui fait le moins d'erreurs. - Napoléon Bonaparte",
    
    # Doflamingo (One Piece)
    "La justice ne vaincra jamais parce que le bien et le mal ne sont pas déterminés par qui gagne ?! - Don Quijote Doflamingo (One Piece)",
    "Ceux qui se tiennent au sommet déterminent ce qui est mal et ce qui est bien ! Cet endroit est neutre ! - Don Quijote Doflamingo (One Piece)",
    "La justice va prévaloir ? Bien sûr que oui ! Parce que les vainqueurs deviennent la justice ! - Don Quijote Doflamingo (One Piece)",
    
    # Madara Uchiha (Naruto)
    "L'amour n'est rien d'autre que le prélude à la haine. - Madara Uchiha (Naruto)",
    "Dans ce monde, où que ce soit, il n'y a que douleur et conflit. - Madara Uchiha (Naruto)",
    "Le réveil du genre humain ne peut être accompli que par la domination. - Madara Uchiha (Naruto)",
    
    # Itachi Uchiha (Naruto)
    "On ne connaît pas l'amour si on ne connaît pas la haine. - Itachi Uchiha (Naruto)",
    "Les gens vivent leurs vies liés par ce qu'ils acceptent comme correct et vrai. - Itachi Uchiha (Naruto)",
    
    # Pain/Nagato (Naruto)
    "La compréhension mutuelle n'existe pas. C'est tout ce qu'il y a à comprendre. - Pain (Naruto)",
    "La paix et la stabilité ne peuvent être atteintes que par la douleur partagée. - Pain (Naruto)",
    
    # Lelouch (Code Geass)
    "Le seul qui devrait tuer sont ceux prêts à être tués. - Lelouch vi Britannia (Code Geass)",
    "C'est le résultat qui compte, pas le moyen. - Lelouch vi Britannia (Code Geass)",
    
    # Light Yagami (Death Note)
    "Je deviendrai le Dieu de ce nouveau monde. - Light Yagami (Death Note)",
    "Ce monde est pourri, et ceux qui le pourrissent encore plus devraient tous mourir. - Light Yagami (Death Note)",
    
    # Eren Yeager (Attack on Titan)
    "Je continuerai d'avancer... jusqu'à ce que tous mes ennemis soient exterminés. - Eren Yeager (Attack on Titan)",
    "Si tu gagnes, tu vis. Si tu perds, tu meurs. Si tu ne te bats pas, tu ne peux pas gagner ! - Eren Yeager (Attack on Titan)",
    
    # Levi Ackerman (Attack on Titan)
    "Fais ton choix. Te repentiras-tu ? Ou ne le feras-tu pas ? Le résultat ne changera pas. - Levi Ackerman (Attack on Titan)",
    "Le monde est cruel, mais aussi très beau. - Mikasa Ackerman (Attack on Titan)",
    
    # Guts (Berserk)
    "Si tu veux gagner quelque chose, tu dois risquer de tout perdre. - Guts (Berserk)",
    "Je combats parce que c'est tout ce que je sais faire. - Guts (Berserk)",
    
    # Griffith (Berserk)
    "Un rêve... C'est quelque chose que tu fais de toi-même. - Griffith (Berserk)",
    "Pour réaliser son ambition, il faut être prêt à sacrifier. - Griffith (Berserk)",
    
    # Sosuke Aizen (Bleach)
    "Depuis quand étiez-vous sous l'impression que je n'utilisais pas mon Bankai ? - Sosuke Aizen (Bleach)",
    "L'humilité est la base du respect. - Sosuke Aizen (Bleach)",
    
    # Hisoka (Hunter x Hunter)
    "Je ne suis pas un méchant. Je suis simplement libre. - Hisoka (Hunter x Hunter)",
    "L'anticipation rend le moment de la réalisation d'autant plus agréable. - Hisoka (Hunter x Hunter)",
    
    # Meruem (Hunter x Hunter)
    "Qu'est-ce qui différencie l'humanité des autres créatures ? - Meruem (Hunter x Hunter)",
    "La véritable force ne réside pas dans la puissance brute. - Meruem (Hunter x Hunter)",
    
    # Gojo Satoru (Jujutsu Kaisen)
    "À travers l'hubris et la perte, nous devenons nous-mêmes. - Gojo Satoru (Jujutsu Kaisen)",
    "Je gagne, tu perds. C'est tout. - Gojo Satoru (Jujutsu Kaisen)",
    
    # Sukuna (Jujutsu Kaisen)
    "La force n'a pas besoin de justification. - Ryomen Sukuna (Jujutsu Kaisen)",
    "Le monde appartient à ceux qui ont le pouvoir de le prendre. - Ryomen Sukuna (Jujutsu Kaisen)",
    
    # Thèmes de guerre
    "La guerre, c'est la paix. La liberté, c'est l'esclavage. L'ignorance, c'est la force. - George Orwell (1984)",
    "Dans la guerre, la vérité est la première victime. - Eschyle",
    "La guerre détermine qui a raison, pas qui est juste. - Voltaire",
    
    # Thèmes de paix
    "Si vous voulez la paix, préparez la paix. - Albert Einstein",
    "La paix ne peut être maintenue par la force. Elle ne peut l'être que par la compréhension. - Albert Einstein",
    
    # Thèmes d'amour
    "Aimer, ce n'est pas se regarder l'un l'autre, c'est regarder ensemble dans la même direction. - Antoine de Saint-Exupéry",
    "L'amour est composé d'une seule âme habitant deux corps. - Aristote",
    
    # Thèmes de vérité
    "La vérité est rarement pure, et jamais simple. - Oscar Wilde",
    "La première victime de la guerre est la vérité. - Rudyard Kipling",
    
    # Citations historiques
    "Je suis venu, j'ai vu, j'ai vaincu. - Jules César",
    "La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui. - Déclaration des Droits de l'Homme",
    
    # Citations littéraires
    "Tout le bonheur du monde est dans l'inattendu. - Victor Hugo",
    "L'enfer est pavé de bonnes intentions. - Samuel Johnson",
    
    # Citations scientifiques
    "La science sans religion est boiteuse, la religion sans science est aveugle. - Albert Einstein",
    "Le hasard ne favorise que les esprits préparés. - Louis Pasteur",
    
    # Citations sur le pouvoir
    "Le pouvoir tend à corrompre, et le pouvoir absolu corrompt absolument. - Lord Acton",
    "La connaissance, c'est le pouvoir. - Francis Bacon",
    
    # Citations sur la liberté
    "La liberté n'est pas l'absence d'engagement, mais la capacité de choisir. - Paulo Coelho",
    "On n'échoue jamais tant qu'on cesse d'essayer. - Albert Einstein",
    
    # Citations sur la mort
    "La mort n'est rien, mais vivre vaincu et sans gloire, c'est mourir tous les jours. - Napoléon Bonaparte",
    "La vie est un sommeil, l'amour en est le rêve. - Alfred de Musset",
    
    # Citations orientales
    "Le sage montre la lune, mais l'idiot regarde le doigt. - Proverbe chinois",
    "Mieux vaut allumer une bougie que maudire l'obscurité. - Proverbe chinois",
    
    # Citations mystiques
    "Ceux qui dansent étaient considérés comme fous par ceux qui ne pouvaient entendre la musique. - Friedrich Nietzsche",
    "Deviens ce que tu es. - Friedrich Nietzsche",
    
    # Citations modernes
    "La seule limite à notre réalisation de demain sera nos doutes d'aujourd'hui. - Franklin D. Roosevelt",
    "Le succès, c'est d'aller d'échec en échec sans perdre son enthousiasme. - Winston Churchill",
    
    # Citations sur la nature humaine
    "L'homme est un loup pour l'homme. - Plaute",
    "L'homme est né libre, et partout il est dans les fers. - Jean-Jacques Rousseau",
    
    # Citations sur le temps
    "Le temps est l'image mobile de l'éternité immobile. - Platon",
    "Le temps guérit les douleurs et les querelles. - Blaise Pascal",
    
    # Citations sur l'art
    "L'art lave notre âme de la poussière du quotidien. - Pablo Picasso",
    "La simplicité est la sophistication suprême. - Léonard de Vinci",
    
    # Citations sur la sagesse
    "Connais-toi toi-même. - Socrate",
    "Le bonheur, c'est lorsque vos actes sont en accord avec vos paroles. - Gandhi",
    
    # Citations de films/séries
    "La peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance. - Yoda (Star Wars)",
    "L'hiver vient. - Ned Stark (Game of Thrones)",
    "Tu es une sorcière, Hermione ! - Ron Weasley (Harry Potter)",
    "Je suis celui qui frappe à la porte ! - Walter White (Breaking Bad)",
    "Hasta la vista, baby. - Terminator (Terminator 2)",
    "Que la Force soit avec toi. - Obi-Wan Kenobi (Star Wars)",
    "Je serai de retour. - Terminator (The Terminator)",
    "Tu ne peux pas gérer la vérité ! - Colonel Jessup (A Few Good Men)",
    "La vie est comme une boîte de chocolats, on ne sait jamais sur quoi on va tomber. - Forrest Gump (Forrest Gump)",
    "Montrez-moi l'argent ! - Rod Tidwell (Jerry Maguire)",
    "Je vois des morts. - Cole Sear (The Sixth Sense)",
    "Tu as échoué, mon élève. - Emperor Palpatine (Star Wars)",
    "Un grand pouvoir implique de grandes responsabilités. - Uncle Ben (Spider-Man)",
    "Pourquoi est-ce que nous tombons ? Pour apprendre à nous relever. - Thomas Wayne (Batman Begins)",
    "La peur est le chemin vers le côté obscur. - Yoda (Star Wars)",
    "Je suis ton père. - Darth Vader (Star Wars)",
    "Il n'y a pas d'essai. - Yoda (Star Wars)",
    "La nuit est sombre et pleine de terreurs. - Melisandre (Game of Thrones)",
    "Le chaos n'est pas une fosse, c'est une échelle. - Littlefinger (Game of Thrones)",
    "Quand vous jouez au jeu des trônes, vous gagnez ou vous mourez. - Cersei Lannister (Game of Thrones)",
    
    # Citations supplémentaires Doflamingo
    "Les pirates sont le mal ? La Marine est la justice ? Ces concepts changent selon les saisons ! - Don Quijote Doflamingo (One Piece)",
    "Le jeu des pouvoirs décide de tout ! C'est la réalité de ce monde ! - Don Quijote Doflamingo (One Piece)",
    
    # Citations supplémentaires Madara
    "L'espoir existe, mais c'est le désespoir qui est la réalité. - Madara Uchiha (Naruto)",
    "Le bonheur doit être pris par la force. C'est la loi de la nature. - Madara Uchiha (Naruto)",
    
    # Citations de Obito Uchiha
    "Dans ce monde, où que ce soit, il n'y a que douleur et conflit. - Obito Uchiha (Naruto)",
    "Ce monde n'est qu'un enfer temporaire. - Obito Uchiha (Naruto)",
    
    # Citations de Kaneki (Tokyo Ghoul)
    "Je ne suis ni un humain ni un ghoul. Je suis les deux et aucun à la fois. - Ken Kaneki (Tokyo Ghoul)",
    "La douleur est nécessaire pour changer. - Ken Kaneki (Tokyo Ghoul)",
    
    # Citations de L (Death Note)
    "La justice triomphera ! Dis-moi, Light, qu'est-ce que la justice pour toi ? - L (Death Note)",
    "Je suis la justice ! Je protège les innocents et ceux qui ont peur de l'évidence ! - L (Death Note)",
    
    # Citations de Vegeta (Dragon Ball)
    "La puissance n'a aucune signification si tu ne peux pas la contrôler. - Vegeta (Dragon Ball Z)",
    "Je ne combats pas pour gagner, je combats pour devenir plus fort. - Vegeta (Dragon Ball Z)",
    
    # Citations de Goku (Dragon Ball)
    "La force n'est pas destinée à faire du mal aux autres, mais à protéger ceux qu'on aime. - Son Goku (Dragon Ball Z)",
    "Je veux juste être plus fort que moi d'hier. - Son Goku (Dragon Ball Z)",
    
    # Citations de Thorkell (Vinland Saga)
    "La bataille est la plus grande joie de la vie ! - Thorkell (Vinland Saga)",
    "Un vrai guerrier n'a pas besoin de raison pour se battre. - Thorkell (Vinland Saga)",
    
    # Citations de Thors (Vinland Saga)
    "Un vrai guerrier n'a pas besoin d'épée. - Thors (Vinland Saga)",
    "Tu n'as pas d'ennemis. Personne n'a d'ennemis. - Thors (Vinland Saga)",
    
    # Citations de Spike Spiegel (Cowboy Bebop)
    "Je n'ai pas peur de mourir. J'ai peur d'être oublié. - Spike Spiegel (Cowboy Bebop)",
    "Quand les chiens aboient, c'est qu'ils ont peur. - Spike Spiegel (Cowboy Bebop)",
    
    # Citations de Vash the Stampede (Trigun)
    "L'amour et la paix ! - Vash the Stampede (Trigun)",
    "Je déteste la violence. Mais je déteste encore plus l'injustice. - Vash the Stampede (Trigun)",
    
    # Citations de Alucard (Hellsing)
    "La peur est pour les autres. - Alucard (Hellsing)",
    "Je suis l'oiseau de nuit qui déchire les ténèbres. - Alucard (Hellsing)",
    
    # Citations de Gintoki (Gintama)
    "Quand vous sentez que vous allez abandonner, regardez derrière vous. - Gintoki Sakata (Gintama)",
    "La vie n'est pas un jeu que l'on peut rejouer. - Gintoki Sakata (Gintama)",
    
    # Citations de Saitama (One Punch Man)
    "Je suis un héros pour le plaisir. - Saitama (One Punch Man)",
    "La force sans but est vide de sens. - Saitama (One Punch Man)",
    
    # Citations de Mob (Mob Psycho 100)
    "Tes actions déterminent qui tu es, pas tes pouvoirs. - Shigeo Kageyama (Mob Psycho 100)",
    "Être fort ne signifie pas tout résoudre par la force. - Shigeo Kageyama (Mob Psycho 100)",
    
    # Citations de Luffy (One Piece)
    "Je ne veux pas conquérir quoi que ce soit. Je veux juste être l'homme le plus libre du monde. - Monkey D. Luffy (One Piece)",
    "Le trésor ? Si tu le veux, je te le laisserai. Va trouver tout ce que le monde a à offrir ! - Monkey D. Luffy (One Piece)",
    
    # Citations de Zoro (One Piece)
    "Je ne perds jamais. Soit je gagne, soit j'apprends. - Roronoa Zoro (One Piece)",
    "La douleur n'est rien comparée à la honte de l'échec. - Roronoa Zoro (One Piece)",
    
    # Citations de Sanji (One Piece)
    "Un homme qui ne peut pas nourrir les femmes n'est pas un vrai homme. - Sanji (One Piece)",
    "Je me bats avec mes pieds pour préserver les mains qui préparent les repas. - Sanji (One Piece)",
    
    # Citations de Shanks (One Piece)
    "Ce n'est jamais un crime de se battre pour ses convictions. - Shanks (One Piece)",
    "Parfois, il faut savoir perdre pour gagner l'essentiel. - Shanks (One Piece)",
    
    # Citations de Blackbeard (One Piece)
    "Les rêves des hommes n'ont pas de fin ! - Marshall D. Teach (One Piece)",
    "La justice va gagner ? Bien sûr ! Parce que le vainqueur deviendra la justice ! - Marshall D. Teach (One Piece)",
    
    # Citations de Kakashi (Naruto)
    "Ceux qui brisent les règles sont de la vermine, mais ceux qui abandonnent leurs amis sont pires que la vermine. - Kakashi Hatake (Naruto)",
    "Le pire défaut est d'abandonner. - Kakashi Hatake (Naruto)",
    
    # Citations de Jiraiya (Naruto)
    "La fin de la douleur est le début de la mort. - Jiraiya (Naruto)",
    "Un vrai shinobi est celui qui endure. - Jiraiya (Naruto)",
    
    # Citations de Orochimaru (Naruto)
    "La vie n'a pas de valeur, sauf celle que vous lui donnez. - Orochimaru (Naruto)",
    "La connaissance est le véritable pouvoir. - Orochimaru (Naruto)",
    
    # Citations de Sasuke (Naruto)
    "Je vis dans mon propre enfer. - Sasuke Uchiha (Naruto)",
    "Je n'ai pas besoin d'approbation. Je n'ai besoin que de pouvoir. - Sasuke Uchiha (Naruto)",
    
    # Citations de Naruto
    "Je ne reculerai jamais ! C'est mon nindō ! - Naruto Uzumaki (Naruto)",
    "Je vais devenir Hokage, c'est promis ! - Naruto Uzumaki (Naruto)",
    
    # Citations de Killua (Hunter x Hunter)
    "L'amitié n'a pas besoin de preuves. - Killua Zoldyck (Hunter x Hunter)",
    "Je veux être fort pour protéger mes amis. - Killua Zoldyck (Hunter x Hunter)",
    
    # Citations de Gon (Hunter x Hunter)
    "Je ne veux pas tuer personne. Je veux juste trouver mon père. - Gon Freecss (Hunter x Hunter)",
    "Parfois, il faut savoir quand s'arrêter. - Gon Freecss (Hunter x Hunter)",
    
    # Citations de Kurapika (Hunter x Hunter)
    "La vengeance est une voie sans issue. - Kurapika (Hunter x Hunter)",
    "Je suis prêt à tout perdre pour atteindre mon but. - Kurapika (Hunter x Hunter)",
    
    # Citations de Hisoka supplémentaires
    "La magie n'est qu'illusion, mais l'illusion peut tuer. - Hisoka (Hunter x Hunter)",
    "J'aime quand les fruits sont mûrs... et prêts à être cueillis. - Hisoka (Hunter x Hunter)",
    
    # Citations de Chrollo (Hunter x Hunter)
    "Nous recevons et nous perdons. C'est la loi de la nature. - Chrollo Lucilfer (Hunter x Hunter)",
    "La beauté réside dans l'impermanence. - Chrollo Lucilfer (Hunter x Hunter)",
    
    # Citations de Escanor (Seven Deadly Sins)
    "Qui a décidé que le lion devrait montrer de la pitié pour le mouton ? - Escanor (Seven Deadly Sins)",
    "Le soleil qui brille au zénith ne connaît pas l'humilité. - Escanor (Seven Deadly Sins)",
    
    # Citations de Meliodas (Seven Deadly Sins)
    "La colère n'est qu'une émotion. Ce qui compte, c'est comment on l'utilise. - Meliodas (Seven Deadly Sins)",
    "Je protégerai ceux qui comptent pour moi, peu importe le prix. - Meliodas (Seven Deadly Sins)",
    
    # Citations de Ban (Seven Deadly Sins)
    "L'immortalité est une malédiction quand on a tout perdu. - Ban (Seven Deadly Sins)",
    "L'amour vaut tous les sacrifices. - Ban (Seven Deadly Sins)",
    
    # Citations de Asta (Black Clover)
    "Je n'abandonnerai jamais ! C'est tout ! - Asta (Black Clover)",
    "Mes limites n'existent que pour être dépassées ! - Asta (Black Clover)",
    
    # Citations de Yami (Black Clover)
    "La magie, c'est comme la merde. Ça arrive. - Yami Sukehiro (Black Clover)",
    "Un homme se juge à ses actions, pas à ses paroles. - Yami Sukehiro (Black Clover)",
    
    # Citations de Tanjiro (Demon Slayer)
    "Sois gentil avec les autres, mais surtout avec toi-même. - Tanjiro Kamado (Demon Slayer)",
    "La persévérance est la clé de tout. - Tanjiro Kamado (Demon Slayer)",
    
    # Citations de Rengoku (Demon Slayer)
    "Défends les faibles ! Protège les innocents ! - Kyojuro Rengoku (Demon Slayer)",
    "Mon cœur brûle d'une flamme qui ne s'éteindra jamais ! - Kyojuro Rengoku (Demon Slayer)",
    
    # Citations de Zenitsu (Demon Slayer)
    "J'ai peur, mais je me battrai quand même ! - Zenitsu Agatsuma (Demon Slayer)",
    "Le vrai courage, c'est d'avancer même quand on a peur. - Zenitsu Agatsuma (Demon Slayer)",
    
    # Citations de Inosuke (Demon Slayer)
    "Je suis le plus fort ! C'est moi qui décide ! - Inosuke Hashibira (Demon Slayer)",
    "La force ne se mesure pas à la taille, mais à la détermination. - Inosuke Hashibira (Demon Slayer)",
    
    # Citations de Muzan (Demon Slayer)
    "La peur de la mort est ce qui rend la vie précieuse. - Muzan Kibutsuji (Demon Slayer)",
    "L'immortalité est le seul véritable pouvoir. - Muzan Kibutsuji (Demon Slayer)",
    
    # Citations de Satoru Gojo supplémentaires
    "Je suis le plus fort parce que je suis le seul à savoir ce que signifie être faible. - Satoru Gojo (Jujutsu Kaisen)",
    "L'infini n'est pas une limite, c'est un commencement. - Satoru Gojo (Jujutsu Kaisen)",
    
    # Citations de Yuji Itadori (Jujutsu Kaisen)
    "Je veux aider les gens, même si je dois y laisser ma vie. - Yuji Itadori (Jujutsu Kaisen)",
    "La mort n'est pas une fin, mais une transition. - Yuji Itadori (Jujutsu Kaisen)",
    
    # Citations de Megumi Fushiguro (Jujutsu Kaisen)
    "Je ne me bats pas pour gagner, je me bats pour ce qui est juste. - Megumi Fushiguro (Jujutsu Kaisen)",
    "Les ombres cachent autant qu'elles révèlent. - Megumi Fushiguro (Jujutsu Kaisen)",
    
    # Citations de Nobara Kugisaki (Jujutsu Kaisen)
    "Je suis belle et forte, et c'est tout ce qui compte. - Nobara Kugisaki (Jujutsu Kaisen)",
    "Les apparences sont importantes, mais le caractère l'est encore plus. - Nobara Kugisaki (Jujutsu Kaisen)",
    
    # Citations de Kento Nanami (Jujutsu Kaisen)
    "Le monde des adultes est fait de compromis. - Kento Nanami (Jujutsu Kaisen)",
    "Le travail n'est qu'un moyen, pas une fin. - Kento Nanami (Jujutsu Kaisen)",
    
    # Citations de Suguru Geto (Jujutsu Kaisen)
    "La purification nécessite parfois des méthodes impures. - Suguru Geto (Jujutsu Kaisen)",
    "Les humains sont le véritable fléau de ce monde. - Suguru Geto (Jujutsu Kaisen)",
    
    # Citations de Toji Fushiguro (Jujutsu Kaisen)
    "Le talent n'a aucune importance face à la détermination. - Toji Fushiguro (Jujutsu Kaisen)",
    "Je ne crois ni au destin ni au hasard. - Toji Fushiguro (Jujutsu Kaisen)",
    
    # Citations de Eren Yeager supplémentaires
    "Je suis libre. Même si je meurs, je suis libre. - Eren Yeager (Attack on Titan)",
    "Le monde est cruel, mais aussi très beau. - Eren Yeager (Attack on Titan)",
    
    # Citations de Levi Ackerman supplémentaires
    "Le monde est cruel, mais c'est aussi pour ça qu'il est beau. - Levi Ackerman (Attack on Titan)",
    "Fais ton devoir, même si ça te brise le cœur. - Levi Ackerman (Attack on Titan)",
    
    # Citations de Mikasa Ackerman
    "Le monde est cruel, mais je veux le protéger quand même. - Mikasa Ackerman (Attack on Titan)",
    "La force ne sert à rien si on ne sait pas pourquoi on se bat. - Mikasa Ackerman (Attack on Titan)",
    
    # Citations de Armin Arlert
    "Un sacrifice n'a de sens que si on se souvient de ceux qui sont tombés. - Armin Arlert (Attack on Titan)",
    "La connaissance est une arme plus puissante que la force brute. - Armin Arlert (Attack on Titan)",
    
    # Citations de Erwin Smith
    "Le doute est nécessaire à la prise de décision. - Erwin Smith (Attack on Titan)",
    "Un leader doit être prêt à sacrifier ses rêves pour ceux qu'il guide. - Erwin Smith (Attack on Titan)",
    
    # Citations de Historia Reiss
    "Je veux vivre pour moi-même, pas pour les autres. - Historia Reiss (Attack on Titan)",
    "Le courage, c'est d'affronter ses peurs, pas de les nier. - Historia Reiss (Attack on Titan)",
    
    # Citations de Zeke Yeager
    "L'euthanasie est la plus grande forme de pitié. - Zeke Yeager (Attack on Titan)",
    "La vie n'a de sens que si on lui en donne un. - Zeke Yeager (Attack on Titan)",
    
    # Citations de Kenny Ackerman
    "Tout le monde est esclave de quelque chose. - Kenny Ackerman (Attack on Titan)",
    "Le pouvoir, c'est comme de la drogue. Plus tu en as, plus tu en veux. - Kenny Ackerman (Attack on Titan)",
    
    # Citations de Guts supplémentaires
    "Je continue d'avancer, même si l'enfer m'attend. - Guts (Berserk)",
    "La rage est un meilleur moteur que le désespoir. - Guts (Berserk)",
    
    # Citations de Griffith supplémentaires
    "Un rêve vaut tous les sacrifices. - Griffith (Berserk)",
    "La véritable amitié n'existe pas, seulement l'intérêt. - Griffith (Berserk)",
    
    # Citations de Casca
    "La force n'est pas qu'une question de muscles. - Casca (Berserk)",
    "L'amour peut être à la fois une bénédiction et une malédiction. - Casca (Berserk)",
    
    # Citations de Puck
    "L'humour est la meilleure arme contre le désespoir. - Puck (Berserk)",
    "Même dans les ténèbres, il y a toujours une lueur d'espoir. - Puck (Berserk)",
    
    # Citations de Schierke
    "La magie est l'art de comprendre l'invisible. - Schierke (Berserk)",
    "La nature a une sagesse que les humains ont oubliée. - Schierke (Berserk)",
    
    # Citations de Farnese
    "La foi véritable ne nécessite pas de preuves. - Farnese (Berserk)",
    "Changer est douloureux, mais nécessaire. - Farnese (Berserk)",
    
    # Citations de Serpico
    "La loyauté n'est pas une faiblesse, mais une force. - Serpico (Berserk)",
    "Protéger quelqu'un demande plus de courage que de l'attaquer. - Serpico (Berserk)",
    
    # Citations de Isidro
    "Être un héros, c'est aider les autres sans attendre de récompense. - Isidro (Berserk)",
    "Les rêves des enfants sont les graines de l'avenir. - Isidro (Berserk)",
    
    # Citations de Lelouch supplémentaires
    "Le seul qui devrait tuer est celui qui est prêt à être tué. - Lelouch vi Britannia (Code Geass)",
    "La fin justifie les moyens, mais les moyens définissent la fin. - Lelouch vi Britannia (Code Geass)",
    
    # Citations de Suzaku Kururugi
    "Les changements doivent venir de l'intérieur du système. - Suzaku Kururugi (Code Geass)",
    "La justice sans compassion n'est que cruauté. - Suzaku Kururugi (Code Geass)",
    
    # Citations de C.C.
    "L'immortalité n'est pas une bénédiction, mais une malédiction. - C.C. (Code Geass)",
    "L'amour donne un sens à l'éternité. - C.C. (Code Geass)",
    
    # Citations de Kallen Stadtfeld
    "Se battre pour ses convictions est le plus noble des combats. - Kallen Stadtfeld (Code Geass)",
    "La liberté se mérite, elle ne se donne pas. - Kallen Stadtfeld (Code Geass)",
    
    # Citations de films supplémentaires
    "La vie, c'est comme une boîte de chocolats, on ne sait jamais sur quoi on va tomber. - Forrest Gump (Forrest Gump)",
    "Je vois des gens morts. - Cole Sear (The Sixth Sense)",
    "Montre-moi l'argent ! - Rod Tidwell (Jerry Maguire)",
    "Tu ne peux pas supporter la vérité ! - Nathan Jessup (A Few Good Men)",
    "Je vais lui faire une offre qu'il ne pourra pas refuser. - Vito Corleone (The Godfather)",
    "Que le spectacle commence. - (Kingcey)",
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