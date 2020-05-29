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
bot = commands.Bot(command_prefix='!')

json_open = open('lib/data.json', mode='r', encoding='utf-8')
json_data = json.load(json_open)
json_open.close

global js
js = {
    "greeting":       list(json_data['greeting'].values()),
    "call":           list(json_data['call'].values()),
    "call_keywords":  list(json_data['call_keywords'].values()),
    "grass_keywords": list(json_data['grass_keywords'].values()),
    "kabu_keywords": list(json_data['kabu_keywords'].values()),
    "face":           list(json_data['face'].values()),
    "cm":             list(json_data['cm'].values()),
    "song":           list(json_data['song'].values()),
    "help_all":             "\n".join(list(json_data['help']['all'].values())),
    "help_funfun":          "\n".join(list(json_data['help']['funfun'].values())),
    "help_funfun_time_set": "\n".join(list(json_data['help']['funfun_time_set'].values()))
}

global time_call
time_call = json_data['time_call']


@client.event
async def on_ready():
    global send_channel
    # global voice_channel
    send_channel = client.get_channel(712237427460407316)
    global genkai_channel
    genkai_channel = client.get_channel(690909527461199922)
    # voice_channel = client.get_channel(683939861539192865)
    
    global funfun_done
    funfun_done = True

    print(f"{client.user} ... 起動！ふんふん！")
    await send_channel.send(f"{client.user.display_name} ... 起動！ふんふん！")
    every.start()

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # チャンネル: ちゃちゃのまる部屋・無法地帯のみ
    if message.channel != send_channel and message.channel != genkai_channel:
        return

    gets = message.content

    if gets == 'ちゃちゃまる':
        # TO DO
        js['greeting'][0] = f'へー、おまえ{message.author.display_name}っていうのか！\nなんだかおまえとは、仲良くできる気がするぞ！ふんふん！'
        await message.channel.send(random.choice(js['greeting']))
    else:
        for i in js['call_keywords']:
            if i in gets:
                await message.channel.send(random.choice(js['call']))
                return

    # 草
    for i in js['grass_keywords']:
        if i in gets:
            await message.channel.send(file=discord.File('lib/grass.png'))
            return

    if re.match(r'^(w|ｗ)+$', gets.lower()):
        await message.channel.send(file=discord.File('lib/grass.png'))

    # カブ
    for i in js['kabu_keywords']:
        if i in gets:
            file = random.choice(['lib/kabu.png', 'lib/kusatta-kabu.png'])
            await message.channel.send(file=discord.File(file))
    
    # All ChaCha's Greeting
    # if gets.startswith('!greet'):
    #     await message.channel.send('\n'.join(js['greeting']))

    if gets.startswith('!face'):
        await message.channel.send(random.choice(js['face']))
        
    if gets.startswith('!cm'):
        await message.channel.send('もって来たぞー')
        await message.channel.send(random.choice(js['cm']))

    if gets.startswith('!song'):
        await message.channel.send('もって来たぞー')
        await message.channel.send(random.choice(js['song']))

    # show all help
    if gets.startswith('!chacha'):
        await message.channel.send(js['help_all'])

    if re.match(r'^!funfun(\s+)true', gets.lower()):
        funfun_done = True
        await message.channel.send('ふんふん！したい気分だぞ！')
    elif re.match(r'^!funfun(\s+)false', gets.lower()):
        funfun_done = False
        await message.channel.send('今日はふんふん！控えようか...')
    elif gets == '!funfun':
        await message.channel.send(str(funfun_done))
    elif re.match(r'^!funfun(\s+)help', gets):
        await message.channel.send(js['help_funfun'])
    elif re.match(r'^!funfun(\s+)time_set', gets):
        await message.channel.send(js['help_funfun_time_set'])
    
# TO DO
# add, del, list

# @bot.command()
# async def funfun(ctx, arg):
#     print('funfun')
#     await ctx.send('funfun add!')

# @bot.command()
# async def add(ctx, a: int, b: int):
#     await ctx.send(a + b)

@tasks.loop(seconds=60)
async def every():
    time = datetime.datetime.now().time()
    if funfun_done and time.minute == 0:
        print('time called')
        
        # 6 - 8 getup
        if time.hour in range(6, 8):
            await send_channel.send(time_call['getup']['default'])
            print('do getup motion')
        # 9 - 12 mornig
        elif time.hour in range(9, 12):
            await send_channel.send(time_call['morning']['default'])
            print('do morning motion')
        # 13 - 16 afternoon
        elif time.hour in range(13, 16):
            await send_channel.send(time_call['afternoon']['defaule'])
            print('do afternoon motion')
        # 17 - 19 evening
        elif time.hour in range(17, 19):
            await send_channel.send(time_call['evening']['default'])
            print('do evening motion')
        # 20 - 22 night
        elif time.hour in range(20, 22):
            await send_channel.send(time_call['night']['default'])
            print('do night motion')
        # 23 - 5 sleep
        elif time.hour in range(0, 5) or time.hour == 23:
            await send_channel.send(time_call['sleep']['default'])
            print('do sleep motion')


client.run(os.environ['TOKEN'])
