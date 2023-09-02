<img src="https://user-images.githubusercontent.com/78437178/236541048-447c112d-4df4-4427-b617-c66a0322cb28.png"  width="20%" height="20%">  

# Xander
A discord/guilded bot for moderation and general utility.  Easily extensible with the plugin system that is included.

# How to run
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
If you want to add more features to the bot you can do so through plugins.  The wiki contains helpful information on how to get started.  (plugins are still WIP and may have drastic changes at any point in development!)

Plugins are loaded from the directory that contains `bot.py` and their file must be prefixed with `plugin-` and end with `.py`.

# Contributing
I'm still working on guidelines but you can open a pull request at any time!

# License
I use the MIT license for my projects.  If you want more info look at `LICENSE`.

# Other contact.
If you want to come and hang out or ask questions about xander this is an IRC server I host: `hangoutirc.mooo.com/6697`  If I'm not on my bot `hangoutbot` will log your questions and I'll be able to answer them when I get online.
