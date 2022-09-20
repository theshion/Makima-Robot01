# ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ɪɴ ᴀɴʏ ᴇʀʀᴏʀs ᴛʜᴀɴ ᴘʟᴢ ᴄᴏɴᴛᴀᴄᴛ @SIXTH_H0KAGE
# sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
# ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates
# ɴᴇᴛᴡᴏʀᴋ :- @Otaku_Binge

from pyrogram import filters

from MakimaRobot import pbot
from MakimaRobot.utils.errors import capture_err
from MakimaRobot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴀʀʙᴏɴ.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴀʀʙᴏɴ.`")
    m = await message.reply_text("😴`ɢᴇɴᴇʀᴀᴛɪɴɢ ᴄᴀʀʙᴏɴ...`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`ᴜᴩʟᴏᴀᴅɪɴɢ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴀʀʙᴏɴ...`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()



