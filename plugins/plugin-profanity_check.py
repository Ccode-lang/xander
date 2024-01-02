from profanity_check import predict, predict_prob
from xander_plugin import *
def onload():
    help_menu_edit("Profanity check plugin", "A plugin that filters profanity.")
    log("Profanity plugin loaded!")

async def onmessage_priority(message):
    if predict([message.content]) == [1]:
        log(message.author.name + ' said: "' + message.content +
            '" on server "' + str(message.guild) + '" (Probability: ' + str(predict_prob([message.content])[0]) + ' )')
        await modlog(message.author.name + ' said: "' + message.content + '" on server "' + message.guild.name + '" (Probability: ' + str(predict_prob([message.content])[0]) + ' )', message, True)
        return False
    return True

async def onmessage(message):
    return True


def onexit():
    log("Profanity plugin exit run.")