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


from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('free'))
async def upgrade(bot,update):
	text = """**❤️‍🔥 <u>sɪʟᴠᴇʀ ᴘʟᴀɴ</u>**

        <b>☞ ᴜᴘʟᴏᴀᴅ 2ɢʙ ꜰɪʟᴇꜱ: ᴛʀᴜᴇ</b>
        <b>☞ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ: 2ɢʙ</b>
        <b>☞ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇꜱꜱ: 2</b>
        <b>☞ ᴛɪᴍᴇ ɢᴀᴘ: ɴᴏ ᴛɪᴍᴇ ɢᴀᴘ</b>

        **💰 <u>ᴘʟᴀɴ ᴘʀɪᴄᴇ</u>**

        <b>☞ ᴘʀɪᴄᴇ: 0</b>
        <b>☞ ᴠᴀʟɪᴅɪᴛʏ: ʟɪғᴇᴛɪᴍᴇ</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			[InlineKeyboardButton("《 Bᴀᴄᴋ", callback_data='upgrade'),
        			InlineKeyboardButton("Bᴜʏ",url = " https://t.me/Devil_Eyes_ZBot")] ]]) 
	await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('silver'))
async def upgrade(bot,update):
	text = """**🥈 <u>sɪʟᴠᴇʀ ᴘʟᴀɴ</u>**

        <b>☞ ᴜᴘʟᴏᴀᴅ 4ɢʙ ꜰɪʟᴇꜱ: ᴛʀᴜᴇ</b>
        <b>☞ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ: 20.0ɢʙ</b>
        <b>☞ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇꜱꜱ: 2</b>
        <b>☞ ᴛɪᴍᴇ ɢᴀᴘ: ɴᴏ ᴛɪᴍᴇ ɢᴀᴘ</b>

        **💰 <u>ᴘʟᴀɴ ᴘʀɪᴄᴇ</u>**

        <b>☞ ᴘʀɪᴄᴇ: ₹49</b>
        <b>☞ ᴠᴀʟɪᴅɪᴛʏ: 𝟹𝟶ᴅᴀʏs</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			[InlineKeyboardButton("《 Bᴀᴄᴋ", callback_data='upgrade'),
        			InlineKeyboardButton("Bᴜʏ",url = " https://t.me/Devil_Eyes_ZBot")] ]]) 
	await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('golden'))
async def upgrade(bot,update):
	text = """**🎖 <u>Gᴏʟᴅᴇɴ ᴘʟᴀɴ</u>**

        <b>☞ ᴜᴘʟᴏᴀᴅ 4ɢʙ ꜰɪʟᴇꜱ: ᴛʀᴜᴇ</b>
        <b>☞ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ: 50.0ɢʙ</b>
        <b>☞ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇꜱꜱ: 3</b>
        <b>☞ ᴛɪᴍᴇ ɢᴀᴘ: ɴᴏ ᴛɪᴍᴇ ɢᴀᴘ</b>

        **💰 <u>ᴘʟᴀɴ ᴘʀɪᴄᴇ</u>**

        <b>☞ ᴘʀɪᴄᴇ: ₹99</b>
        <b>☞ ᴠᴀʟɪᴅɪᴛʏ: 𝟹𝟶ᴅᴀʏs</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			[InlineKeyboardButton("《 Bᴀᴄᴋ", callback_data='upgrade'),
        			InlineKeyboardButton("Bᴜʏ",url = " https://t.me/Devil_Eyes_ZBot")] ]]) 
	await update.message.edit(text = text,reply_markup = keybord)

 @Client.on_callback_query(filters.regex('diamond'))
async def upgrade(bot,update):
	text = """**💎 <u>Dɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u>**

        <b>☞ ᴜᴘʟᴏᴀᴅ 4ɢʙ ꜰɪʟᴇꜱ: ᴛʀᴜᴇ</b>
        <b>☞ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ: 100.0ɢʙ</b>
        <b>☞ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇꜱꜱ: 5</b>
        <b>☞ ᴛɪᴍᴇ ɢᴀᴘ: ɴᴏ ᴛɪᴍᴇ ɢᴀᴘ</b>

        **💰 <u>ᴘʟᴀɴ ᴘʀɪᴄᴇ</u>**

        <b>☞ ᴘʀɪᴄᴇ: ₹159</b>
        <b>☞ ᴠᴀʟɪᴅɪᴛʏ: 𝟹𝟶ᴅᴀʏs</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			[InlineKeyboardButton("《 Bᴀᴄᴋ", callback_data='upgrade'),
        			InlineKeyboardButton("Bᴜʏ",url = " https://t.me/Devil_Eyes_ZBot")] ]]) 
	await update.message.edit(text = text,reply_markup = keybord)
