from xander_plugin import *


def onload():
    log("Say plugin loaded!")

async def onmessage(message):
    if message.content.startswith("!say ") and message.channel.name == config.dev:
        say = message.content[5:]
        channel = discord.utils.get(
            message.guild.text_channels, name=config.xanderchannel)
        if not channel == None:
            await channel.send(say)
        return False
    return True


def onexit():
    log("Say plugin exit run.")