from os import getenv
from dotenv import load_dotenv
from base64 import b64decode as who

GIT_TOKEN = getenv(
    "GIT_TOKEN",
    who("").decode("utf-8"),
)
