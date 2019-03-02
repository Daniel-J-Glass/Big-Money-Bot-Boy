import os
import sys
sys.path.append('../')

from bfxapi import Client

bfx = Client(
  logLevel='DEBUG'
)

@bfx.ws.on('error')
def log_error(err):
  print ("Error: {}".format(err))

@bfx.ws.on('new_candle')
def log_candle(candle):
#should i buy? \(owo)/

  print ("New candle: {}".format(candle))

@bfx.ws.on('new_trade')
def log_trade(trade):
  print ("New trade: {}".format(trade))

async def start():
  await bfx.ws.subscribe('candles', 'tETHUSD', timeframe='1m')
  await bfx.ws.subscribe('trades', 'tETHUSD')

bfx.ws.on('connected', start)
bfx.ws.run()
