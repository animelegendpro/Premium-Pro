from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**๏ Fʀᴇᴇ ᴘʟᴀɴ ᴜsᴇʀ**

        ☞ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ: 2.0 GB
        ☞ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇꜱꜱ: 2
        ☞ ᴛɪᴍᴇᴏᴜᴛ: 1 ᴍɪɴᴜᴛᴇꜱ
        ☞ ᴛɪᴍᴇ ɢᴀᴘ: ʏᴇꜱ
	
	**▼ Uᴘɢʀᴀᴅᴇ ᴘʟᴀɴ ▼**"""
	keybord = InlineKeyboardMarkup([[ 
        		       [InlineKeyboardButton("ғʀᴇᴇ", callback_data='free'),
                                InlineKeyboardButton("sɪʟᴠᴇʀ", callback_data='silver')],
                               [InlineKeyboardButton("ɢᴏʟᴅᴇɴ", callback_data='golden'),
			        InlineKeyboardButton("ᴅɪᴀᴍᴏɴᴅ", callback_data='diamond')],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**๏ Fʀᴇᴇ ᴘʟᴀɴ ᴜsᴇʀ**

        ☞ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ: 2.0 GB
        ☞ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇꜱꜱ: 2
        ☞ ᴛɪᴍᴇᴏᴜᴛ: 1 ᴍɪɴᴜᴛᴇꜱ
        ☞ ᴛɪᴍᴇ ɢᴀᴘ: ʏᴇꜱ
	
	**▼ Uᴘɢʀᴀᴅᴇ ᴘʟᴀɴ ▼**"""
	keybord = InlineKeyboardMarkup([[ 
        		       [InlineKeyboardButton("ғʀᴇᴇ", callback_data='free'),
                                InlineKeyboardButton("sɪʟᴠᴇʀ", callback_data='silver')],
                               [InlineKeyboardButton("ɢᴏʟᴅᴇɴ", callback_data='golden'),
			        InlineKeyboardButton("ᴅɪᴀᴍᴏɴᴅ", callback_data='diamond')],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)







# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
