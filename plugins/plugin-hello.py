obj = None
log = None
modlog = None


def onload(objin):
    global obj
    global log
    global modlog
    obj = objin
    log = obj["log"]
    modlog = obj["modlog"]
    log("Hello plugin loaded!")

async def onmessage(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    return True


def onexit():
    log("Hello plugin exit run.")