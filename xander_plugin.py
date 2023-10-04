import __main__

config = __main__.config
log = __main__.log
discord = __main__.discord
modlog = __main__.modlog
client = __main__.client
help_menu = __main__.help_menu

def getother(name):
    return getattr(__main__, name)

def help_menu_edit(feature_name, info):
    help_menu[feature_name] = info
