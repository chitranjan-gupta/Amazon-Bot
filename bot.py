from re import sub, IGNORECASE, findall
from requests import Session
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types, executor
from logging import basicConfig, INFO
from os import environ
import asyncio

BOT_TOKEN = environ.get('BOT_TOKEN') # Token used by telegram to authorize the use of bot; replace with your token
TIME = 60 * 60 # Check the price every given seconds; change the time according to your need
url = "https://www.amazon.in/OnePlus-Bluetooth-Wireless-Earphones-Bombastic/dp/B0B3MNYGTW" #default link
status = False # Status of tracker 
prices = [] # array of price changes

def CheckUrl(text,type):
  reg = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = findall(reg,text)
  if type == "c":
    if(url):
      return True
    else:
      return False
  else:
    if(url):
      return url[0][0]

def Telegram():
  bot = Bot(token=BOT_TOKEN)
  disp = Dispatcher(bot=bot)

  @disp.message_handler(commands=['start'])
  async def send_welcome(message: types.Message):
    await message.answer(
      f"""Hi! {message['from']['first_name']}\nWelcome You to Amazon Product Price Tracker Bot. You can track the price of Amazon Product by sending the link.\n"""
    )

  @disp.message_handler(commands=['tstart'])
  async def send_start(message: types.Message):
    global status
    if status == False:
      status = True
      await message.answer("Started Tracking...")
      t1 = asyncio.create_task(Check(message=message))
      await t1
    else:
      await message.answer("Tracking is already running")

  @disp.message_handler(commands=['tstop'])
  async def send_stop(message: types.Message):
    global status
    if status == True:
      status = False
      await message.answer("Stopped Tracking.")
    else:
      await message.answer("Tracking is already stopped.")

  @disp.message_handler(commands=['help'])
  async def send_help(message: types.Message):
    await message.reply("Type /start to Interact With The Bot")
  
  @disp.message_handler()
  async def check(message: types.Message):
    global status, url, prices
    if status == False and CheckUrl(message['text'],"c"):
      url = CheckUrl(message['text'],"n")
      prices.clear()
      await message.answer(
        "Link is Added to tracking\n To Start Tracking send command /tstart \nand to Stop Tracking send command /tstop"
      )
  
  executor.start_polling(disp)

async def Request(url):
    session = Session()
    session.headers.update({
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language':'en-US, en;q=0.5'
    })
    data = session.get(url)
    if data.status_code == 200:
        soup = BeautifulSoup(data.content,'lxml')
        div = soup.find("div",attrs={"id":'corePrice_desktop'})
        pricediv = div.find("span",attrs={"class":"apexPriceToPay"})
        pricespan = pricediv.find("span",attrs={"class":"a-offscreen"})
        currentprice = float(sub("[₹,$]","",pricespan.string,flags=IGNORECASE))
        return currentprice
    else:
        print("Error")
        return 0

async def Check(message: types.Message):
  global status, prices, TIME, url
  while status == True:
    currentprice = await Request(url)
    if len(prices) >= 1:
      if currentprice < prices[-1]:
        prices.append(currentprice)
        await message.answer("Current Price: ₹" + str(currentprice))
    else:
      prices.append(currentprice)
      await message.answer("Current Price: ₹" + str(currentprice))
    await asyncio.sleep(TIME)

if __name__ == '__main__':
  basicConfig(level=INFO)
  Telegram()
