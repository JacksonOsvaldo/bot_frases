import discord
import requests
import json

from deep_translator import GoogleTranslator
from decouple import config

client = discord.Client(intents=discord.Intents.default())

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = GoogleTranslator(source='auto', target='pt').translate(text=json_data[0]['q']) + "\n – " + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspirar'):
    quote = get_quote()
    await message.channel.send(quote)

client.run(config('TOKEN'))