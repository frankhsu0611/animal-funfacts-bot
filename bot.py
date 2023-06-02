import os
import discord
from dotenv import load_dotenv
import requests
from chatgpt import do

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name='fact', description="fun facts about animals")
async def animal_funfacts(interaction,
                animal=discord.Option(str, description='animal', required=False, default='')
    ):
    await interaction.response.defer()
    resp, img = do(animal)
    embed = discord.Embed()
    embed.set_image(url=img)
    embed.description = resp
    await interaction.followup.send(embed = embed)

@bot.slash_command(name='test', description='test')
async def test(ctx):
    await ctx.respond('test successful')

print('Bot is running...')
bot.run(TOKEN)