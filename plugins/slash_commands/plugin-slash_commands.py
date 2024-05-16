from xander_plugin import *
from discord import app_commands
from discord import utils
import traceback

def onload():
    log("Slash command plugin loaded!")
    
async def async_onload():
    plugins = getother("plugins")
    tree = app_commands.CommandTree(client)
    for plugin in plugins:
        try:
            plugin.register_slash(tree)
            log(f"Registered {plugin.__name__} slash commands.")
        except:
            pass
    try:
        try:
            tree.copy_global_to(guild=client.get_guild(config.priority_server))
            await tree.sync(guild=client.get_guild(config.priority_server))
        except:
            pass
        await tree.sync()
        log("Done with command sync.")
    except:
        traceback.print_exc()


def onexit():
    log("Slash command plugin exit run.")