from xander_plugin import *


def onload():
    help_menu_edit("Gmgn plugin", "Saying \"gm\" or \"gn\" makes the bot respond.")
    log("Gm gn plugin loaded!")

async def onmessage(message):
    if message.content.lower() == "gm":
        await message.channel.send("top of the morning to ya " + message.author.mention + "!")
        return False
    elif message.content.lower() == "gn":
        await message.channel.send(message.author.mention + ", well off to bed you cheeky git.")
        return False
    return True


def onexit():
    log("Gm gn plugin exit run.")
