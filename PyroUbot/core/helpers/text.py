from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import OWNER_ID, bot, ubot, get_expired_date


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b></blockquote>
"""

    def START(message):
        return f"""🛠 ʜᴀʟᴏ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a> 
〄➠ **ᴘᴇɴᴇᴊᴇʟᴀsᴀɴ: {bot.me.mention} ᴀᴅᴀʟᴀʜ ʙᴏᴛ ᴍᴜʟᴛɪ ᴄʟɪᴇɴᴛ ʏᴀɴɢ ʙɪsᴀ ᴅɪ ᴅᴇᴘʟᴏʏ,ᴜsᴇʀʙᴏᴛ ɪɴɪ ᴅɪ ʙᴜᴀᴛ ᴅᴇɴɢᴀɴ sᴀɴɢᴀᴛ ᴍᴜᴅᴀʜ. 
〄➠ **ᴘᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ: sᴀʏᴀ ᴅɪ ᴋᴇᴍʙᴀɴɢᴋᴀɴ ᴏʟᴇʜ <a href=tg://op<enmessage?user_id={OWNER_ID}>ᴠᴇɴɴᴏᴏғғᴄ</a>
<blockquote>〄➠ **ᴜsᴇʀʙᴏᴛ ɪɴɪ ᴅɪ ʟᴇɴɢᴋᴀᴘɪ ғɪᴛᴜʀ :**
 **• ᴍ𝖾𝗇𝗀𝗂𝗋𝗂𝗆 ᴘ𝖾𝗌𝖺𝗇 ᴋᴇ s𝖾𝗅𝗎𝗋𝗎𝗁 ɢ𝗋𝗈𝗎𝗉/𝗎𝗌𝖾𝗋𝗌 ʙᴇʀsᴀᴍᴀᴀɴ**
 **• ᴍᴇɴʏɪᴍᴘᴀɴ ғᴏᴛᴏ/ᴛᴇxᴛ ʜᴀɴʏᴀ ᴅᴇɴɢᴀɴ ᴄᴏᴍᴍᴀɴᴅ**
 **• ᴍᴇᴍɪʟɪᴋɪ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ᴀʟʟ sᴏsɪᴀʟ ᴍᴇᴅɪᴀ sᴇᴘᴇʀᴛɪ ᴛɪᴋᴛᴏᴋ,ɪɢ,ᴅʟʟ.**
 **• ᴍᴇʟɪʜᴀᴛ ᴍᴏᴅᴜʟᴇ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ ᴅᴀɴ ʙᴜᴛᴛᴏɴ.**
 **• ᴀɴɪᴍᴀsɪ, ᴀɴɪᴍᴇ, ᴅᴀɴ sᴜᴅᴀʜ ɴᴏ ᴡᴀᴛᴇʀᴍᴀʀᴋ 𝟷𝟶𝟶%.**
 **• ʙɪsᴀ ᴊᴜɢᴀ ᴜɴᴛᴜᴋ ᴊᴀsᴇʙ ᴏᴛᴏᴍᴀᴛɪs ʏɢʏ, sᴜᴅᴀʜ ʟᴇɴɢᴋᴀᴘ ᴅᴇɴɢᴀɴ ᴛᴜᴛᴏʀɪᴀʟɴʏᴀ</blockquote>**
〄➠ **ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴍᴇɴᴜ ᴅᴀɴ ᴍᴏᴅᴜʟᴇ sᴇᴄᴀʀᴀ ʟᴇɴɢᴋᴀᴘ sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴄᴇᴋ ᴍᴇɴᴜ.**
〄➠ **ᴄᴀᴛᴀᴛᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʟɪ ᴜsᴇʀʙᴏᴛ sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ʙᴜᴛᴛᴏɴ ʙᴇʟɪ ᴜsᴇʀʙᴏᴛ.
〄➠ **ᴊɪᴋᴀ ᴀɴᴅᴀ sᴜᴅᴀʜ ᴍᴇᴍʙᴇʟɪ sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ (ɪᴋᴜᴛɪɴ ᴀʀᴀʜᴀɴ ᴜʙᴏᴛ).**"""



    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>╭ ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: 10.000</b>
<b>│ ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
<b>│ Qʀɪꜱ ᴀʟʟ ᴘᴀʏᴍᴇɴᴛ </b>
<b>│ ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ: ʀᴘ 10.000</b>
<b>╰ ᴛᴏᴛᴀʟ ʙᴜʟᴀɴ: 10.000</b> 
ᴏᴡɴᴇʀ ᴜsᴇʀʙᴏᴛ <a href=tg://openmessage?user_id={OWNER_ID}>ɴᴀᴛᴢ ʟɪᴇ</a> 

<b>🛍 ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b></blockquote>
"""

    async def UBOT(count):
        return f"""
<blockquote><b>╭〢ᴜsᴇʀʙᴏᴛ ᴋᴇ </b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b>├〢ᴀᴄᴄᴏᴜɴᴛ </b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b>╰〢ᴜsᴇʀ ɪᴅ </b> <code>{ubot._ubot[int(count)].me.id}</code></blockquote>
"""

    def POLICY():
        return """ ᴊɪᴋᴀ ᴀᴅᴀ ᴋᴇɴᴅᴀʟᴀ sɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ  <a href=tg://openmessage?user_id={OWNER_ID}>ɴᴀᴛᴢ ʟɪᴇ</a> 
"""
