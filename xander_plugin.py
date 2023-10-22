import __main__

# bot.py keywords
config = __main__.config
log = __main__.log
discord = __main__.discord
modlog = __main__.modlog
client = __main__.client
help_menu = __main__.help_menu

# Library state variables
voice_client = None


# Plugin utility methods
def getother(name):
    return getattr(__main__, name)

def help_menu_edit(feature_name, info):
    help_menu[feature_name] = info

async def join_vc(channel):
    global voice_client
    if voice_client == None and not config.platform == "guilded":
        voice_client = await channel.connect()

async def leave_vc():
    global voice_client
    if not voice_client == None and not config.platform == "guilded":
        await voice_client.disconnect()
        voice_client = None
