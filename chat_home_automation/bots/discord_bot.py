import logging
import os

import discord
from discord.ext import commands

from chat_home_automation.bots.base import AbstractBot
from chat_home_automation.commands import Commands

logger = logging.getLogger(__name__)


class DiscordBot(AbstractBot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        self._commands = Commands()

    def run(self):
        @self.bot.event
        async def on_ready():
            logging.info("Logged in as {0.user}".format(self.bot))

        @self.bot.event
        async def on_message(message):
            if message.author == self.bot.user:
                return

            if message.content.startswith("!"):
                status, msg = self._commands.execute_command(message.content[1:])
                if status:
                    await message.channel.send(f"Command executed: {msg}")
                else:
                    await message.channel.send(f"Command failed: {msg}")

        self.bot.run(os.environ.get("DISCORD_TOKEN"))
