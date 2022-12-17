import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone -b beta https://github.com/TeamKillerX/KillerX-Base && cd KillerX-Base && pip3 install -r requirements.txt && python3 -m KillerXBase")
