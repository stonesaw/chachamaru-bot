# developing ...

import os
from dotenv import load_dotenv

import discord
from discord.ext import tasks, commands

from events import ChaChaEvents

load_dotenv(verbose=True)

class Client(discord.Client):
    def __init__(self):
        super().__init__()

    def run(self):
        super().run(os.environ['TOKEN'])

    async def on_ready(self):
        self.send_channel = self.get_channel(711149516572721173)
        self.voice_channel = self.get_channel(710821816922275872)

        print(f"{self.user.display_name} ... 起動！ふんふん！")
        await self.send_channel.send(f"{self.user.display_name} ... 起動！ふんふん！")
        # self.min_loop.start()

    async def on_message(self, message):
        await ChaChaEvents.receive(message)

    @tasks.loop(seconds=60)
    async def min_loop(self):
        await ChaChaEvents.loops()

        


print("--- ふんふん! ---\n")
