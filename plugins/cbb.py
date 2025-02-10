from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""<b>𝖠𝖻𝗈𝗎𝗍...\n\n›› 𝖬𝖺𝖽𝖾 𝖿𝗈𝗋 : <a href='https://t.me/Zoroflix'>𝖹𝖮𝖱𝖮𝖥𝖫𝖨𝖷</a> \n›› 𝖮𝗐𝗇𝖾𝖽 𝖻𝗒 : <a tg://user?id={OWNER_ID}'> 𝖠𝗄𝖺𝗌𝗁</a> !! </b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴏᴍᴇ", callback_data = "home"),
                 InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close")]
            ])
        )    

    if data == "home":
        await query.message.edit_text(
            text = START_MSG.format(
                first = query.from_user.first_name,
                last = query.from_user.last_name,
                username = None if not query.from_user.username else '@' + query.from_user.username,
                mention = query.from_user.mention,
                id = query.from_user.id
            ),
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data = "about"),
                 InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close")]
            ])
        )  

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass




# Don't Remove Credit 🥺
# Telegram Channel @AxomBotz
# Developer @imakashrabha
