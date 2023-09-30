import sys
import config

if config.platform == "discord":
    import discord
elif config.platform == "guilded":
    import guilded as discord
else:
    print("Invalid platform in config.py!")
    sys.exit()


import config
import os
import datetime
import atexit
from traceback import print_exc

if config.platform == "discord":
    intents = discord.Intents.all()
    # intents.message_content = True

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


@client.event
async def on_ready():
    log(f'We have logged in as {client.user}')
    if config.platform == "discord":
        await client.change_presence(activity=discord.Game(status))
    global loadplugins
    if loadplugins:
        log("Loading plugins")
        sys.path.insert(0, os.path.join(os.getcwd(), "plugins"))
        files = os.listdir("plugins")
        global plugins
        for filename in files:
            if filename.endswith(".py") and filename.startswith("plugin-"):
                plugins += [__import__(filename.split(".")[0])]
        for plugin in plugins:
            plugin.onload()
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
                print("Caught the following exception:")
                print_exc()
                go = True
            if not go:
                return 0

    if message.content == "!reload" and message.author.id in config.admins:
        await message.channel.send("Reloading plugins.")
        log("Reloading plugins.")
        plugins = []
        files = os.listdir()
        for filename in files:
            if filename.endswith(".py") and filename.startswith("plugin-"):
                plugins += [__import__(filename.split(".")[0])]
        for plugin in plugins:
            plugin.onload()


def exit_handler():
    print("exit run. Sending exit signal to plugins")
    for plugin in plugins:
        plugin.onexit()


atexit.register(exit_handler)

try:
    client.run(config.token)
except discord.errors.LoginFailure:
    log("Improper token on startup.")
import xander_plugin