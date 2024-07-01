from xander_plugin import *

def onload():
    help_menu_edit("Delete log plugin", "A plugin that logs everything that gets deleted.")
    log("Delete log plugin loaded!")

async def onrawmessagedelete(rawmessage):
    if not rawmessage.cached_message is None and not rawmessage.cached_message.author.id == client.user.id:
        await modlog(f"{rawmessage.cached_message.author.display_name} deleted their message: \"{rawmessage.cached_message.content}\"", rawmessage.cached_message)


def onexit():
    log("Delete log plugin exit run.")
