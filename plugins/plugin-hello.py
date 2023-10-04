from xander_plugin import *


def onload():
    help_menu_edit("!hello", "A command that makes the bot say hello.")
    log("Hello plugin loaded!")

async def onmessage(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    return True


def onexit():
    log("Hello plugin exit run.")