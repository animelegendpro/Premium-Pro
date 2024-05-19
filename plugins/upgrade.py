from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters
from callback import silver , golden , diamond

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**ғʀᴇᴇ ᴘʟᴀɴ ᴜsᴇʀ**
	ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟸ɢʙ
	ᴘʀɪᴄᴇ 𝟶
	
	**🥈 Sɪʟᴠᴇʀ** 
	ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ 20GB
	ᴘʀɪᴄᴇ ʀs 49  ɪɴᴅɪᴀ /🌎 0.59$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	**🎖 Gᴏʟᴅᴇɴ**
	ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 50GB
	ᴘʀɪᴄᴇ ʀs 99  ɪɴᴅɪᴀ /🌎 1.19$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	**💎 ᴅɪᴀᴍᴏɴᴅ**
	ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 100GB
	ᴘʀɪᴄᴇ ʀs 159  ɪɴᴅɪᴀ /🌎 2.16$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	
	ᴘᴀʏ ᴜsɪɴɢ ᴜᴘɪ ɪ'ᴅ `anime-legend@axl`
	
	<b>ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛs ᴏғ</b> 
        <b>ᴘᴀʏᴍᴇɴᴛ ᴛᴏ ᴀᴅᴍɪɴ @Devil_Eyes_ZBot</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Sɪʟᴠᴇʀ", callback_data='silver')], 
        			[InlineKeyboardButton("Gᴏʟᴅᴇɴ", callback_data='golden'),
        			InlineKeyboardButton("Dɪᴀᴍᴏɴᴅ", callback_data='diamond')],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """<b>Free Plan Users</b>

        <b>☞ Daily Upload: 2.0 GB</b>
        <b>☞ Parallel Process: 2</b>
        <b>☞ Timeout: 1 Minutes</b>
        <b>☞ Time Gap: Yes</b>
	
        <b>▼ Upgrade Plan ▼</b>"""
	keybord = InlineKeyboardMarkup([
                               [InlineKeyboardButton('Sɪʟᴠᴇʀ', callback_data='silver'),
                               InlineKeyboardButton('Gᴏʟᴅᴇɴ', callback_data='golden')],
                               [InlineKeyboardButton('Dᴜʏ', url = "https://t.me/Devil_Eyes_ZBot"),
                               InlineKeyboardButton('Dɪᴀᴍᴏɴᴅ', callback_data='diamond')] 
	                       ]) 
	await message.reply_text(text = text,reply_markup = keybord)








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
