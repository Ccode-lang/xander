import __main__

config = __main__.config
log = __main__.log
discord = __main__.discord
modlog = __main__.modlog
client = __main__.client

def getother(name):
    return getattr(__main__, name)