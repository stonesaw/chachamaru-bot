import os
import random
import re
import time
import datetime
import json
from dotenv import load_dotenv

import discord
from discord.ext import tasks, commands

load_dotenv(verbose=True)


on_chacha = True
funfun_done = True

GREETING = [
    'へー、おまえっていうのかか！\nなんだかおまえとは、仲良くできる気がするぞ！ふんふん！',
    'オイラ、ちゃちゃまるってんだ！\nよろしくな！',
    'こんちゃまる！'
]

CALL = [
    '呼んだかー？'
]

FACE = ':pleading_face:'

CM = [
    'https://www.youtube.com/watch?v=0H4oeZnTLFM',
    'https://www.youtube.com/watch?v=J_DQ4VSdEBc',
    'https://www.youtube.com/watch?v=4qu_Omnyogw',
    'https://www.youtube.com/watch?v=N6LeIcEMo0M',
    'https://www.youtube.com/watch?v=LWmLNFdtQXc',
    'https://www.youtube.com/watch?v=RzBeNGPFdKA',
    'https://www.youtube.com/watch?v=1DtNyFyvlLY'
]

SONG = [
    'https://www.youtube.com/watch?v=ec6__tsfR1M'   
]

HELP_ALL = """
**オイラは、ちゃちゃまるだ！ よろしくな～**
```
- ちゃちゃまる
    オイラが、受け答えするぞー！ふんふん！
- !song
    熱盛の曲を流すぞー！ふんふん！
- !cm
    ちゃっかり宣伝するぞー！ふんふん！
(予定↓)
- !hunhun (on/off)
    ふんふんする気分を変えるぞ！
```
"""

client = discord.Client()
send_channel = None
voice_channel = None


@client.event
async def on_ready():
    send_channel = client.get_channel(712237427460407316)
    voice_channel = client.get_channel(683939861539192865)
    print(f"{client.user} ... 起動！ふんふん！")
    await send_channel.send(f"{client.user.display_name} ... 起動！ふんふん！")
    every.start()

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # チャンネル: ちゃちゃのまる部屋のみ
    # if message.channel.id != send_channel or on_chacha == False:
    #     return

    gets = message.content

    if gets == 'ちゃちゃまる':
        GREETING[0] = f'へー、おまえ{message.author.display_name}っていうのか！\nなんだかおまえとは、仲良くできる気がするぞ！ふんふん！'
        await message.channel.send(random.choice(GREETING))
    elif 'ちゃ' in gets:
        await message.channel.send(random.choice(CALL))

    # All ChaCha's Greeting
    # if gets.startswith('!greet'):
    #     await message.channel.send('\n'.join(GREETING))
    
    if gets.startswith('!face'):
        await message.channel.send(FACE)
        
    if gets.startswith('!song'):
        await message.channel.send('もって来たぞー')
        await message.channel.send(random.choice(SONG))

    if gets.startswith('!cm'):
        await message.channel.send(random.choice(CM))

    if gets.startswith('!chacha'):
        await message.channel.send(HELP_ALL)

@tasks.loop(seconds=10)
async def every():
    await send_channel.send("ふんふん！")



client.run(os.environ['TOKEN'])
