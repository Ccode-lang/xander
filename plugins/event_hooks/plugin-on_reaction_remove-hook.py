from traceback import format_exc
from xander_plugin import *

plugins = None

def onload():
    global plugins
    plugins = getother("plugins")
    log("on_reaction_remove hook plugin loaded!")

@client.event
async def on_reaction_remove(reaction, user):
    global plugins
    go = True

    for plugin in plugins:
        try:
            if hasattr(plugin, 'onreactionremove'):
                go = await plugin.onreactionremove(reaction, user)
        except:
            log(f"Caught the following exception:\n{format_exc()}")
        if not go:
            return




def onexit():
    log("on_reaction_remove hook plugin exit run.")