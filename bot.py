import discord
from better_profanity import profanity
import config


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



@client.event
async def on_message(message):
    if profanity.contains_profanity(message.content):
        print(message.author, ' said: "', message.content, '" on server "', message.guild, '"')
        channel = discord.utils.get(message.guild.text_channels, name = "modlog")
        if not channel == None:
            await channel.send(message.author.name + ' said: "' + message.content + '" on server "' + message.guild.name + '"')
        await message.delete()
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith("!echo "):
        await message.channel.send(message.content[6:])

    if message.content.startswith("!say ") and message.channel.name == "dev":
        say = message.content[5:]
        channel = discord.utils.get(message.guild.text_channels, name = "general")
        if not channel == None:
            await channel.send(say)

client.run(config.token)
