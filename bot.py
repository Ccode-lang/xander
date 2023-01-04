import discord
from better_profanity import profanity
import config
import random
import os
import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

status = config.defaultact

@client.event
async def on_ready():
    log(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(status))

def log(line):
    t = datetime.datetime.now()
    t = t.strftime("%d/%m/%Y %H:%M:%S")
    line = "[" + t + "] " + line
    print(line)
    file = open(os.path.join("log", "log.txt"), "a")
    file.write(line + os.linesep)
    file.close()

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    #print(message.author.id)
    
    if config.botping in message.content:
        num = random.randint(1, 10)
        if num == 10:
            await message.channel.send("Why have you pinged me?")

    check = "".join(ch for ch in message.content if ch.isalnum())

    if profanity.contains_profanity(check) or profanity.contains_profanity(message.content):
        log(message.author.name + ' said: "' + message.content + '" on server "' + str(message.guild) + '"')
        channel = discord.utils.get(message.guild.text_channels, name = config.modlog)
        if not channel == None:
            await channel.send(message.author.name + ' said: "' + message.content + '" on server "' + message.guild.name + '"')
        try:
            await message.delete()
        except:
            log("Invalid perms")
    elif message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith("!echo "):
        log(message.author.name + ' echoed: "' + message.content[6:] + '" on server "' + message.guild.name + '"')
        await message.channel.send(message.content[6:])
    elif message.content.startswith("!servers"):
        await message.channel.send(str(len(client.guilds)))
    elif message.content.startswith("!say ") and message.channel.name == config.dev:
        say = message.content[5:] 
        channel = discord.utils.get(message.guild.text_channels, name = config.xanderchannel)
        if not channel == None:
            await channel.send(say)
    elif message.content.startswith("!status ") and message.channel.name == config.dev and message.author.id in config.admins:
        play = message.content[8:]
        global status
        status = play
        await client.change_presence(activity=discord.Game(play))
    elif message.content.lower() == "gm":
        await message.channel.send("The " + message.author.mention + " has awoken!")
    elif message.content.lower() == "gn":
        await message.channel.send("The " + message.author.mention + " has gone into a deep slumber.")

client.run(config.token)
