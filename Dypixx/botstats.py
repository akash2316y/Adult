'''
Smile, please... 😊
Goodbye forever.

Thank you all for your care and support throughout this journey.

Unfortunately, my @dypixx account has been hacked. The hacker is now using it to promote unknown content. Please be cautious, stay alert, and don’t fall for anything they post.

Take care, stay safe — and once again, thank you for everything.
Goodbye.

— Dypixx
'''

from pyrogram import *
from vars import ADMIN_ID
from Database.maindb import mdb
from Database.userdb import udb
from bot import bot
import time

async def get_readable_time(seconds: int) -> str:
    time_data = []
    for unit, div in [("d", 86400), ("h", 3600), ("m", 60), ("s", 1)]:
        value, seconds = divmod(seconds, div)
        if value > 0 or unit == "s":
            time_data.append(f"{int(value)}{unit}")
    return " ".join(time_data)

@Client.on_message(filters.command("stats") & filters.private)
async def stats_command(client, message):
    if message.from_user.id != ADMIN_ID:
        await message.delete()
        await message.reply_text("**🚫 You’re not authorized to use this command...**")
        return
    video_count = await mdb.count_all_videos()
    total_users = await udb.get_all_users()
    bot_uptime = int(time.time() - bot.START_TIME)
    uptime = await get_readable_time(bot_uptime)
    STATS = ">**🤖 Bot Statistics**\n\n"
    STATS += f"**Total Users: {len(total_users)}\n**"
    STATS += f"**Total Files in DB: {video_count}\n**"
    STATS += f"**BOT Uptime: {uptime}**"
    await message.reply_text(STATS)
