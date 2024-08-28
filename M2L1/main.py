import discord, os, random, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
print(os.listdir('M2L1\Imagenes'))

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def saquenme_de_peru(ctx):
    with open('M2L1\images/sdp.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('M2L1\Imagenes'))
    with open(f'M2L1\Imagenes/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.command()
async def mem_ani(ctx):
    img_name = random.choice(os.listdir('M2L1\eni'))
    with open(f'M2L1\eni/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def animals(ctx):
    img_name = random.chice(os)

bot.run("TOKEN")