from profanity_check import predict, predict_prob
from xander_plugin import *
def onload():
    help_menu_edit("Profanity check plugin", "A plugin that filters profanity.")
    log("Profanity plugin loaded!")

async def onmessage_priority(message):
    if predict(message.content):
        log(message.author.name + ' said: "' + message.content +
            '" on server "' + str(message.guild) + '"')
        await modlog(message.author.name + ' said: "' + message.content + '" on server "' + message.guild.name + '"', message, True)
        return False
    return True

async def onmessage(message):
    return True


def onexit():
    log("Profanity plugin exit run.")