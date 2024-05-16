from traceback import format_exc
from xander_plugin import *

plugins = None

def onload():
    global plugins
    plugins = getother("plugins")
    log("on_reaction_add hook plugin loaded!")

@client.event
async def on_reaction_add(reaction, user):
    global plugins
    go = True

    for plugin in plugins:
        try:
            if hasattr(plugin, 'onreactionadd'):
                go = await plugin.onreactionadd(reaction, user)
        except:
            log(f"Caught the following exception:\n{format_exc()}")
        if not go:
            return




def onexit():
    log("on_reaction_add hook plugin exit run.")