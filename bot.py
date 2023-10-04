import config
import os
import datetime
import atexit
from traceback import format_exc
import sys

os.chdir(os.path.dirname(__file__) or '.')
sys.path.insert(0, os.path.join(os.getcwd(), "plugins"))


if config.platform == "discord":
    import discord
elif config.platform == "guilded":
    import guilded as discord
else:
    print("Invalid platform in config.py!")
    sys.exit()

if config.platform == "discord":
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
if config.platform == "guilded":
    client = discord.Client()

status = config.defaultact

plugins = []


def log(line):
    t = datetime.datetime.now()
    t = t.strftime("%d/%m/%Y %H:%M:%S")
    line = "[" + t + "] " + line
    print(line)
    if not os.path.exists(os.path.join("log", "log.txt")):
        os.mkdir("log")
    file = open(os.path.join("log", "log.txt"), "a")
    file.write(line + os.linesep)
    file.close()


async def modlog(string, message, delete=False):
    channel = discord.utils.get(
        message.guild.text_channels, name=config.modlog)
    if not channel == None:
        await channel.send(string)
    try:
        if delete:
            await message.delete()
    except:
        log(
            f"Invalid perms to access modlog channel in server {message.guild.name}")

loadplugins = True

def pluginsinit():
        global plugins
        plugins = []
        log("Loading plugins")
        files = os.listdir("plugins")
        for filename in files:
            if filename.endswith(".py") and filename.startswith("plugin-"):
                plugins += [__import__(filename.split(".")[0])]
        for plugin in plugins:
            plugin.onload()


@client.event
async def on_ready():
    global loadplugins
    log(f'We have logged in as {client.user}')
    if config.platform == "discord":
        await client.change_presence(activity=discord.Game(status))
    if loadplugins:
        pluginsinit()
        loadplugins = False


@client.event
async def on_message(message):
    global plugins
    runothers = True
    go = True
    if message.author.id == client.user.id:
        return

    for plugin in plugins:
        try:
            go = await plugin.onmessage_priority(message)
        except:
            go = True
        if not go:
            runothers = False
            return 0

    if runothers == True:
        for plugin in plugins:
            try:
                go = await plugin.onmessage(message)
            except:
                log(f"Caught the following exception:\n{format_exc()}")
                go = True
            if not go:
                return 0

    if message.content == "!reload" and message.author.id in config.admins:
        await message.channel.send("Reloading plugins.")
        log("Reloading plugins.")
        pluginsinit()


def exit_handler():
    log("exit run. Sending exit signal to plugins")
    for plugin in plugins:
        plugin.onexit()


atexit.register(exit_handler)

try:
    client.run(config.token)
except discord.errors.LoginFailure:
    log("Improper token on startup.")

import xander_plugin