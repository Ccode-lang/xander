<img src="https://user-images.githubusercontent.com/78437178/236541048-447c112d-4df4-4427-b617-c66a0322cb28.png"  width="20%" height="20%">  

[Discord server](https://discord.gg/tsn6UtKy)  

# Xander
A discord/guilded bot for moderation and general utility.  Easily extensible with the plugin system that is included.

# How to run
1. Install `better_profanity` and `discord.py` through pip.  (The bot is not tested on Python 2 so make sure you are using 3.8 or up!)
2. Remove any plugins you do not want by deleting them from the plugins folder. (You can also add your own plugins if you know how to write them.  More info in the wiki section of the repository.)
3. Change your `config.py`.  (More info below)
4. Run `bot.py` and watch the magic happen!

# Changing config
To run you have to change the config.py to suit your needs.  The below is a description of each field:  
 - token: The bot login token.  Either guilded or discord tokens will work.
 - defaultact: The status of the bot.
 - dev: The name of the dev channel.  This is used for functions that only mods (who are defined in another field) can use.  (status changing commands will not work in Guilded as bots do not have status updates in Guilded)
 - xanderchannel: Where the bot will send messages that everyone can see.
 - admins: A list of the user ids of the admins who will manage the bot.
 - botping: The ping for the bot.  Set to a random string if you don't want it to ask why people pinged it.
 - platform: the platform the bot is on, "discord" if on discord, "guilded" if on guilded.  

Now that your config is updated you can run the bot with `python bot.py`.  

# Advanced setup
If you want to add more features to the bot you can do so through plugins.  The wiki contains helpful information on how to get started.

Plugins are loaded from the 'plugins' directory and their file must be prefixed with `plugin-` and end with `.py`.  

I have a few plugins made and stored at https://github.com/Ccode-lang/xander-testing if you want to check them out. I'll add more information about them later.  

If you want to remove features you can do so by going to the plugins folder and deleting the corresponding plugin files.

# Contributing
I'm still working on guidelines but you can open a pull request at any time!

# License
I use the MIT license for my projects.  If you want more info look at `LICENSE`.
