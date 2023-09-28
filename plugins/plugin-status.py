obj = None
log = None
modlog = None
config = None
client = None
discord = None

def onload(objin):
    global obj
    global log
    global modlog
    global config
    global client
    global discord
    obj = objin
    log = obj["log"]
    modlog = obj["modlog"]
    config = obj["config"]
    client = obj["client"]
    discord = obj["discord"]
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