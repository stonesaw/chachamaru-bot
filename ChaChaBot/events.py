# developing ...

import discord
import random
import re
import time
import datetime
import json

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

class ChaChaEvents:
    def __init__(self, send_channel, voice_channel):
        self.send_channel = send_channel
        self.voice_channel = voice_channel

    async def events(self, message:discord.Message):
        if message.author.bot:
            return

        # チャンネル: ちゃちゃ丸の部屋
        # if message.channel.id != send_channel or on_chacha == False:
        #     return

        gets = message.content

        if gets == 'ちゃちゃまる':
            GREETING[0] = f'へー、おまえ{message.author.display_name}っていうのか！\nなんだかおまえとは、仲良くできる気がするぞ！ふんふん！'
            await message.channel.send(random.choice(GREETING))
        elif 'ちゃちゃ' in gets:
            await message.channel.send(random.choice(CALL))

        # if gets.startswith('!chacha'):
        #     await message.channel.send('\n'.join(GREETING))

        if gets.startswith('!face'):
            await message.channel.send(FACE)

        if gets.startswith('!song'):
            await message.channel.send(random.choice(SONG))

        if gets.startswith('!cm'):
            await message.channel.send(random.choice(CM))

        if gets.startswith('!help'):
            await message.channel.send(HELP_ALL)

    def loops(self):
        print("be update")
        now = datetime.datetime.now()
        if funfun_done and now.minute == 0:
            await self.send_channel.send(f'{now.hour}時だぞ！ ふんふん！')
            print("do ふんふん！")