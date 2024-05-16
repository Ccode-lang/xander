from xander_plugin import *
from discord import app_commands
import xander_utils


def onload():
    help_menu_edit("!hello", "A command that makes the bot say hello.")
    log("Hello plugin loaded!")

async def onmessage(message):
    if message.content.startswith('!hello'):
        await hello(message)
        return False
    return True

def register_slash(tree):
    tree.add_command(app_commands.Command(name="hello", callback=hello, description="Say hello to Xander."))

async def hello(ctx):
    await xander_utils.send_ac(ctx, "Hello!")


def onexit():
    log("Hello plugin exit run.")