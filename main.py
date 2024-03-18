import os
import sys
import json
import time
import requests
from keep_alive import keep_alive

GUILD_ID = os.getenv("guild_id")
CHANNEL_ID = os.getenv("channel_id")
SELF_MUTE = True
SELF_DEAF = False

usertoken = os.getenv("token")
if not usertoken:
    print("[ERROR] Please add a token inside Secrets.")
    sys.exit()

@client.event
async def on_ready():
    os.system("clear")
    print('Logged in as {client.user} {client user.id')
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id = CHANNEL_ID)
    await vs.guild.change_voice_state(channel=vc, self_mute=True, self_deaf=True)
    print("Succesfully joined {vc.name} {vc.id}")

keep_alive()
