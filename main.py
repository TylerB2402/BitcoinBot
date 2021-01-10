import discord
import os
from os import environ
import requests
import json

ACCESS_KEY = environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# parameters for get_price request.get
cookies = {
    '__cfduid': 'd47a98994d84973b8bbc5ee67af418a6b1610054701',
    '_ga': 'GA1.2.2110437517.1610054704',
    '_gid': 'GA1.2.1282873142.1610054704',
    '__zlcmid': '122jib3PCUWDQ8l',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.5',
    'ftx-client': 'web',
    'Referer': 'https://ftx.com/trade/BTC-PERP',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
}

params = (
    ('resolution', '60'),
)

# get price from FTX for BTC 
def get_price():
  response = requests.get('https://ftx.com/api/indexes/BTC/candles/last', headers=headers, params=params, cookies=cookies)
  json_data = json.loads(response.text) # parse response into json format/string
  price = json_data['result']['open'] # alter string to retrieve what I need
  return(price)

# parameters for get_percentage_change_1hr request.get & get_percentage_change_24hr
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.5',
    'ftx-client': 'web',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ1c2VyfHR5bGVybGVlYmVkZG93QGhvdG1haWwuY28udWsiLCJpc3MiOiJmdHguY29tIiwibmJmIjoxNjEwMjI5OTI5LCJleHAiOjE2MTI4MjE5ODksImF1ZCI6Imh0dHBzOi8vZnRleGNoYW5nZS5jb20vYXBpLyIsImlhdCI6MTYxMDIyOTk4OSwibWZhIjp0cnVlLCJ3aXRoZHJhd2Fsc0Rpc2FibGVkIjpmYWxzZSwiaW50ZXJuYWxUcmFuc2ZlcnNEaXNhYmxlZCI6ZmFsc2UsInJlYWRPbmx5IjpudWxsfQ.dz8X8TCHjUR2lCjcW4GRwLGyfPgUABBolEXrrYyjQzn7xdxrhSUK906UxDuQa-hvYo_JDLCxhwnwr4yTqGk1j3-v6LrY6WQgb-10HWrIPijrG9-0fqq36z2Mj1LRKqpPW06QfhL8To2_ONqKcl4ZoEV-uitZrUcigNjj_EDECA6M_CO6LiJAbej7H-nAKx_D5CeOTJt1rqCK3lBccirqTVqxWQYQqaeKOAbl1w2OayxKtxM3wZ6TbrLHQZOjGPx5NJKUTjz10Jy69sOx82sn08juLppbDoV1vbrXUiVqe5XCWcaQbT11984TzwNvu66nAneIO55ceVQNedh5i_qBNA',
    'Referer': 'https://ftx.com/trade/BTC-PERP',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
}

cookies = {
    '__cfduid': 'd47a98994d84973b8bbc5ee67af418a6b1610054701',
    '_ga': 'GA1.2.2110437517.1610054704',
    '_gid': 'GA1.2.1282873142.1610054704',
    '__zlcmid': '122jib3PCUWDQ8l',
}

def get_percentage_change_1hr():
 response = requests.get('https://ftx.com/api/futures/BTC-PERP', headers=headers,cookies=cookies)
 json_data = json.loads(response.text) # parse response into json format/string
 perc1hr = json_data['result']['change1h'] # alter string to retrieve what I need
 return(perc1hr)

def get_percentage_change_24hr():
  response = requests.get('https://ftx.com/api/futures/BTC-PERP', headers=headers,cookies=cookies)
  json_data = json.loads(response.text) # parse response into json format/string
  perc24hr = json_data['result']['change24h'] # alter string to retrieve what I need
  return(perc24hr)

@client.event
async def on_message(message):
  if message.content.startswith('!price'):
    price = get_price()
    await message.channel.send(f"""Current price of bitcoin is ${price}""")

  if message.content.startswith('!1hour'):
    perc1hr = get_percentage_change_1hr()
    percalc1hr = "{:.2%}".format(perc1hr) 
    await message.channel.send(f"""Bitcoin price has changed by {percalc1hr} in the past hour.""")

  if message.content.startswith('!24hour'):
    perc24hr = get_percentage_change_24hr()
    percalc24hr = "{:.2%}".format(perc24hr) 
    await message.channel.send(f"""Bitcoin price has changed by {percalc24hr} in the past day.""")

client.run(os.getenv('TOKEN'))