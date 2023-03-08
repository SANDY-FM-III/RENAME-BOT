import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Movies BOT :- <a href='https://t.me/SANDMAN_AUTO_BOT'>Sandman Auto</a>\nCreater :- <a href='https://t.me/syrus_143_hpy'>🦋SandMan🦋</a>\nLanguage :- Python3\nLibrary :- Pyrogram 2.0\nServer :- Heroku\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n Thank you **<a href='https://t.me/fm_onr'>Sandy</a>** for your hard work \n\n❤️ we love you <a href='https://t.me/syrus_143_hpy'>**Sandy**</a> ❤️",quote=True)
