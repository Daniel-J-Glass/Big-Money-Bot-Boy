import os
import sys
sys.path.append('../')

from bfxapi import Client, Order

API_KEY=os.getenv("BFX_KEY")
API_SECRET=os.getenv("BFX_SECRET")

bfx = Client(
  API_KEY='
  logLevel='DEBUG'
)



# def sell(client, price):


@bfx.ws.on('order_snapshot')
async def cancel_all(data):
  await bfx.ws.cancel_all_orders()

@bfx.ws.on('order_confirmed')
async def trade_completed(order):
  print ("Order confirmed.")
  print (order)
  ## close the order
  # await order.close()
  # or
  # await bfx.ws.cancel_order(order.id)
  # or
  # await bfx.ws.cancel_all_orders()


@bfx.ws.on('error')
def log_error(err):
  print ("Error: {}".format(err))

@bfx.ws.on('new_candle')
def log_candle(candle):
#should i buy? \(owo)/
  print ("New candle: {}".format(candle))
  arr = candle
  print(arr['open'])
  if(arr['open'] < 150.5) :
    async def submit_order(auth_message):
        print('fuck')
        await bfx.ws.submit_order('tBTCUSD', 1, 3, Order.Type.EXCHANGE_LIMIT)
  # print(arr[3])

# @bfx.ws.on('new_trade')
# def log_trade(trade):
#   print ("New trade: {}".format(trade))


# @bfx.ws.on('authenticated')
# async def submit_order(auth_message):
#   await bfx.ws.submit_order('tBTCUSD', 1, 3, Order.Type.EXCHANGE_LIMIT)


# If you dont want to use a decorator
# ws.on('authenticated', submit_order)
# ws.on('error', log_error)

# You can also provide a callback
# await ws.submit_order('tBTCUSD', 0, 0.01,
# 'EXCHANGE MARKET', onClose=trade_complete)

async def start():
  await bfx.ws.subscribe('candles', 'tETHUSD', timeframe='1m')
  # await bfx.ws.subscribe('trades', 'tETHUSD')

bfx.ws.on('connected', start)
bfx.ws.run()
