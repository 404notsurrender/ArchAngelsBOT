import discord
from discord.ext import commands
from discord import Intents
from discord import Activity, ActivityType, Status

intents = Intents.default()
intents.members = True
intents.typing = False
intents.presences = False
intents.messages = True
intents.message_content = True

# Membuat bot dengan prefix "!"
bot = commands.Bot(command_prefix="!", intents=intents)


# Event yang dipanggil ketika bot Online
@bot.event
async def on_ready():
    print(f'{bot.user.name} is now online!')
        # Set the bot's status to "Watching"
    activity = Activity(name="you", type=ActivityType.watching, details="Watching", state="In the lab")
    await bot.change_presence(status=Status.online, activity=activity)

# Command sederhana
@bot.command()
async def halo(ctx):
    await ctx.send('my name is ian!')

# Command untuk mengetes ping bot
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command ga jelas wkwkkw
@bot.command()
async def menghibur(ctx):
    await ctx.send(f'menghibur, menghibur... orang kesusahan dibilang menghibur')

@bot.command()
async def zahran(ctx):
    await ctx.send(f'are you children?!?')

@bot.command()
async def lol(ctx):
    await ctx.send(f'whehehehe')

# Jalankan bot dengan token
bot.run('[TOKEN]')
