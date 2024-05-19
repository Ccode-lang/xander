import asyncio
import platform
import config
import os
import datetime
import atexit
from traceback import format_exc
import sys

# Put plugins into python path.
os.chdir(os.path.dirname(__file__) or '.')

for folder in [x[0] for x in os.walk(os.getcwd())]:
    sys.path.insert(0, folder)

# Import required bot library.
if config.platform == "discord":
    import discord
elif config.platform == "guilded":
    import guilded as discord
else:
    print("Invalid platform in config.py!")
    sys.exit()

# Manage intents.
if config.platform == "discord":
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
if config.platform == "guilded":
    client = discord.Client()

# Bot status
status = config.defaultact

# Plugin variables
plugins = []
help_menu_default = [("!xhelp", "Shows this help message.")]
help_menu = {}

# Reset help_menu to help_menu_default
def reset_menu():
    global help_menu
    global help_menu_default
    help_menu.clear()
    for tup in help_menu_default:
        help_menu[tup[0]] = tup[1]

# Log a line to the terminal and to log/log.txt
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

# Send a message to modlog and delete the flagged message if specified.
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

# State check for first load
loadplugins = True

# Init plugins and load them into the plugins list
async def pluginsinit():
        global plugins
        global help_menu
        global help_menu_default
        plugins = []
        reset_menu()
        log("Loading plugins")
        for folder in [x[0] for x in os.walk(os.getcwd())]:
            files = os.listdir(folder)
            for filename in files:
                if filename.endswith(".py") and filename.startswith("plugin-"):
                    plugins += [__import__(filename.split(".")[0])]
        for plugin in plugins:
            plugin.onload()
            try:
                await plugin.async_onload()
            except:
                pass

# Load plugins and set the presence when the bot is online.
@client.event
async def on_ready():
    global loadplugins
    log(f'We have logged in as {client.user}')
    if config.platform == "discord":
        await client.change_presence(activity=discord.Game(status))
    if loadplugins:
        await pluginsinit()
        loadplugins = False

# Manage new messages
@client.event
async def on_message(message):
    global plugins
    go = True

    # Ignore messages if they are from the bot.
    if message.author.id == client.user.id:
        return

    # Run priority onmessage functions.
    for plugin in plugins:
        try:
            go = await plugin.onmessage_priority(message)
        except:
            pass
        if not go:
            return

    # Run plugin onmessages.
    for plugin in plugins:
        try:
            if hasattr(plugin, 'onmessage'):
                go = await plugin.onmessage(message)
        except:
            log(f"Caught the following exception:\n{format_exc()}")
        if not go:
            return

    # Reload and help commands
    if message.content == "!reload" and message.author.id in config.admins:
        await message.channel.send("Reloading plugins.")
        log("Reloading plugins.")
        pluginsinit()
    elif message.content == "!xhelp":
        longmsg = ""
        for feature in help_menu:
            longmsg += f"**{feature}**: {help_menu[feature]}\n"
        for i in range(0, len(longmsg), 2000):
            await message.channel.send(longmsg[i:i+2000])
        

# Tell plugins when the bot exits.
def exit_handler():
    log("exit run. Sending exit signal to plugins")
    for plugin in plugins:
        plugin.onexit()

atexit.register(exit_handler)

if platform.system() == 'Windows':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# Run the bot
try:
    client.run(config.token)
except discord.errors.LoginFailure:
    log("Improper token on startup.")

# Initialize plugin API
import xander_plugin
