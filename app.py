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

client = discord.Client()

json_open = open('data.json', mode='r', encoding='utf-8')
json_data = json.load(json_open)
json_open.close

@client.event
async def on_ready():
    global send_channel
    # global voice_channel
    send_channel = client.get_channel(712237427460407316)
    # voice_channel = client.get_channel(683939861539192865)

    global greeting
    global call
    global face
    global cm
    global song
    global help_all
    global help_funfun
    global help_funfun_time_set
    global time_call
    greeting = list(json_data['greeting'].values())
    call =     list(json_data['call'].values())
    face =     list(json_data['face'].values())
    cm =       list(json_data['cm'].values())
    song =     list(json_data['song'].values())
    help_all =    "\n".join(list(json_data['help']['all'].values()))
    help_funfun = "\n".join(list(json_data['help']['funfun'].values()))
    help_funfun_time_set = "\n".join(list(json_data['help']['funfun_time_set'].values()))
    time_call = json_data['time_call']
    
    global funfun_done
    funfun_done = True

    print(f"{client.user} ... 起動！ふんふん！")
    await send_channel.send(f"{client.user.display_name} ... 起動！ふんふん！")
    every.start()

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # チャンネル: ちゃちゃのまる部屋のみ
    # if message.channel.id != send_channel:
    #     return

    gets = message.content

    if gets == 'ちゃちゃまる':
        # TO DO
        greeting[0] = f'へー、おまえ{message.author.display_name}っていうのか！\nなんだかおまえとは、仲良くできる気がするぞ！ふんふん！'
        await message.channel.send(random.choice(greeting))
    else: 
        for i in ['ちゃ', 'まる', '筋肉', '筋トレ', 'ひつじ', '羊']:
            if i in gets:
                await message.channel.send(random.choice(call))
                return

    # All ChaCha's Greeting
    # if gets.startswith('!greet'):
    #     await message.channel.send('\n'.join(greeting))
    
    if gets.startswith('!face'):
        await message.channel.send(random.choice(face))
        
    if gets.startswith('!cm'):
        await message.channel.send('もって来たぞー')
        await message.channel.send(random.choice(cm))

    if gets.startswith('!song'):
        await message.channel.send('もって来たぞー')
        await message.channel.send(random.choice(song))

    # show all help
    if gets.startswith('!chacha'):
        await message.channel.send(help_all)

    if re.match(r'^!funfun(\s+)true', gets.lower()):
        funfun_done = True
        await message.channel.send('ふんふん！したい気分だぞ！')
    elif re.match(r'^!funfun(\s+)false', gets.lower()):
        funfun_done = False
        await message.channel.send('今日はふんふん！控えようか...')
    elif gets == '!funfun':
        await message.channel.send(str(funfun_done))
    elif re.match(r'^!funfun(\s)help', gets):
        await message.channel.send(help_funfun)
    elif re.match(r'^!funfun(\s)time_set', gets):
        await message.channel.send(help_funfun_time_set)
    # TO DO
    # add, del, list

@tasks.loop(seconds=60)
async def every():
    time = datetime.datetime.now().time()
    if funfun_done and time.minute == 0:
        print('time call')
        # 6 - 8 getup
        if time.hour in range(6, 8):
            await send_channel.send(time_call['getup']['kintore'])
            print('do getup motion')
        # 9 - 12 mornig
        elif time.hour in range(9, 12):
            await send_channel.send(time_call['morning']['default']) # TO DO
            print('do morning motion')
        # 13 - 16 afternoon
        elif time.hour in range(13, 16):
            await send_channel.send(time_call['afternoon']['bee'])
            print('do afternoon motion')
        # 17 - 19 evening
        elif time.hour in range(17, 19):
            await send_channel.send(time_call['evening']['default']) # TO DO
            print('do evening motion')
        # 20 - 22 night
        elif time.hour in range(20, 22):
            await send_channel.send(time_call['night']['default']) # TO DO
            print('do night motion')
        # 23 - 5 sleep
        elif time.hour in range(0, 5) or time.hour == 23:
            await send_channel.send(time_call['sleep']['sleep'])
            print('do sleep motion')



client.run(os.environ['TOKEN'])
