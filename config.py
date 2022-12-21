from os import getenv
from dotenv import load_dotenv
from base64 import b64decode as who
from KillerXBase.helper.error import *

load_dotenv("config.env")

API_ID = int(getenv("API_ID", "9774346")) 
API_HASH = getenv("API_HASH", "a92aed7d74654a563af4b07efbcd88e9")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "907544310").split()))
OWNER_ID = int(getenv("OWNER_ID", "907544310"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://ubot:Rextor99@ubot.dmvt6ch.mongodb.net/?retryWrites=true&w=majority")
DB_URL = getenv("DATABASE_URL", "postgres://mxdgysvq:ZeYsob0qEIz44VqgB6YEcKUlaRySpUdp@peanut.db.elephantsql.com/mxdgysvq")
BOT_TOKEN = getenv("BOT_TOKEN", "5817963475:AAEKCmCUOp32AsNNmf1RLZfrMsLKLwXEbnM")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = int(getenv("LOG_GROUP", "-1001581658290"))
PACK_NAME = getenv("PACK_NAME", "kang pack")

# don't kanger repo this !!!
CHANNEL = "@RendyProjects"
SUPPORT = "@pantekyks"

BOT_VER = "0.2.1@dev"
BRANCH = getenv("BRANCH", "dev") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQAhIHQAuhslv3a1b_FnxqLK9rczZ7LBYYKy64WoeFPyIFWABwQ4h9BhS1ZlU0pBjwumQ_zE1HniWMJnpCMAXbjYG6v60ckViK9U7ioLOmNDJTH5cHAHwH_P4rTmaB8TytE29yJI5rk2MqV8VI0VOJVEmXRIdLoLGRKmFur_sx-kHPnwjUP6ISACueYPHoc7hOkpeGF1PJ_1j1QlOsDKgeg8XG6KOB1Z7QJzxqDijdqmcU0Yv6Rf2p5znhl9DOcceutRwqnPzcbzrHZypwPvTIG62hYHu4UkE5IPwEqZ9iUCARZcC35qv1LawJlBQFgrKT7pOsX63z7oAgUb3Swyc5CmhrBWcQAAAAA2GAb2AA")
STRING_SESSION2 = getenv("STRING_SESSION2", None)
STRING_SESSION3 = getenv("STRING_SESSION3", None)
STRING_SESSION4 = getenv("STRING_SESSION4", None)
STRING_SESSION5 = getenv("STRING_SESSION5", None)
STRING_SESSION6 = getenv("STRING_SESSION6", None)
STRING_SESSION7 = getenv("STRING_SESSION7", None)
STRING_SESSION8 = getenv("STRING_SESSION8", None)
STRING_SESSION9 = getenv("STRING_SESSION9", None)
STRING_SESSION10 = getenv("STRING_SESSION10", None)
