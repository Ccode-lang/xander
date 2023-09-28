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
    log("Echo plugin loaded!")

async def onmessage_priority(message):
    if message.content.startswith("!echo "):
        log(message.author.name + ' echoed: "' +
            message.content[6:] + '" on server "' + message.guild.name + '"')
        await modlog(message.author.name + ' echoed: "' + message.content[6:] + '" on server "' + message.guild.name + '"', message)
        await message.channel.send(message.content[6:])
        return False
    return True


def onexit():
    log("Echo plugin exit run.")