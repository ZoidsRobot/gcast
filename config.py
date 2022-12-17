from os import getenv
from dotenv import load_dotenv
from base64 import b64decode as who
from KillerXBase.helper.error import *

load_dotenv("config.env")

API_ID = int(getenv("API_ID", "")) 
API_HASH = getenv("API_HASH")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID", ""))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
PACK_NAME = getenv("PACK_NAME", "kang pack")

BOT_VER = "0.1.9@beta"
BRANCH = getenv("BRANCH", "beta") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", None)
STRING_SESSION3 = getenv("STRING_SESSION3", None)
STRING_SESSION4 = getenv("STRING_SESSION4", None)
STRING_SESSION5 = getenv("STRING_SESSION5", None)
STRING_SESSION6 = getenv("STRING_SESSION6", None)
STRING_SESSION7 = getenv("STRING_SESSION7", None)
STRING_SESSION8 = getenv("STRING_SESSION8", None)
STRING_SESSION9 = getenv("STRING_SESSION9", None)
STRING_SESSION10 = getenv("STRING_SESSION10", None)
