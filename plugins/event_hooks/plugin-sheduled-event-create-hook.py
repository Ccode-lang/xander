from traceback import format_exc
from xander_plugin import *

plugins = None

def onload():
    global plugins
    plugins = getother("plugins")
    log("on_scheduled_event_create hook plugin loaded!")

@client.event
async def on_scheduled_event_create(event):
    global plugins
    go = True

    for plugin in plugins:
        try:
            if hasattr(plugin, 'onscheduledeventcreate'):
                go = await plugin.onscheduledeventcreate(event)
        except:
            log(f"Caught the following exception:\n{format_exc()}")
        if not go:
            return




def onexit():
    log("on_scheduled_event_create hook plugin exit run.")