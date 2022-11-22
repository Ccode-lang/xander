import discord
from better_profanity import profanity
import config


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(' around with you guys.'))



@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if profanity.contains_profanity(message.content):
        print(message.author, ' said: "', message.content, '" on server "', message.guild, '"')
        channel = discord.utils.get(message.guild.text_channels, name = "modlog")
        if not channel == None:
            await channel.send(message.author.name + ' said: "' + message.content + '" on server "' + message.guild.name + '"')
        try:
            await message.delete()
        except:
            print("Invalid perms")
    elif message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith("!echo "):
        print(message.author.name + ' echoed: "' + message.content[6:] + '" on server "' + message.guild.name + '"')
        await message.channel.send(message.content[6:])
    elif message.content.startswith("!servers"):
        await message.channel.send(str(len(client.guilds)))
    elif message.content.startswith("!say ") and message.channel.name == "dev":
        say = message.content[5:]
        channel = discord.utils.get(message.guild.text_channels, name = "general")
        if not channel == None:
            await channel.send(say)

client.run(config.token)
