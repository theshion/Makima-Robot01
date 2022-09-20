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
❂ Mᴀᴋɪᴍᴀ ɪs ᴀɴ ᴀɴɪᴍᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ ғʀᴏᴍ ᴄʜᴀɪɴsᴀᴡ ᴍᴀɴ ᴀɴɪᴍᴇ sʜᴇ ɪs ᴀ ᴅᴇᴠɪʟ ʜᴜɴᴛᴇʀ.

❂ ᴡᴇ ᴍᴀᴅᴇ ᴛʜɪs ᴍᴀᴋɪᴍᴀ  ʙᴇᴄᴀᴜsᴇ ᴀʟʀᴇᴀᴅʏ ᴀ ᴍᴀᴋɪᴍᴀ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ɪs ᴀʟʀᴇᴀᴅʏ ᴘᴏᴘᴜʟᴀʀ ᴀɴᴅ sʜᴇ ɪs ᴏɴᴇ ᴏғ ᴛʜᴇ ʙᴇsᴛ ᴀɴɪᴍᴇ ᴛʜᴇᴍᴇᴅ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴛʜᴏᴜɢʜ ʜᴇʀ ʀᴇᴘᴏ ɪs ɴᴏᴛ ᴘᴜʙʟɪᴄ sᴏ ᴀɴʏᴏɴᴇ ᴄᴀɴ'ᴛ ᴍᴀᴋᴇ ᴏᴡɴ ᴍᴀᴋɪᴍᴀ ᴀɴᴅ ᴅᴇᴘʟᴏʏ ɪᴛ.

❂ Sᴏ ᴡᴇ ᴛʜᴏᴜɢʜᴛ ʟᴇᴛs ɢɪᴠᴇ ɪᴛ ᴀ ᴛʀʏ ᴀɴᴅ ᴍᴀᴋᴇ ᴏᴡɴ ᴍᴀᴋɪᴍᴀ ᴀɴᴅ ᴡᴇ ᴋɴᴏᴡ ᴛʜᴀᴛ ᴡᴇ ɴᴏᴛ sᴜᴄᴄᴇssғᴜʟʟ ɪɴ ᴄᴏᴘʏɪɴɢ ᴛʜᴇ ᴏʀɪɢɪɴᴀʟ ɢᴏᴅᴅᴇss  ᴍᴀᴋɪᴍᴀ ʙᴜᴛ ᴡᴇ ᴀᴛʟᴇᴀsᴛ ɢɪᴠᴇ ɪᴛ ᴀ ᴛʀʏ
ᴀɴᴅ ɴᴏᴡ ᴍᴀᴋɪᴍᴀ ʀᴇᴘᴏ ɪs ɴᴏᴡ ᴘᴜʙʟɪᴄ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ʏᴏᴜ ᴄᴀɴ ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ᴍᴀᴋɪᴍᴀ.

⚠️ ɴᴏᴛᴇ :- 2.0 ɪs ɪɴ ᴘʀᴏᴄᴇss ᴡᴇ ᴡɪʟʟ ʀᴇʟᴇᴀsᴇ ɪᴛ sᴏᴏɴ ʙᴜᴛ ᴍᴀᴋɪᴍᴀ 2.0 ʀᴇᴘᴏ ᴡɪʟʟ ʙᴇ ᴘʀɪᴠᴀᴛᴇ sᴏ ɪғ ᴡᴀɴᴛ ᴛᴏ ʙᴜʏ ᴛʜᴀᴛ ʀᴇᴘᴏ ᴛʜᴀɴ ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴛᴀᴄᴛ.
"""


        update.effective_message.reply_photo(
            PHOTO,
            caption=TEXT,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    
                    [
                        InlineKeyboardButton(
                            text="ᴍᴀᴋɪᴍᴀ ʀᴇᴘᴏ", url="https://github.com/otakubinge/Makima-Robot"
                        ),
                        InlineKeyboardButton(
                            text="ᴍʏ ᴏᴡɴᴇʀ", url="https://t.me/SIXTH_H0KAGE"
                        ),
                    ],
                ]
            ),
        )

    ABOUT_handler = CommandHandler(("about", "source", "repo"), ABOUT)
    dispatcher.add_handler(ABOUT_handler)

    
