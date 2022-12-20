from os import getenv
from dotenv import load_dotenv
from base64 import b64decode as who

# jangan hapus && auto crashed

GIT_TOKEN = getenv(
    "GIT_TOKEN",
    who("").decode("utf-8"),
)


REPO_URL = getenv(
    "REPO_URL",
    who("aHR0cHM6Ly9naXRodWIuY29tL1RlYW1LaWxsZXJYL0tpbGxlclgtQmFzZQ==").decode("utf-8"),
)

CHANNEL = who("UmVuZHlQcm9qZWN0cwo=").decode("utf-8")
SUPPORT = who("cGFudGVreWtzCg==").decode("utf-8")
