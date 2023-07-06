import sys
import config

if config.platform == "discord":
    import discord
elif config.platform == "guilded":
    import guilded as discord
else:
    print("Invalid platform in config.py!")
    sys.exit()


from better_profanity import profanity
import config
import random
import os
import datetime
import atexit

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

access = {
    "discord": discord,
    "log": log,
    "modlog": modlog,
    "config": config
}
loadplugins = True


@client.event
async def on_ready():
    log(f'We have logged in as {client.user}')
    if config.platform == "discord":
        await client.change_presence(activity=discord.Game(status))
    global loadplugins
    if loadplugins:
        log("Loading plugins")
        files = os.listdir()
        global plugins
        for filename in files:
            if filename.endswith(".py") and filename.startswith("plugin-"):
                plugins += [__import__(filename.split(".")[0])]
        for plugin in plugins:
            plugin.onload(access)
        loadplugins = False


@client.event
async def on_message(message):
    global plugins

    go = True
    if message.author.id == client.user.id:
        return
    # print(message.author.id)
    for plugin in plugins:
        go = await plugin.onmessage(message)
        if not go:
            return 0

    if config.botping in message.content:
        num = random.randint(1, 10)
        if num == 10:
            await message.channel.send("Why have you pinged me?")

    check = "".join(ch for ch in message.content if ch.isalnum())

    if profanity.contains_profanity(check) or profanity.contains_profanity(message.content):
        log(message.author.name + ' said: "' + message.content +
            '" on server "' + str(message.guild) + '"')
        await modlog(message.author.name + ' said: "' + message.content + '" on server "' + message.guild.name + '"', message, True)
    elif message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith("!echo "):
        log(message.author.name + ' echoed: "' +
            message.content[6:] + '" on server "' + message.guild.name + '"')
        await modlog(message.author.name + ' echoed: "' + message.content[6:] + '" on server "' + message.guild.name + '"', message)
        await message.channel.send(message.content[6:])
    elif message.content.startswith("!servers"):
        await message.channel.send(str(len(client.guilds)))
    elif message.content.startswith("!say ") and message.channel.name == config.dev:
        say = message.content[5:]
        channel = discord.utils.get(
            message.guild.text_channels, name=config.xanderchannel)
        if not channel == None:
            await channel.send(say)
    elif message.content.startswith("!status ") and message.channel.name == config.dev and message.author.id in config.admins and config.platform == "discord":
        play = message.content[8:]
        global status
        status = play
        await client.change_presence(activity=discord.Game(play))
    elif message.content.lower() == "gm":
        if config.platform == "guilded":
            await message.channel.send("The " + message.author.name + " has awoken!")
        elif config.platform == "discord":
            await message.channel.send("The " + message.author.mention + " has awoken!")
    elif message.content.lower() == "gn":
        if config.platform == "guilded":
            await message.channel.send("The " + message.author.name + " has gone into a deep slumber.")
        elif config.platform == "discord":
            await message.channel.send("The " + message.author.mention + " has gone into a deep slumber.")
    elif message.content == "!reload" and message.author.id in config.admins:
        await message.channel.send("Reloading plugins.")
        log("Reloading plugins.")
        plugins = []
        files = os.listdir()
        for filename in files:
            if filename.endswith(".py") and filename.startswith("plugin-"):
                plugins += [__import__(filename.split(".")[0])]
        for plugin in plugins:
            plugin.onload(access)


def exit_handler():
    print("exit run. Sending exit signal to plugins")
    for plugin in plugins:
        plugin.onexit()


atexit.register(exit_handler)

try:
    client.run(config.token)
except discord.errors.LoginFailure:
    log("Improper token on startup.")
