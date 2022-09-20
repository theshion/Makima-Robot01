# ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ɪɴ ᴀɴʏ ᴇʀʀᴏʀs ᴛʜᴀɴ ᴘʟᴢ ᴄᴏɴᴛᴀᴄᴛ @SIXTH_H0KAGE
# sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
# ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates
# ɴᴇᴛᴡᴏʀᴋ :- @Otaku_Binge

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler

from MakimaRobot import dispatcher

PHOTO = "https://te.legra.ph/file/d1d1ac98666a20b2a4d37.jpg"

about_name = "makima info"

if about_name == "makima info":

    def ABOUT(update: Update, context: CallbackContext):

        TEXT = f"""
MAKIMA IS AN ANIME CHARACTER FROM CHAINSAW MAN SHE IS A DEVIL HUNTER,
WE MAKE THIS MAKIMA BECAUSE ALREADY A MAKIMA ON TELEGRAM IS REALLY POPULAR AND 
SHE IS ONE OF THE BEST TELEGRAM MANAGEMENT THOUGH HER REPO IS NOT PUBLIC SO ANYONE CAN'T 
DEPLOY HER,
SO WE THOUGHT LET'S MAKE OWN MAKIMA AND WE ARE STILL WORKING ON IT,AFTER WE FINISH OUR WORK 
WE WILL KEEP THIS REPO PRIVATE FOR SOMETIME
BUT YOU CAN GET THE REPO NOW BY CONTACTING [𝓚𝒶кคѕⒽᎥ ђ𝔞𝓉ᗩЌ𝒆 ⸙『𝕭𝖎𝖓𝖌𝖊』 ᭄™](https://t.me/SIXTH_H0KAGE)

CREDIT:-
• [MAKIMA](https://t.me/Makima_UltraXBot) **THANKS FOR INSPIRATION❤️**
• [Makima ROBOT](https://t.me/FallenXRobot) thanks for the base repo

"""

        update.effective_message.reply_photo(
            PHOTO,
            caption=TEXT,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Oᴛᴀᴋᴜ • ʙɪɴɢᴇ 𝙉𝙚𝙩𝙬𝙤𝙧𝙠", url="https://t.me/Otaku_Binge"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text="Main chat group ♦️", url="https://t.me/anichatbakwas"
                        ),
                        InlineKeyboardButton(
                            text="support 🥂", url="https://t.me/kakashi_bots_support"
                        ),
                    ],
                ]
            ),
        )

    ABOUT_handler = CommandHandler(("about", "source", "repo"), ABOUT)
    dispatcher.add_handler(ABOUT_handler)

    __help__ = """
    ──「MAKIMA INFO & HISTORY」──                         
    
    ❂ /about / /source / /repo: Get information about makima"""

    __mod_name__ = "ABOUT"
