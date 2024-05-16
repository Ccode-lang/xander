#send message no matter the context
async def send_ac(ctx, message):
    try:
        await ctx.response.send_message(message)
    except:
        await ctx.channel.send(message)

async def pong(ctx):
    try:
        await ctx.response.send_message("Command Run", ephemeral=True)
    except:
        pass

def get_author(ctx):
    try:
        return ctx.author
    except:
        return ctx.user