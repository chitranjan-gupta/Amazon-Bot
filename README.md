# Amazon Product Price Tracking Telegram Bot.
## Description
Weary about continuously checking the decrease in the price of the product you want to purchase from Amazon? Do not worry; The Amazon bot will help you in achieving it. The Amazon bot will check the price every 24 hours. And if the price has decreased. Then it will send a notification on telegram.
## Run Live on Telegram
* [Amazon Bot](https://telegram.dog/AmazonPriceRangeBot)
## Installation Guide
### Prerequisites
* [git](https://git-scm.com/)
* [python](https://www.python.org/) (3.7 or higher)
### Local Setup
> The setup is given here is for a linux environment.
* Clone the project
```bash
$ git clone https://github.com/chitranjan01/Amazon-Bot.git
```
* Go to the project directory
```bash
$ cd Amazon-Bot
```
* Create and activate virtual environment
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```
* Install python dependencies
```bash
$ pip3 install -U -r requirements.tt
```
### Environment Variables
Properly setup the enviroment variables or populate bot.py with the values. Setting the environment variables is advised as some of the values are sensitive data, and should be kept secret. 
* ```BOT_TOKEN``` - Telegram Bot Token. Obtain your bot token from [Bot Father](https://t.me/BotFather).
> To know how to add the token visit [wiki](https://github.com/chitranjan01/Amazon-Bot/wiki/Installation#linux).
### Run the bot
```bash
$ python3 bot.py
```
Now go and ```/start``` the bot. If everything went fine, the bot will respond with welcome message.
## Supported commands
* ```/start``` - Command to start the bot or check whether the bot is alive.
* ```/link url``` - Replace the url with the Amazon Product Link and send the command to add the link to tracker.
* ```/tstart``` - Command to start the tracker.
* ```/tstop``` - Command to stop the tracker.
## Dependencies
* BeautifulSoup
* requests
* aiogram
* lxml
## Supported Environment
* [Linux](https://github.com/chitranjan01/Amazon-Bot/wiki/Installation#linux)
* [Windows](https://github.com/chitranjan01/Amazon-Bot/wiki/Installation#windows)
* [Android (Termux)](https://github.com/chitranjan01/Amazon-Bot/wiki/Installation#android)
## Documentation
Read the documentation on [wiki](https://github.com/chitranjan01/Amazon-Bot/wiki).
## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
