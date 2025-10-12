# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

class script(object):
    START_TXT = """<b><blockquote>Salut {} 👋,</blockquote>
    
Je suis <a href='t.me/YumeFlowerBot'>Yume</a> je peut te fournir des Films/Séries de n'importe quel genre. il suffit de rejoindre mes canaux er toit est bon</b>"""

    CLONE_START_TXT = """<b><blockquote>Bonjour {}, mon nom est <a href=https://t.me/{}>{}</a></blockquote>
    
Je suis un bot de filtre automatique avancé et puissant avec des fonctionnalités incroyables. Tapez simplement ce que vous voulez puis voyez mon pouvoir 💘</b>"""
    
    HELP_TXT = """<b>Bonjour {}
Voici quelque uns de mes fonctionnalités 👇👇.\n\nVous pouviez également m'ajouter à votre groupe ❤️😘</b>"""

    ABOUT_TXT = """<b><blockquote>⍟───[ Mes détails ]───⍟</blockquote>
    
‣ Mon nom : <a href=https://t.me/{}>{}</a>
‣ Mon meilleur ami : <a href='tg://settings'>cette personne</a> 
‣ Développeur : <a href='t.me/WorldZPrimeBot'>propriétaire</a> 
‣ Bibliothèque : <a href='https://docs.pyrogram.org/'>pyrogram</a> 
‣ Langage : <a href='https://www.python.org/download/releases/3.0/'>python 3</a> 
‣ Base de données : <a href='https://www.firebase.com/'>Ici</a> 
‣ Serveur bot : <a href='https://heroku.com'>heroku</a></b>"""

    CLONE_ABOUT_TXT = """<b><blockquote>⍟───[ ᴍʏ ᴀʙᴏᴜᴛ ]───⍟</blockquote>
    
‣ ᴍʏ ɴᴀᴍᴇ : {}
‣ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> 
‣ ᴄʟᴏɴᴇᴅ ғʀᴏᴍ : <a href=https://t.me/{}>{}</a>
‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> 
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a> 
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]></b>"""

    CLONE_TXT = """<b>🌟 <u>CLONE MODE</u>

- Yᴏᴜ Cʀᴇᴀᴛᴇ Yᴏᴜʀ Oᴡɴ Cʟᴏɴᴇ Bᴏᴛ Bʏ /clone Cᴏᴍᴍᴀɴᴅ 
- Yᴏᴜ Cᴀɴ Bʀᴏᴀᴅᴄᴀsᴛ Iɴ Yᴏᴜʀ Cʟᴏɴᴇ Bᴏᴛs
- Aɴᴅ Mɪʟʟɪᴏɴ Oғ Fɪʟᴇs Iɴᴅᴇx Aʟʀᴇᴀᴅʏ Nᴏ Nᴇᴇᴅ Tᴏ Aᴅᴅ Aɴʏ Fɪʟᴇ

👨‍💻 Cᴏᴍᴍᴀɴᴅ : /clone</b>"""

    SUBSCRIPTION_TXT = """
<b>Parrainez vos amis, famille, chaîne et groupe avec votre lien pour obtenir un abonnement premium gratuit pendant {}

Lien de parrainage - https://telegram.me/{}?start=VJ-{}

Si {} utilisateurs uniques démarrent le bot avec votre lien de parrainage, vous serez automatiquement ajouté à la liste premium.

Achetez un plan payant par - /plan</b>"""

    MANUELFILTER_TXT = """Aide : <b>Filtres</b>
- Le filtre est une fonctionnalité où les utilisateurs peuvent configurer des réponses automatiques pour un mot-clé particulier et je répondrai chaque fois qu'un mot-clé est trouvé dans le message
<b>Note :</b>
1. Ce bot doit avoir les privilèges d'administrateur.
2. Seuls les administrateurs peuvent ajouter des filtres dans une discussion.
3. Les boutons d'alerte ont une limite de 64 caractères.
Commandes et utilisation :
• /filter - <code>ajouter un filtre dans une discussion</code>
• /filters - <code>lister tous les filtres d'une discussion</code>
• /del - <code>supprimer un filtre spécifique dans une discussion</code>
• /delall - <code>supprimer tous les filtres d'une discussion (propriétaire du chat seulement)</code>"""

    # Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

    BUTTON_TXT = """Aide : <b>Boutons</b>
- Ce bot prend en charge les boutons inline URL et alerte.
<b>Note :</b>
1. Telegram ne vous permettra pas d'envoyer des boutons sans aucun contenu, le contenu est donc obligatoire.
2. Ce bot prend en charge les boutons avec n'importe quel type de média Telegram.
3. Les boutons doivent être correctement analysés au format markdown
<b>Boutons URL :</b>
<code>[Texte du bouton](buttonurl:https://t.me/vjupdates2/3)</code>
<b>Boutons d'alerte :</b>
<code>[Texte du bouton](buttonalert:Ceci est un message d'alerte)</code>"""

    AUTOFILTER_TXT = """Aide : <b>Filtre automatique</b>
<b>Note : Index de fichiers</b>
1. Rendez-moi administrateur de votre chaîne si elle est privée.
2. Assurez-vous que votre chaîne ne contient pas de camrips, de pornographie et de fichiers faux.
3. Transmettez le dernier message à moi avec des citations. J'ajouterai tous les fichiers de cette chaîne à ma base de données.

<b>Note : Filtre automatique</b>
1. Ajoutez le bot comme administrateur dans votre groupe.
2. Utilisez /connect et connectez votre groupe au bot.
3. Utilisez /settings dans le MP du bot et activez le Filtre automatique dans le menu des paramètres."""

    CONNECTION_TXT = """Aide : <b>Connexions</b>
- Utilisé pour connecter le bot au MP pour gérer les filtres 
- Cela aide à éviter le spam dans les groupes.
<b>Note :</b>
1. Seuls les administrateurs peuvent ajouter une connexion.
2. Envoyez <code>/connect</code> pour me connecter à votre MP
Commandes et utilisation :
• /connect  - <code>connecter une discussion particulière à votre MP</code>
• /disconnect  - <code>se déconnecter d'une discussion</code>
• /connections - <code>lister toutes vos connexions</code>"""

    # Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

    EXTRAMOD_TXT = """Aide : Modules supplémentaires
<b>Note :</b>
 <b>✯ Maintenu par : <a href={}>Propriétaire</a></b>
  
 <b>✯ Rejoignez ici : <a href={}>Chaîne de mises à jour</a></b> 
  
 ./id - <code>obtenir l'ID d'un utilisateur spécifié.</code> 
  
 ./info  - <code>obtenir des informations sur un utilisateur.</code> 
  
 ./song - Télécharger n'importe quelle chanson [<code>exemple /song vaa vaathi song</code>] 
  
 ./telegraph - <code>Générateur Telegraph envoyez une vidéo ou une photo de moins de 5MB je donne le lien telegraph</code> 
  
 ./tts - <code>Cette commande convertit le texte en voix</code> 
  
 ./video - Cette commande télécharge n'importe quelle vidéo YouTube en HD [<code>exemple /video https://youtu.be/exemple...</code>]

./font - Cette commande génère des polices stylées et cool [<code>exemple /font salut</code>]"""


    ADMIN_TXT = """Aide : Modules administrateur
<b>Note :</b>
Ce module fonctionne uniquement pour mes administrateurs
Commandes et utilisation :
• /logs - <code>pour obtenir les erreurs récentes</code>
• /stats - <code>pour obtenir le statut des fichiers dans la base de données. [Cette commande peut être utilisée par n'importe qui]</code>
• /delete - <code>pour supprimer un fichier spécifique de la base de données.</code>
• /users - <code>pour obtenir la liste de mes utilisateurs et leurs IDs.</code>
• /chats - <code>pour obtenir la liste de mes discussions et leurs IDs</code>
• /leave  - <code>pour quitter une discussion.</code>
• /disable  -  <code>pour désactiver une discussion.</code>
• /ban  - <code>pour bannir un utilisateur.</code>
• /unban  - <code>pour débannir un utilisateur.</code>
• /channel - <code>pour obtenir la liste de toutes les chaînes connectées</code>
• /broadcast - <code>pour diffuser un message à tous les utilisateurs</code>
• /grp_broadcast - <code>Pour diffuser un message à tous les groupes connectés.</code>
• /gfilter - <code>pour ajouter des filtres globaux</code>
• /gfilters - <code>pour voir la liste de tous les filtres globaux</code>
• /delg - <code>pour supprimer un filtre global spécifique</code>
• /request - <code>Pour envoyer une demande de film/série aux administrateurs du bot. Fonctionne uniquement sur le groupe de support. [Cette commande peut être utilisée par n'importe qui]</code>
• /delallg - <code>Pour supprimer tous les filtres globaux de la base de données du bot.</code>
• /deletefiles - <code>Pour supprimer les fichiers CamRip et PreDVD de la base de données du bot.</code>"""

    SEC_STATUS_TXT = """<b>★ Utilisateurs totaux : <code>{}</code>
★ Discussions totales : <code>{}</code>
★ Fichiers totaux : <code>{}</code>
★ Stockage utilisé : <code>{} MB</code>
★ Stockage libre : <code>{} MB</code></b>"""
    
    STATUS_TXT = """<b>Fichiers totaux de toutes les bases de données : <code>{}</code>

BASE DE DONNÉES UTILISATEURS :- 
★ Utilisateurs totaux : <code>{}</code>
★ Discussions totales : <code>{}</code>

PREMIÈRE BASE DE DONNÉES DE FICHIERS :-
★ Fichiers totaux : <code>{}</code>
★ Stockage utilisé : <code>{} MB</code>
★ Stockage libre : <code>{} MB</code>

SECONDE BASE DE DONNÉES DE FICHIERS :-
★ Fichiers totaux : <code>{}</code>
★ Stockage utilisé : <code>{} MB</code>
★ Stockage libre : <code>{} MB</code>

AUTRE BASE DE DONNÉES :-
★ Stockage utilisé : <code>{} MB</code>
★ Stockage libre : <code>{} MB</code></b>"""
    
    LOG_TEXT_G = """#NouveauGroupe
Groupe = {}(<code>{}</code>)
Membres totaux = <code>{}</code>
Ajouté par - {}"""

    LOG_TEXT_P = """#NouvelUtilisateur
ID - <code>{}</code>
Nom - {}"""

    ALRT_TXT = """Bonjour {},
ceci n'est pas votre demande de film,
demandez le vôtre..."""

    OLD_ALRT_TXT = """Hé {},
vous utilisez un de mes anciens messages, 
veuillez envoyer la demande à nouveau."""

    CUDNT_FND = """Je n'ai rien trouvé concernant {}
Vouliez-vous dire l'un de ceux-ci?"""

    I_CUDNT = """<b>Désolé aucun fichier n'a été trouvé pour votre demande {} 😕

Vérifiez votre orthographe sur Google et réessayez 😃

Format de demande de film 👇

Exemple : Uncharted ou Uncharted 2022 ou Uncharted En

Format de demande de série 👇

Exemple : Loki S01 ou Loki S01E04 ou Lucifer S03E24

🚯 N'utilisez pas ➠ ':(!,./)</b>"""

    I_CUD_NT = """Je n'ai trouvé aucun film lié à {}.
Veuillez vérifier l'orthographe sur Google ou IMDb..."""

    MVE_NT_FND = """Film non trouvé dans la base de données..."""

    TOP_ALRT_MSG = """Recherche du film dans la base de données..."""

    MELCOW_ENG = """<b>Bonjour {} 😍, Et bienvenue dans le groupe {} ❤️</b>"""

    SHORTLINK_INFO = """

🫵 Choisissez votre langue et gagnez de l'argent 💰"""

    REQINFO = """
⚠ Information ⚠

Après 5 minutes ce message sera automatiquement supprimé

Si vous ne voyez pas le fichier de film/série demandé, regardez à la page suivante"""

    SELECT = """Sélectionnez votre langue préférée, qualité, saison et épisode"""

    SINFO = """
🫣 Pour le film, rejoignez d'abord puis cliquez sur le bouton Réessayer 😅"""

    NORSLTS = """ 
★ #AucunRésultat ★

ID <b>: {}</b>

Nom <b>: {}</b>

Message <b>: {}</b>"""

    CAPTION = """<b>📂 Nom du fichier : {file_name} Par [<a href='t.me/WorldZPrime'>WorldZPrime</a></b>""" 

    IMDB_TEMPLATE_TXT = """
<b>Requête : {qurey}

Données IMDb :

<b>🏷 Titre</b>: <a href={url}>{title}</a>
🎭 Genres : {genres}
📆 Année : <a href={url}/releaseinfo>{year}</a>
🌟 Note : <a href={url}/ratings>{rating}</a> / 10 (basé sur {votes} avis d'utilisateurs.)
☀️ Langues : <code>Français</code>


⏰ Résultat affiché en : {remaining_seconds} <i>secondes</i> 🔥

Demandé par : {message.from_user.mention}</b>"""
    
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """
<b>Bienvenue dans les Filtres Globaux 🌍. Les Filtres Globaux sont les filtres définis par les administrateurs du bot qui fonctionneront sur tous les groupes.</b>
    
Commandes disponibles :
• /gfilter - <code>Pour créer un filtre global.</code>
• /gfilters - <code>Pour voir tous les filtres globaux.</code>
• /delg - <code>Pour supprimer un filtre global spécifique.</code>
• /delallg - <code>pour supprimer tous les filtres globaux.</code>"""
    
    FILE_STORE_TXT = """
<b>Le Stockage de Fichiers est la fonctionnalité qui créera un lien partageable d'un ou plusieurs fichiers 📂.</b>

Commandes disponibles :
• /batch - <code>Pour créer un lien groupé de plusieurs fichiers.</code>
• /link - <code>Pour créer un lien de stockage de fichier unique.</code>
• /pbatch - <code>Comme /batch, mais les fichiers seront envoyés avec des restrictions de transfert.</code>
• /plink - <code>Comme /link, mais le fichier sera envoyé avec des restrictions de transfert.</code>"""

    SONG_TXT = """<b>Module de téléchargement de musique 🎵</b> 
      
 <b>Module de téléchargement de musique, pour ceux qui aiment la musique. Vous pouvez utiliser cette fonctionnalité pour télécharger n'importe quelle chanson à vitesse super rapide. Fonctionne uniquement dans le bot et les groupes...</b> 
  
 <b>Commandes</b> :<b> 𝄟⃝.  /song nom de la chanson</b></b>""" 
  
    YTDL_TXT = """<b>Aide pour télécharger des vidéos depuis YouTube 📥. 
  
 Utilisation : Vous pouvez télécharger n'importe quelle vidéo depuis YouTube 
  
 Comment utiliser : tapez - /video ou /mp4 
  
 Exemple :<code>/mp4 https://youtu.be/exemple...</code></b>""" 
  
    TTS_TXT = """<b>Module TTS 🎤 : Convertir du texte en parole 
  
 Commandes et utilisation : /tts</b>""" 
  
    GTRANS_TXT = """<b>Aide : Traducteur Google 🌐 
  
 Cette commande vous aide à traduire un texte dans n'importe quelle langue que vous voulez. Cette commande fonctionne à la fois en MP et en groupe 
  
 Commandes et utilisation : /tr - pour traduire des textes vers une langue spécifique 
  
 Note : Lors de l'utilisation de /tr, vous devez spécifier le code de langue 
  
 Exemple: /𝗍𝗋 ml 
 • en = anglais 
 • ml = malayalam 
 • hi = hindi</b>""" 
  
    TELE_TXT = """<b>Aide : Module Telegraph! 
  
 Utilisation : /telegraph - envoyez-moi une image ou une vidéo de moins de (5mb) 
  
 Note : 
 Cette commande est disponible dans les groupes et les MPs 
 Cette commande peut être utilisée par tout le monde</b>""" 
  
    CORONA_TXT = """<b>Aide : Covid 🦠 
  
 Cette commande vous aide à connaître les informations quotidiennes sur le covid 
  
 Commandes et utilisation : 
  
 /covid - utilisez cette commande avec le nom de votre pays pour obtenir des informations sur le covid 
 Exemple:<code>/covid France</code> 
  
 ⚠️ Ce service a été arrêté 
  
 </b>""" 

    PROGRESS_BAR = """\n
╭━━━━❰ Le fichier est en cours de renommage... ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """
  
    ABOOK_TXT = """<b>Aide : Livre audio 📖 
  
 Vous pouvez convertir un fichier PDF en fichier audio avec cette commande ✯ 
  
 Commandes et utilisation : 
 /audiobook: Répondez à cette commande avec n'importe quel PDF pour générer l'audio 
</b>""" 
  
 
    PINGS_TXT = """<b>Test de ping : vous aide à connaître votre ping 🪄 
  
 Commandes : 
 • /alive - pour vérifier que vous êtes en ligne. 
 • /help - Pour obtenir de l'aide. 
 • /ping - <b>pour obtenir votre ping. 
  
 Utilisation : 
 • Ces commandes peuvent être utilisées en MP et dans les groupes 
 • Ces commandes peuvent être utilisées par tout le monde dans les groupes et les MPs du bot 
 • Partagez-nous pour plus de fonctionnalités 
  </b>""" 
  
    STICKER_TXT = """<b>Vous pouvez utiliser ce module pour trouver n'importe quel ID de sticker. 
 • Utilisation : pour obtenir un sticker 
   
 ⭕ Comment utiliser 
 /stickerid
 </b>""" 
  
    FONT_TXT= """<b>Utilisation 
  
 Vous pouvez utiliser ce module pour changer le style de police 
  
 Commande : /font votre texte (optionnel) 
 Exemple :- /font bonjour 
  
 </b>""" 
  
    PURGE_TXT = """<b>Purger 🗑️ 
      
 Supprimer beaucoup de messages des groupes !  
      
  Administrateur 
  
 ◉ /purge :- supprimer tous les messages du message auquel vous avez répondu, jusqu'au message actuel</b>""" 
  
    WHOIS_TXT = """<b>Module Whois 👤 
  
 Note:- Donne les détails d'un utilisateur 
 /whois :- donne tous les détails d'un utilisateur 📑 
 </b>""" 
  
    JSON_TXT = """<b> 
 JSON :  
 Le bot renvoie JSON pour tous les messages auxquels on a répondu avec /json 
  
 Fonctionnalités : 
  
 Édition de message JSON 
 Support MP 
 Support groupe 
  
 Note : 
  
 Tout le monde peut utiliser cette commande, si du spam se produit, le bot vous bannira automatiquement du groupe.</b>""" 
  
    URLSHORT_TXT = """<b>Aide : Raccourcisseur d'URL 🔗 
  
 <i><b>Cette commande vous aide à raccourcir une URL</i></b> 
  
 Commandes et utilisation : 
  
 /short: <b>utilisez cette commande avec votre lien pour obtenir des liens raccourcis</b> 
 Exemple:<code>/short https://youtu.be/exemple...</code> 
</b>""" 
  
    CARB_TXT = """<b>Aide pour Carbon 
  
 Carbon est une fonctionnalité pour créer l'image comme montré en haut avec vos textes. 
 Pour utiliser le module, envoyez simplement le texte et répondez-y avec la commande /carbon, le bot répondra avec l'image carbon 
</b>""" 
    GEN_PASS = """<b>Aide : Générateur de mot de passe 🔐 
  
 Rien de plus à savoir. Envoyez-moi la limite de votre mot de passe. 
 - Je vous donnerai le mot de passe de cette limite. 
  
 Commandes et utilisation : 
 • /genpassword ou /genpw 20 
  
 NOTE : 
 • Seuls les chiffres sont autorisés 
 • Maximum de chiffres autorisés jusqu'à 84 
 (Je ne peux pas générer de mots de passe au-dessus de la longueur 84) 
 • IMDʙ doit avoir les privilèges d'administrateur. 
 • Ces commandes fonctionnent à la fois en MP et en groupe. 
 • Ces commandes peuvent être utilisées par n'importe quel membre du groupe.</b>""" 
  
    SHARE_TXT = """<b>Obtenez l'URL de partage de votre texte. 
  
 - Ex :- /share
  
 </b>""" 
  
    PIN_TXT = """<b>Module d'épinglage 📌 
 Épingler un message... 
  
 Toutes les commandes liées à l'épinglage peuvent être trouvées ici : 
  
 📌Commandes et utilisation📌 
  
 /pin :- pour épingler le message sur vos discussions 
 /unpin :- pour désépingler le message actuellement épinglé</b>"""

    RESTART_TXT = """
<b>Bot redémarré ! 🔄

📅 Date : <code>{}</code>
⏰ Heure : <code>{}</code>
🌐 Fuseau horaire : <code>Asia/Kolkata</code>
🛠️ Statut de version : <code>v2.7.1 [ Stable ]</code></b>"""

    LOGO = """
████████╗███████╗███████╗██╗  ██╗    ╔██        ██╗       ██╗
╚═ ██╔══╝██╔════╝██╔════╝██║  ██║     ║██      ██║        ██║
   ██║    █████╗  ██║      ███████║      ║██    ██║         ██║
   ██║    ██╔══╝  ██║      ██╔══██║       ║██  ██║  ╔██     ██║
   ██║    ███████╗███████╗██║  ██║        ║████║   ║████████║
   ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═╝        ╚════╝   ╚════════╝"""
 
    TAMIL_INFO = """
ஏய் <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 இப்போது டெலிகிராமிலும் பணம் சம்பாதிக்கலாம்.

 தந்தி மூலம் பணம் சம்பாதிக்க உங்களிடம் 1 குழு இருக்க வேண்டும்.
 உங்களிடம் குழு இருந்தால், எங்கள் bot ஐ உங்கள் குழுவில் சேர்ப்பதன் மூலம் நீங்கள் பணம் சம்பாதிக்கலாம்.

 உங்கள் குழுவில் அதிக உறுப்பினர்கள் இருந்தால், உங்கள் வருமானம் அதிகரிக்கும்.

 எப்படி மற்றும் என்ன செய்ய வேண்டும்

 படி 1: இந்த VJ-FILTER-BOT போட் உங்கள் குழுவை நிர்வாகியாக்குங்கள்

 படி 2: உங்கள் இணையதளம் மற்றும் API ஐச் சேர்க்கவும்

 Exp: /shortlink xtz.in 4b392f8eb6ad711fbe58

 வீடியோவைச் சேர்க்கவும்

 👇 எப்படி சேர்ப்பது 👇

 Exp: /set_tutorial video link

மேலும் உங்கள் குழுவில் பயிற்சி வீடியோ தொகுப்பு ஆகிடும்..."""

    ENGLISH_INFO = """
Hey <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 Now you can earn money on Telegram too.

 You must have 1 group to earn money by telegram.
 If you have a group, you can earn money by adding our bot to your group.

 The more members you have in your group, the higher your income will be.

 How and what to do

 Step 1: Administer this VJ-FILTER-BOT bot to your group

 Step 2: Add your website and API

 Exp: /shortlink xtz.in 4b392f8eb6ad711fbe58

 Add a video

 👇 How to add 👇

 Exp: /set_tutorial video link

Also your tutorial will be Added Your Group..."""

    TELUGU_INFO = """
హే <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 ఇప్పుడు మీరు టెలిగ్రామ్‌లో కూడా డబ్బు సంపాదించవచ్చు.

 టెలిగ్రామ్ ద్వారా డబ్బు సంపాదించడానికి మీరు తప్పనిసరిగా 1 గ్రూప్‌ని కలిగి ఉండాలి.
 మీకు గ్రూప్ ఉన్నట్లయితే, మా బాట్‌ను మీ గ్రూప్‌కి జోడించడం ద్వారా మీరు డబ్బు సంపాదించవచ్చు.

 మీ గ్రూప్‌లో ఎంత ఎక్కువ మంది సభ్యులు ఉంటే మీ ఆదాయం అంత ఎక్కువగా ఉంటుంది.

 ఎలా మరియు ఏమి చేయాలి

 దశ 1: ఈ VJ-FILTER-BOT బాట్‌ని మీ సమూహానికి నిర్వహించండి

 దశ 2: మీ వెబ్‌సైట్ మరియు APIని జోడించండి

 గడువు: /shortlink xtz.in 4b392f8eb6ad711fbe58

 వీడియోను జోడించండి

 👇 ఎలా జోడించాలి 👇

 గడువు: /set_tutorial వీడియో లింక్

అలాగే మీ బృందం వీడియో సేకరణకు శిక్షణ ఇస్తుంది..."""

    HINDI_INFO = """
अरे <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 अब आप टेलीग्राम पर भी पैसे कमा सकते हैं।

 टेलीग्राम से पैसे कमाने के लिए आपके पास 1 ग्रुप होना चाहिए।
 यदि आपके पास एक समूह है, तो आप हमारे बॉट को अपने समूह में जोड़कर पैसा कमा सकते हैं।

 आपके समूह में जितने अधिक सदस्य होंगे, आपकी आय उतनी ही अधिक होगी।

 कैसे और क्या करना है

 चरण 1: इस फ़िल्टर-बॉट बॉट को अपने समूह में प्रशासित करें

 चरण 2: अपनी वेबसाइट और एपीआई जोड़ें

 एक्सप: /shortlink xtz.in 4b392f8eb6ad711fbe58

 एक वीडियो जोड़ें

 👇कैसे जोड़ें 👇

 ऍक्स्प: /set_tutorial वीडियो लिंक

साथ ही आपकी टीम वीडियो संग्रह का प्रशिक्षण भी देगी..."""

    MALAYALAM_INFO = """
ഹേയ് <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 ഇപ്പോൾ നിങ്ങൾക്ക് ടെലിഗ്രാമിലും പണം സമ്പാദിക്കാം.

 ടെലിഗ്രാം വഴി പണം സമ്പാദിക്കാൻ നിങ്ങൾക്ക് ഒരു ഗ്രൂപ്പ് ഉണ്ടായിരിക്കണം.
 നിങ്ങൾക്ക് ഒരു ഗ്രൂപ്പ് ഉണ്ടെങ്കിൽ, നിങ്ങളുടെ ഗ്രൂപ്പിലേക്ക് ഞങ്ങളുടെ ബോട്ട് ചേർത്തുകൊണ്ട് നിങ്ങൾക്ക് പണം സമ്പാദിക്കാം.

 നിങ്ങളുടെ ഗ്രൂപ്പിൽ കൂടുതൽ അംഗങ്ങൾ ഉണ്ടെങ്കിൽ, നിങ്ങളുടെ വരുമാനം ഉയർന്നതായിരിക്കും.

 എങ്ങനെ, എന്ത് ചെയ്യണം

 ഘട്ടം 1: ഈ തലപതി-ഫിൽട്ടർ-ബോട്ട് ബോട്ട് നിങ്ങളുടെ ഗ്രൂപ്പിലേക്ക് നൽകുക

 ഘട്ടം 2: നിങ്ങളുടെ വെബ്‌സൈറ്റും API-യും ചേർക്കുക

 കാലഹരണപ്പെടൽ: /shortlink xtz.in 4b392f8eb6ad711fbe58

 ഒരു വീഡിയോ ചേർക്കുക

 👇 എങ്ങനെ ചേർക്കാം 👇

 കാലഹരണപ്പെടൽ: /set_tutorial വീഡിയോ ലിങ്ക്

നിങ്ങളുടെ ടീം വീഡിയോ ശേഖരണവും പരിശീലിപ്പിക്കും..."""

    URTU_INFO = """
 <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 اب آپ ٹیلی گرام پر بھی پیسے کما سکتے ہیں۔

 ٹیلی گرام کے ذریعے پیسے کمانے کے لیے آپ کے پاس 1 گروپ ہونا ضروری ہے۔
 اگر آپ کا کوئی گروپ ہے، تو آپ ہمارے بوٹ کو اپنے گروپ میں شامل کر کے پیسے کما سکتے ہیں۔

 آپ کے گروپ میں جتنے زیادہ ممبر ہوں گے آپ کی آمدنی اتنی ہی زیادہ ہوگی۔

 کیسے اور کیا کرنا ہے۔

 مرحلہ 1: اپنے گروپ میں اس VJ-FILTER-BOT بوٹ کا انتظام کریں۔

 مرحلہ 2: اپنی ویب سائٹ اور API شامل کریں۔

 Exp: /shortlink xtz.in 4b392f8eb6ad711fbe58

 ایک ویڈیو شامل کریں۔

 👇 کیسے شامل کریں 👇

 Exp: /set_tutorial ویڈیو لنک

نیز آپ کی ٹیم ویڈیو جمع کرنے کی تربیت دے گی..."""

    GUJARATI_INFO = """
અરે <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 હવે તમે ટેલિગ્રામ પર પણ પૈસા કમાઈ શકો છો.

 ટેલિગ્રામ દ્વારા પૈસા કમાવવા માટે તમારી પાસે 1 જૂથ હોવું આવશ્યક છે.
 જો તમારી પાસે જૂથ છે, તો તમે અમારા બોટને તમારા જૂથમાં ઉમેરીને પૈસા કમાઈ શકો છો.

 તમારા જૂથમાં તમારા જેટલા વધુ સભ્યો હશે તેટલી તમારી આવક વધુ હશે.

 કેવી રીતે અને શું કરવું

 પગલું 1: તમારા જૂથમાં આ VJ-FILTER-BOT બોટનું સંચાલન કરો

 પગલું 2: તમારી વેબસાઇટ અને API ઉમેરો

 સમાપ્તિ: /shortlink xtz.in 4b392f8eb6ad711fbe58

 વિડિઓ ઉમેરો

 👇 કેવી રીતે ઉમેરવું 👇

 સમાપ્તિ: /set_tutorial વિડિઓ લિંક

તેમજ તમારી ટીમ વિડિયો કલેક્શનની તાલીમ આપશે..."""

    KANNADA_INFO = """
ಹೇ {message.from_user.mention}

 ಈಗ ನೀವು ಟೆಲಿಗ್ರಾಮ್‌ನಲ್ಲಿಯೂ ಹಣ ಗಳಿಸಬಹುದು.

 ಟೆಲಿಗ್ರಾಮ್ ಮೂಲಕ ಹಣ ಗಳಿಸಲು ನೀವು 1 ಗುಂಪನ್ನು ಹೊಂದಿರಬೇಕು.
 ನೀವು ಗುಂಪನ್ನು ಹೊಂದಿದ್ದರೆ, ನಮ್ಮ ಬೋಟ್ ಅನ್ನು ನಿಮ್ಮ ಗುಂಪಿಗೆ ಸೇರಿಸುವ ಮೂಲಕ ನೀವು ಹಣವನ್ನು ಗಳಿಸಬಹುದು.

 ನಿಮ್ಮ ಗುಂಪಿನಲ್ಲಿ ನೀವು ಹೆಚ್ಚು ಸದಸ್ಯರನ್ನು ಹೊಂದಿದ್ದರೆ, ನಿಮ್ಮ ಆದಾಯವು ಹೆಚ್ಚಾಗುತ್ತದೆ.

 ಹೇಗೆ ಮತ್ತು ಏನು ಮಾಡಬೇಕು

 ಹಂತ 1: ಈ ಫಿಲ್ಟರ್-ಬಾಟ್ ಬೋಟ್ ಅನ್ನು ನಿಮ್ಮ ಗುಂಪಿಗೆ ನಿರ್ವಹಿಸಿ

 ಹಂತ 2: ನಿಮ್ಮ ವೆಬ್‌ಸೈಟ್ ಮತ್ತು API ಸೇರಿಸಿ

 ಅವಧಿ: /shortlink xtz.in 4b392f8eb6ad711fbe58

 ವೀಡಿಯೊ ಸೇರಿಸಿ

 👇 ಸೇರಿಸುವುದು ಹೇಗೆ 👇

 ಅವಧಿ: /set_tutorial ವೀಡಿಯೊ ಲಿಂಕ್

ನಿಮ್ಮ ತಂಡವು ವೀಡಿಯೋ ಸಂಗ್ರಹಣೆಗೆ ತರಬೇತಿ ನೀಡಲಿದೆ..."""

    BANGLADESH_INFO = """
আরে <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 

 এখন আপনি টেলিগ্রামেও অর্থ উপার্জন করতে পারেন।

 টেলিগ্রামের মাধ্যমে অর্থ উপার্জন করতে আপনার অবশ্যই 1টি গ্রুপ থাকতে হবে।
 আপনার যদি একটি গ্রুপ থাকে, আপনি আপনার গ্রুপে আমাদের বট যোগ করে অর্থ উপার্জন করতে পারেন।

 আপনার গ্রুপে যত বেশি সদস্য থাকবেন আপনার আয় তত বেশি হবে।

 কিভাবে এবং কি করতে হবে

 ধাপ 1: আপনার গ্রুপে এই VJ-FILTER-BOT বট পরিচালনা করুন

 ধাপ 2: আপনার ওয়েবসাইট এবং API যোগ করুন

 মেয়াদ: /shortlink xtz.in 4b392f8eb6ad711fbe58

 একটি ভিডিও যোগ করুন

 👇 কিভাবে যোগ করবেন 👇

 মেয়াদ: /set_tutorial ভিডিও লিঙ্ক

এছাড়াও আপনার দল ভিডিও সংগ্রহের প্রশিক্ষণ দেবে..."""

    RENAME_TXT = """
🌌 <b><u>HOW TO SET THUMBNAIL</u></b>
  
•> /set_thumb - send any picture to automatically set thumbnail.
•> /del_thumb use this command and delete your old thumbnail.
•> /view_thumb use this command view your current thumbnail.

📑 <b><u>HOW TO SET CUSTOM CAPTION</u></b>

•> /set_caption - set a custom caption
•> /see_caption - see your custom caption
•> /del_caption - delete custom caption

Example:- /set_caption 📕 File Name: {filename}
💾 Size: {filesize}
⏰ Duration: {duration}

✏️ <b><u>HOW TO RENAME A FILE</u></b>

•> /rename - send any file and click rename option and type new file name and \nthen select [ document, video, audio ]👈 choice this.
"""

    STREAM_TXT = """<b><u>HOW TO GET STREAM AND DOWNLOAD LINK :</u>

/stream - ɢᴇᴛ sᴛʀᴇᴀᴍᴀʙʟᴇ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀɴʏ ғɪʟᴇ</b>"""


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


    
