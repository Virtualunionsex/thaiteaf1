import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5679702303:AAHt0T6CRBAi6H5XfRufu2A5L4TCU99hqq8")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16246834"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001636429528"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7423630"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://azbxclgr:YADtY7HIPvuaHWXMhZ_MXXksMXJCkegm@queenie.db.elephantsql.com/azbxclgr")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001875335696"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nJoin group dan Channel gua dulu ya bang kalaw mau dapat video free.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5591632852").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>Join Grup dan Channelnya dulu ya\n\nKalaw mau nggak ribet join sana sini order VIP ke admin ya</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(7423630)
ADMINS.append(5591632852)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
