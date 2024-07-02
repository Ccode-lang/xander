from xander_plugin import *

def onload():
    help_menu_edit("Delete log plugin", "A plugin that logs everything that gets deleted.")
    log("Delete log plugin loaded!")

async def onmessagedelete(message):
    if not message.author.id == client.user.id:
        await modlog(f"message written by {message.author.display_name} was deleted: \"{message.content}\"", message)
    return True


def onexit():
    log("Delete log plugin exit run.")
