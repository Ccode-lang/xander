from xander_plugin import *
import traceback
from discord import app_commands
import xander_utils

def onload():
    help_menu_edit("!servers", "A command that prints the number of servers the bot is in.")
    log("Servers plugin loaded!")

async def onmessage(message):
    if message.content.startswith("!servers"):
        await servers(message)
        return False
    return True

async def servers(ctx):
    await xander_utils.send_ac(ctx, (str(len(client.guilds))))

def register_slash(tree):
    try:
        tree.add_command(app_commands.Command(name="servers", callback=servers, description="A command that prints the number of servers the bot is in."))
    except:
        traceback.print_exc()

def onexit():
    log("Servers plugin exit run.")