from xander_plugin import *

def onload():
    help_menu_edit("!servers", "A command that prints the number of servers the bot is in.")
    log("Servers plugin loaded!")

async def onmessage(message):
    if message.content.startswith("!servers"):
        await message.channel.send(str(len(client.guilds)))
        return False
    return True


def onexit():
    log("Servers plugin exit run.")