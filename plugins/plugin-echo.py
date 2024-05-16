from xander_plugin import *
from discord import app_commands
import xander_utils
import traceback


def onload():
    help_menu_edit("!echo", "A command that echos your input.")
    log("Echo plugin loaded!")

async def onmessage(message):
    if message.content.startswith("!echo "):
        await echo(message, message.content[6:])
        return False
    return True

async def echo(ctx, message: str):
    log(xander_utils.get_author(ctx).name + ' echoed: "' +
    message + '" on server "' + ctx.guild.name + '"')
    await modlog(xander_utils.get_author(ctx).name + ' echoed: "' + message + '" on server "' + ctx.guild.name + '"', ctx)
    await xander_utils.send_ac(ctx, message)

def register_slash(tree):
    try:
        tree.add_command(app_commands.Command(name="echo", callback=echo, description="Echo message."))
    except:
        traceback.print_exc()

def onexit():
    log("Echo plugin exit run.")