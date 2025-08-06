import os
from typing import List

API_ID = int(os.getenv("API_ID", "21184495"))
API_HASH = os.getenv("API_HASH", "7238819d51a5280143fc3023a2f1abed")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7478540145:AAGtOR4C6y7-uCmL_c-VorFd5qM8rIPzBDA")
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://akashrabha2005:781120@cluster0.pv6yd2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID", "-1002829620846"))
ADMIN_ID = int(os.getenv("ADMIN_ID", "8110231942"))
LOG_CHNL = int(os.getenv("LOG_CHNL", "-1002764219378"))
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "AlwaysToHelpBot") # Without @
IS_FSUB = bool(os.environ.get("FSUB", False))
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "").split()))
DATABASE_CHANNEL_LOG = int(os.getenv("DATABASE_CHANNEL_ID", "-1002635795381"))
FREE_VIDEO_DURATION = int(os.getenv("FREE_VIDEO_DURATION", "500"))

