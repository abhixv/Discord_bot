import discord
from discord.ext import commands,tasks
import random
from itertools import cycle

client = commands.Bot(command_prefix='/')
status = cycle(['status 1','status 2'])

@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.idle,activity=discord.Game("Hello there!"))

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_member_join(ctx,member):
    await ctx.send(f"Welcome {member} to this server\n Rules : \n 1.Do not use offensive Language \n 2.Respect everyone Or Get a Ban\n")
@client.event
async def on_member_remove(ctx,member):
    await ctx.send(f"{member} has lefted the server")
@client.command()
async def ping(ctx):
    await ctx.send(f"pong! {client.latency*1000}ms")

@client.command()
async def mihir(ctx):
    await ctx.send(f"Obviously badwa!!!")

@client.command()
async def Rules(ctx):
    await ctx.send(f"Rules : \n 1.Do not use offensive Language \n 2.Respect everyone Or Get a Ban")

@client.command()
async def clear(ctx,amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def link(ctx,amount=10):
    await ctx.send(f"")


@client.command()
async def kick(ctx,member : discord.Member,*,reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx,member : discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention} from the server")

@client.command()
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name ,member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user  = ban_entry.user
        if(user.name,user.discriminator)==(member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


@client.command(aliases=['bot','test'])
async def good(ctx,*,question):
    responses = ['Dyanyawad','Sukriya','Thanks']
    await ctx.send(f"Question : {question}\n Answer: {random.choice(responses)}")



        
client.run('<UR CLIENT ID>')

