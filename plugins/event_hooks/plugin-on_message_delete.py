from traceback import format_exc
from xander_plugin import *

plugins = None

def onload():
    global plugins
    plugins = getother("plugins")
    log("on_message_delete hook plugin loaded!")

@client.event
async def on_message_delete(message):
    global plugins
    go = True

    for plugin in plugins:
        try:
            if hasattr(plugin, 'onmessagedelete'):
                go = await plugin.onmessagedelete(message)
        except:
            log(f"Caught the following exception:\n{format_exc()}")
        if not go:
            return

def onexit():
    log("on_message_delete hook plugin exit run.")