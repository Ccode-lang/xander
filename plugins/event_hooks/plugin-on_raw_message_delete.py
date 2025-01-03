from traceback import format_exc
from xander_plugin import *

plugins = None

def onload():
    global plugins
    plugins = getother("plugins")
    log("on_raw_message_delete hook plugin loaded!")

@client.event
async def on_raw_message_delete(rawmessage):
    global plugins
    go = True

    for plugin in plugins:
        try:
            if hasattr(plugin, 'onrawmessagedelete'):
                go = await plugin.onrawmessagedelete(rawmessage)
        except:
            log(f"Caught the following exception:\n{format_exc()}")
        if not go:
            return

def onexit():
    log("on_raw_message_delete hook plugin exit run.")