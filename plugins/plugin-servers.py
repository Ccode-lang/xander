obj = None
log = None
modlog = None
client = None

def onload(objin):
    global obj
    global log
    global modlog
    global client
    obj = objin
    log = obj["log"]
    modlog = obj["modlog"]
    client = obj["client"]
    log("Servers plugin loaded!")

async def onmessage(message):
    if message.content.startswith("!servers"):
        await message.channel.send(str(len(client.guilds)))
        return False
    return True


def onexit():
    log("Servers plugin exit run.")