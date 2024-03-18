import os
import sys
import json
import time
import requests
import websocket
from keep_alive import keep_alive

GUILD_ID = os.getenv("guild_id")
CHANNEL_ID = os.getenv("channel_id")
SELF_MUTE = True
SELF_DEAF = False

usertoken = os.getenv("token")
if not usertoken:
    print("[ERROR] Please add a token inside Secrets.")
    sys.exit()

headers = {"Authorization": usertoken, "Content-Type": "application/json"}

validate = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers)
if validate.status_code != 200:
  print("[ERROR] Your token might be invalid. Please check it again.")
  sys.exit()

userinfo = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

def joiner(token):
    start = json.loads(ws.recv())
    heartbeat = start['d']['heartbeat_interval']
    auth = {"op": 2,"d": {"token": token,"properties": {"$os": "Windows 10","$browser": "Google Chrome","$device": "Windows"},"s": None,"t": None}
    vc = {"op": 4,"d": {"guild_id": GUILD_ID,"channel_id": CHANNEL_ID,"self_mute": SELF_MUTE,"self_deaf": SELF_DEAF}}
    time.sleep(heartbeat / 1000)

def run_joiner():
  os.system("clear")
  print(f"Logged in as {username}#{discriminator} ({userid}).")
  while True:
    joiner(usertoken, status)
    time.sleep(30)

keep_alive()
run_joiner()
