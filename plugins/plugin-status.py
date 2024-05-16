from xander_plugin import *
import xander_utils
import traceback
from discord import app_commands

def onload():
    help_menu_edit("!status", "A command that changes the status of the bot. (Needs bot admin)")
    log("Status plugin loaded!")

async def onmessage(message):
    if message.content.startswith("!status ") and message.channel.name == config.dev and message.author.id in config.admins and config.platform == "discord":
        await statusc(message, message.content[8:])
        return False
    return True


async def statusc(ctx, statusm: str):
    if ctx.channel.name == config.dev and xander_utils.get_author(ctx).id in config.admins and config.platform == "discord":
        play = statusm
        global status
        status = play
        await client.change_presence(activity=discord.Game(play))
    await xander_utils.pong(ctx)
    

def register_slash(tree):
    try:
        tree.add_command(app_commands.Command(name="status", callback=statusc, description="Change bot status. (Only works for bot admins)"))
    except:
        traceback.print_exc()

def onexit():
    log("Status plugin exit run.")