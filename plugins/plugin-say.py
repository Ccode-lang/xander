obj = None
log = None
modlog = None
config = None
discord = None


def onload(objin):
    global obj
    global log
    global modlog
    global config
    global discord
    obj = objin
    log = obj["log"]
    modlog = obj["modlog"]
    config = obj["config"]
    discord = obj["discord"]
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