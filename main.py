import os
import discord
import datetime
from datetime import date
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix=';')

async def is_owner(ctx):
    if ctx.author.id == os.getenv('OWNER_ID'):
        return True
    else:
        return False

@bot.event
async def on_ready():
	game = discord.Game("with arch btw")
	await bot.change_presence(status=discord.Status.online, activity=game)
	print('Im Ready')

@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def run(ctx, *, arg):
	ownerState = await is_owner(ctx)
	if ownerState is True:
		await ctx.send("This feature has been disabled because it is too dangerous.")
		#os.system(arg + "&")
		#await ctx.send("Done!")
	else:
		await ctx.send("This feature has been disabled because it is too dangerous.")
		#await ctx.send("You are not authorised to run this command!")

@bot.command()
async def accountAge(ctx, member: discord.Member):
	now = datetime.datetime.utcnow()

	delta = now - member.created_at
	print(delta.days)

	message = "This account is {days} days old.".format(days=delta.days)

	await ctx.send(message)


@bot.command()
async def isDown(ctx, *, arg)
    pass

bot.run(os.getenv('TOKEN'))
