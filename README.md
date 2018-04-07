# WaltonMiningNotification

This is a simple python script that sends you a Telegram Message when you find another Block.
## How does it work?
It is checking your current mined Blocks via Waltonchain API at the start.
After 10 seconds it checks if the amount of your mined blocks increased.
If this is the case you will receive a message in your telegram bot channel.



## Installation

This is a python script, so make sure you installed python. I use this script on my raspberry pi with installed Raspbian.

### Prerequisites

What things you need to install the software and how to install them

```
sudo pip install requests
```

### Telegram Setup
```
Please look at this link how to setup a telegram bot and how to get your chatID + telegram api key
https://www.forsomedefinition.com/automation/creating-telegram-bot-notifications/
```

