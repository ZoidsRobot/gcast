## KillerX-Base

![Python Version](https://img.shields.io/badge/python-3.9-green?style=for-the-badge&logo=appveyor)
![Issues](https://img.shields.io/github/issues/TeamKillerX/KillerX-Base?style=for-the-badge&logo=appveyor)
![Forks](https://img.shields.io/github/forks/TeamKillerX/KillerX-Base?style=for-the-badge&logo=appveyor)
![Stars](https://img.shields.io/github/stars/TeamKillerX/KillerX-Base?style=for-the-badge&logo=appveyor)
![Contributors](https://img.shields.io/github/contributors/TeamKillerX/KillerX-Base?style=for-the-badge&logo=appveyor)
![Repository Size](https://img.shields.io/github/repo-size/TeamKillerX/KillerX-Base?style=for-the-badge&logo=appveyor)
[![Docker Pulls](https://img.shields.io/docker/pulls/rendyprojects/python)](https://hub.docker.com/r/rendyprojects/python/tags)

![back](https://user-images.githubusercontent.com/90479255/178405323-34f4af0b-5c1e-4822-b0d6-eb578e30ff54.png)
```
️                       ⚠️ WARNING FOR YOU ️ ️⚠️
   KillerXBase is used to help your account activities on Telegram
   We are not responsible for what you misuse in this repository
   !  Be careful when using this repository!
   If one of the members misuses this repository, we are forced to ban you
   Never ever abuse this repository
``` 
## Tutorial Coding Pyrogram
<details> 
<summary>How to create new file</summary>

  - View code 
  - Click 3 dots 
  - Select create new files

<img src="./resources/coding.jpg" alt="details">

- try use `test.py`
```python
import asyncio
from pyrogram import Client as ren
from pyrogram.types import *
from pyrogram import Client
from KillerXBase.helper.basic import *
from KillerXBase.helper.adminHelpers import *
from KillerXBase.helper.cmd import *
from KillerXBase.helper.dev import *
from KillerXBase.helper.misc import *
from KillerXBase.modules.help import *

@ren.on_message(filters.command("test", cmd) & filters.me)
async def test(client: Client, message: Message):
    await asyncio.gather(message.delete(), client.send_message(message.chat.id, "**hello World"*", reply_to_message_id=ReplyCheck(message),),)


add_command_help(
    "test",
    [
        ["test", "Hello World"],
    ],
)
```

</details>

## Deploy On KillerXBase

<details> 
<summary>See Click</summary>

## Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://killerxbase.vercel.app/)

## Cloud Okteto
[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/TeamKillerX/KillerX-Base)

## Railway App
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/9Me5Kj?referralCode=NzLfjZ)

## Tutorial VPS
```console
Rendy@Ubuntu~ $ sudo apt update && sudo apt upgrade -y && sudo apt-get install -y curl git npm screen ffmpeg && sudo apt-get install python3-pip -y
Rendy@Ubuntu~ $ git clone https://github.com/TeamKillerX/KillerX-Base && cd KillerX-Base
Rendy@Ubuntu~ $ pip3 install -r req *
Rendy@Ubuntu~ $ cp sample_config.env config.env
Rendy@Ubuntu~ $ nano config.env
Rendy@Ubuntu~ $ screen -S base 
Rendy@Ubuntu~ $ python3 -m KillerXBase

# ctrl a + d 
```

</details> 

## Credits
- [KillerX-Base](https://github.com/TeamKillerX/KillerX-Base)
- [Zaid-Userbot](https://github.com/ITZ-ZAID/ZAID-USERBOT)
- [PyroMan-Userbot](https://github.com/mrismanaziz/PyroMan-Userbot)

## library 
- [Pyrogram](https://github.com/pyrogram)
