from xander_plugin import *


def onload():
    help_menu_edit("Gmgn plugin", "Saying \"gm\" or \"gn\" makes the bot respond.")
    log("Gm gn plugin loaded!")

async def onmessage(message):
    if message.content.lower() == "gm":
        if config.platform == "guilded":
            await message.channel.send("The " + message.author.name + " has awoken!")
        elif config.platform == "discord":
            await message.channel.send("The " + message.author.mention + " has awoken!")
        return False
    elif message.content.lower() == "gn":
        if config.platform == "guilded":
            await message.channel.send("The " + message.author.name + " has gone into a deep slumber.")
        elif config.platform == "discord":
            await message.channel.send("The " + message.author.mention + " has gone into a deep slumber.")
        return False
    return True


def onexit():
    log("Gm gn plugin exit run.")
