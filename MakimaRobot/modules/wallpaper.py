#ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ɪɴ ᴀɴʏ ᴇʀʀᴏʀs ᴛʜᴀɴ ᴘʟᴢ ᴄᴏɴᴛᴀᴄᴛ @SIXTH_H0KAGE
#sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
#ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates
#ɴᴇᴛᴡᴏʀᴋ :- @Otaku_Binge

import io
import os

import requests
from PIL import Image
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from MakimaRobot import SUPPORT_CHAT, dispatcher, pbot


def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@pbot.on_message(filters.command(["wall"]))
async def wall(client, message):
    quew = get_text(message)
    if not quew:
        await client.send_message(
            message.chat.id, "😶 **ᴩʟᴇᴀsᴇ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ ᴡᴀʟʟᴩᴀᴩᴇʀ !**"
        )
        return
    m = await client.send_message(message.chat.id, "⚙️ **sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ᴡᴀʟʟᴩᴀᴩᴇʀ...**")
    try:
        text = get_text(message)
        LOGO_API = f"https://single-developers.up.railway.app/wallpaper?search={text}"
        randc = LOGO_API
        murl = (
            requests.get(
                f"https://single-developers.up.railway.app/wallpaper?search={text}"
            )
            .history[1]
            .url
        )
        img = Image.open(io.BytesIO(requests.get(randc).content))
        fname = "fallenrobot.png"
        img.save(fname, "png")
        caption = f"""
♦️ ᴡᴀʟʟᴩᴀᴩᴇʀ ɢᴇɴᴇʀᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ 

♦️ **ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ :** [{dispatcher.bot.first_name}](https://t.me/{dispatcher.bot.username})
♦️ **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
♦️ **ᴅᴏᴡɴʟᴏᴀᴅ :** `{murl}`
"""
        await m.delete()
        await client.send_photo(
            message.chat.id,
            photo=murl,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("• ʟɪɴᴋ •", url=f"{murl}")],
                ]
            ),
        )
        if os.path.exists(fname):
            os.remove(fname)
    except Exception as e:
        await client.send_message(
            message.chat.id,
            f"sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ.\nᴩʟᴇᴀsᴇ ʀᴇᴩᴏʀᴛ ᴛʜɪs ᴀᴛ @{SUPPORT_CHAT}\n\n**ᴇʀʀᴏʀ :** {e}",
        )
