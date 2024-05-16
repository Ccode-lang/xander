from xander_plugin import *
import traceback
from discord import app_commands
import xander_utils

def onload():
    help_menu_edit("!say", "A command that echos your input into another channel. (Needs bot admin)")
    log("Say plugin loaded!")

async def onmessage(message):
    if message.content.startswith("!say ") and message.channel.name == config.dev:
        await say(message, message.content[5:])
        return False
    return True

async def say(ctx, message: str):
    if ctx.channel.name == config.dev:
        say = message
        channel = discord.utils.get(
            ctx.guild.text_channels, name=config.xanderchannel)
        if not channel == None:
            await channel.send(say)
    await xander_utils.pong(ctx)

def register_slash(tree):
    try:
        tree.add_command(app_commands.Command(name="say", callback=say, description="A command that echos your input into another channel. (Needs bot admin)"))
    except:
        traceback.print_exc()

def onexit():
    log("Say plugin exit run.")