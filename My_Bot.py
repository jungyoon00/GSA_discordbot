import asyncio, discord, re, random
from discord.ext import commands

from my_modules import dice as dc
from my_modules import memory as mr

bot = commands.Bot(command_prefix="#", intents=discord.Intents.all())

@bot.event
async def on_ready():
	print("We have logged in as {0.user}".format(bot))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Error")

@bot.command()
async def hello(ctx):
	await ctx.send("Hello!")

@bot.command()
async def helps(ctx):
	embed = discord.Embed(title = "<HELP>", description = "This is commands for you.")
	embed.add_field(name="#dice", value="c: alone / g: game")
	embed.add_field(name="#calculate", value="This is for math.")
	embed.add_field(name="#code", value="This is for python.")
	embed.add_field(name="#memory", value="Create your own memory file.")
	embed.add_field(name="#add", value="ex) #save key value --> {'key': 'value'}")
	embed.add_field(name="#show", value="See your memory file's contents.")

	await ctx.send(embed=embed)

@bot.command()
async def dice(ctx, mode="c"):
	if str(mode) == "c":
		result = dc.Dice.roll_dice_client()
		text = str(ctx.author.name)+ ": 🎲" + str(result)
		await ctx.send(text)
	elif str(mode) == "g":
		client, bot, win = dc.Dice.roll_dice_game()
		embed = discord.Embed(title = "<DICE>", description = None)
		b = "🎲"+str(b)
		embed.add_field(name = "Bot", value = bot, inline = True)
		c = "🎲"+str(c)
		embed.add_field(name = ctx.author.name, value = client, inline = True)
		win = "Result: " + str(win)
		embed.set_footer(text= win)
		await ctx.send(embed=embed)
	else:
		await ctx.send("Error")

@bot.command()
async def calculate(ctx, get):
	# only int or float / +, -, *, /
	get_str = str(get)
	if re.findall("[a-zA-Z]+", get_str):
		await ctx.send("Error (Please enter only int or float)")
	else:
		value = eval(get_str)
		embed = discord.Embed(title = "<CALCULATE>", description = None)
		embed.add_field(name = get_str, value = value)
		await ctx.send(embed=embed)

@bot.command()
async def code(ctx, code):
	code = str(code)
	try:
		get = eval(code)
		value = ">>> " + str(get)
		embed = discord.Embed(title = "<PYTHON INTERPRETER>", description="Run: Good")
		embed.add_field(name = "Completed", value = value)
	except Exception as E:
		send = ">>> " + str(E)
		embed = discord.Embed(title = "<PYTHON INTERPRETER>", description="Run: Error")
		embed.add_field(name = "Error", value = send)
	await ctx.send(embed=embed)

@bot.command()
async def memory(ctx):
	name = str(ctx.message.author)
	print(name)
	a = mr.Memory.searchFolder(name)
	print(a)
	if not mr.Memory.searchFolder(name):
		print("Folder")
		mr.Memory.makeFolder(name)
	else:
		await ctx.send("This memory folder is already existed")
		return
	if not mr.Memory.searchFile(name):
		print("File")
		mr.Memory.makeFile(name)
	else:
		await ctx.send("This memory file is already existed")
		return
	await ctx.send("Create your memory folder&file successfully")

@bot.command()
async def add(ctx, key, value):
	name = str(ctx.message.author)
	if not mr.Memory.searchFolder(name):
		await ctx.send("Can't save data on non-existing memory folder")
		return
	if not mr.Memory.searchFile(name):
		await ctx.send("Can't save data on non-existing memory file")
		return
	path = mr.Memory.searchFile(name)
	mr.Memory.writeFile(path, str(key), str(value))
	await ctx.send(f"Add a data on your memory --> [{str(key)}, {str(value)}]")

@bot.command()
async def show(ctx, first=1):
	name = str(ctx.message.author)
	if not mr.Memory.searchFolder(name):
		await ctx.send("Can't see data on non-existing memory folder")
		return
	if not mr.Memory.searchFile(name):
		await ctx.send("Can't see data on non-existing memory file")
		return
	path = mr.Memory.searchFile(name)
	memory_lines = mr.Memory.readFile(path)
	print("M:", memory_lines)
	amount = len(list(memory_lines.keys()))
	if amount < 20:
		state = "Good"
	elif amount < 50:
		state = "Warning"
	elif amount < 80:
		state = "Bad"
	else:
		state = "Full"
	embed = discord.Embed(title = f"<{name}'s Memory>", description=f"Lines: {amount} | Status: {state}")
	keys = list(memory_lines.keys())
	processed_keys = keys[(first-1):]
	if len(processed_keys) > 20:
		repeat = 20
		end = f"More +{amount - 20} keys"
	else:
		repeat = len(processed_keys)
		end = "End"
	for index in range(repeat):
		key = processed_keys[index]
		embed.add_field(name=str(key), value=str(memory_lines[key]), inline=False)
	embed.add_field(name=f"PATH: .../memories/{name}/{name}.csv", value=end)

	await ctx.send(embed=embed)

@bot.command()
async def delete(ctx, key):
	name = str(ctx.message.author)
	if not mr.Memory.searchFolder(name):
		await ctx.send("Can't delete data on non-existing memory folder")
		return
	if not mr.Memory.searchFile(name):
		await ctx.send("Can't delete data on non-existing memory file")
		return
	path = mr.Memory.searchFile(name)
	remove = mr.Memory.deleteFile(path, str(key))
	await ctx.send(f"Delete a data on your memory --> Memory Key: {str(key)} / Value: {str(remove)}")

# Don't worry. This function is just TEMPORATURE.
@bot.command()
async def destroy(ctx):
	pass



bot.run("MTA4MzYxODg4NzEwODY2MTMwOA.GW9VzH.Shb8FLb9VExvOQGAUXfJjyVOa03ROCi3UQKMtE")
