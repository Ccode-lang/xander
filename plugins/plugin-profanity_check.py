from better_profanity import profanity


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
    log("Profanity plugin loaded!")

async def onmessage_priority(message):
    check = "".join(ch for ch in message.content if ch.isalnum())

    if profanity.contains_profanity(check) or profanity.contains_profanity(message.content):
        log(message.author.name + ' said: "' + message.content +
            '" on server "' + str(message.guild) + '"')
        await modlog(message.author.name + ' said: "' + message.content + '" on server "' + message.guild.name + '"', message, True)

        return False
    return True


def onexit():
    log("Profanity plugin exit run.")