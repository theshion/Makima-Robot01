# ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ɪɴ ᴀɴʏ ᴇʀʀᴏʀs ᴛʜᴀɴ ᴘʟᴢ ᴄᴏɴᴛᴀᴄᴛ @SIXTH_H0KAGE
# sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
# ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates
# ɴᴇᴛᴡᴏʀᴋ :- @Otaku_Binge

import requests
from telegram import Update
from telegram.ext import CallbackContext

from MakimaRobot import dispatcher
from MakimaRobot.modules.disable import DisableAbleCommandHandler


def truth(update: Update, context: CallbackContext):
    context.args
    truth = requests.get("https://elianaapi.herokuapp.com/games/truth").json()
    truth = truth.get("truth")
    update.effective_message.reply_text(truth)


def dare(update: Update, context: CallbackContext):
    context.args
    dare = requests.get("https://elianaapi.herokuapp.com/games/dares").json()
    dare = dare.get("dare")
    update.effective_message.reply_text(dare)


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__help__ = """
*Truth & Dare*
 ❂ /truth *:* Sends a random truth string.
 ❂ /dare *:* Sends a random dare string.
"""
__mod_name__ = "Tʀᴜᴛʜ-Dᴀʀᴇ🎰"
