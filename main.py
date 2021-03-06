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

# parameters for get_percentage_change_1hr request.get & get_percentage_change_24hr & get_percentage_change_day
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.5',
    'ftx-client': 'web',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ1c2VyfHR5bGVybGVlYmVkZG93QGdtYWlsLmNvbSIsImlzcyI6ImZ0eC5jb20iLCJuYmYiOjE2MTA0OTAyMzEsImV4cCI6MTYxMDU3NjY5MSwiYXVkIjoiaHR0cHM6Ly9mdGV4Y2hhbmdlLmNvbS9hcGkvIiwiaWF0IjoxNjEwNDkwMjkxLCJtZmEiOmZhbHNlLCJ3aXRoZHJhd2Fsc0Rpc2FibGVkIjpmYWxzZSwiaW50ZXJuYWxUcmFuc2ZlcnNEaXNhYmxlZCI6ZmFsc2UsInJlYWRPbmx5IjpudWxsfQ.qZItDzPKRelo6qfoaVlWy9wkWWf_tb2Ky_97cRps7cAKBeGB_M4heIFiA0tWhKlsJFRyGR7QwOMmYFq_LWcyIWp6dDZwSKDWNjcC2obzsqKhsA09VG6CRHGixSZoOXLUccE2XfbRWOeXp8BDZLylfmU6xHKuRPn2qbI2i5yXYpqMA4LhAGTTbzFHWJ4Ue2zpQdgwAjNXW4gmJs6WcvkHXu-5psDS7fURU8u5IkDA8ZM5GHS9TZ45Twu1epb2EBx_gwI_cfaqyk2gSgO3GKhGw7KgnLao9rBKF1KvVEbUd6sZx54FTZwOSm8LPNzj7Dbxzr6oagjjVDrHU0yAex6yLg',
    'Referer': 'https://ftx.com/trade/BTC-PERP',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
}

cookies2 = {
    '__cfduid': 'd47a98994d84973b8bbc5ee67af418a6b1610054701',
    '_ga': 'GA1.2.2110437517.1610054704',
    '_gid': 'GA1.2.1282873142.1610054704',
    '__zlcmid': '122jib3PCUWDQ8l',
}

def get_percentage_change_1hr():
 response = requests.get('https://ftx.com/api/futures/BTC-PERP', headers=headers2,cookies=cookies2)
 json_data = json.loads(response.text) # parse response into json format/string
 perc1hr = json_data['result']['change1h'] # alter string to retrieve what I need
 return(perc1hr)

def get_percentage_change_24hr():
  response = requests.get('https://ftx.com/api/futures/BTC-PERP', headers=headers2,cookies=cookies2)
  json_data = json.loads(response.text) # parse response into json format/string
  perc24hr = json_data['result']['change24h'] # alter string to retrieve what I need
  return(perc24hr)

def get_percentage_change_day():
  response = requests.get('https://ftx.com/api/futures/BTC-PERP', headers=headers2,cookies=cookies2)
  json_data = json.loads(response.text) # parse response into json format/string
  percday = json_data['result']['changeBod'] # alter string to retrieve what I need
  return(percday)

cookies3 = {
    '__cfduid': 'd47a98994d84973b8bbc5ee67af418a6b1610054701',
    '_ga': 'GA1.2.2110437517.1610054704',
    '_gid': 'GA1.2.1282873142.1610054704',
    '__zlcmid': '122jib3PCUWDQ8l',
}

headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.5',
    'ftx-client': 'web',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ1c2VyfHR5bGVybGVlYmVkZG93QGdtYWlsLmNvbSIsImlzcyI6ImZ0eC5jb20iLCJuYmYiOjE2MTA0OTAyMzEsImV4cCI6MTYxMDU3NjY5MSwiYXVkIjoiaHR0cHM6Ly9mdGV4Y2hhbmdlLmNvbS9hcGkvIiwiaWF0IjoxNjEwNDkwMjkxLCJtZmEiOmZhbHNlLCJ3aXRoZHJhd2Fsc0Rpc2FibGVkIjpmYWxzZSwiaW50ZXJuYWxUcmFuc2ZlcnNEaXNhYmxlZCI6ZmFsc2UsInJlYWRPbmx5IjpudWxsfQ.qZItDzPKRelo6qfoaVlWy9wkWWf_tb2Ky_97cRps7cAKBeGB_M4heIFiA0tWhKlsJFRyGR7QwOMmYFq_LWcyIWp6dDZwSKDWNjcC2obzsqKhsA09VG6CRHGixSZoOXLUccE2XfbRWOeXp8BDZLylfmU6xHKuRPn2qbI2i5yXYpqMA4LhAGTTbzFHWJ4Ue2zpQdgwAjNXW4gmJs6WcvkHXu-5psDS7fURU8u5IkDA8ZM5GHS9TZ45Twu1epb2EBx_gwI_cfaqyk2gSgO3GKhGw7KgnLao9rBKF1KvVEbUd6sZx54FTZwOSm8LPNzj7Dbxzr6oagjjVDrHU0yAex6yLg',
    'Referer': 'https://ftx.com/trade/BTC-PERP',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
}

params3 = (
    ('showAvgPrice', 'true'),
)

def get_current_pnl():
 session = requests.Session()
 response = session.get('https://ftx.com/api/positions', headers=headers3,params=params3,cookies=session.cookies)
 json_data = json.loads(response.text) # parse response into json format/string
 # currentpnl = json_data['result'][0]['recentPnl'] # alter string to retrieve what I need
 return(json_data)

#def get_current_pnl():
 #response = requests.get('https://ftx.com/api/positions', headers=headers3,params=params3,cookies=cookies3)
 #json_data = json.loads(response.text) # parse response into json format/string
 #currentpnl = json_data['result'][0]['recentPnl'] # alter string to retrieve what I need
 #return(currentpnl)

@client.event
async def on_message(message):
  if message.content.startswith('!BBHelp'):
    await message.channel.send("List of commands are !price (gets current price), !1hour (gets percentage difference for the last hour), !24hour (gets percentage difference for the last 24 hours), !day (gets percentage difference from the start of the day (00:00))")

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
    await message.channel.send(f"""Bitcoin price has changed by {percalc24hr} in the past 24 hours.""")

  if message.content.startswith('!day'):
    percday = get_percentage_change_day()
    percalcday = "{:.2%}".format(percday) 
    await message.channel.send(f"""Bitcoin price has changed by {percalcday} in the past day (from 00:00).""")

  if message.content.startswith('!pnl'):
    currentpnl = get_current_pnl()
    await message.author.send(f"""Your PnL is currently at US${json_data}.""")

client.run(os.getenv('TOKEN'))