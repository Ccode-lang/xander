from xander_plugin import *

def onload():
    help_menu_edit("!status", "A command that changes the status of the bot. (Needs bot admin)")
    log("Status plugin loaded!")

async def onmessage(message):
    if message.content.startswith("!status ") and message.channel.name == config.dev and message.author.id in config.admins and config.platform == "discord":
        play = message.content[8:]
        global status
        status = play
        await client.change_presence(activity=discord.Game(play))
        return False
    return True


def onexit():
    log("Status plugin exit run.")