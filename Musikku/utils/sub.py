from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Musikku import app
from config import JOIN_DULU


async def subcribe(client, message):
    if not JOIN_DULU:
        return
    
    try:
        await app.get_chat_member(config.JOIN_DULU, message.from_user.id)
    except UserNotParticipant:
        try:
            link = f"t.me/{config.JOIN_DULU}"
            await message.reply(
                f"**Hay kak {message.from_user.mention}, Silahkan join dulu biar bisa pake bot ini kak**",
            reply_markup=InlineKeyboardMarkup(
                  [[InlineKeyboardButton("••ꜱɪʟᴀʜᴋᴀɴ ᴊᴏɪɴ••", url=link)]]
                        ),
            )
        except Exception as e:
            return await message.reply(f"**ERROR :** {e}")
        
            
