# WaltonMiningNotification

This is a simple python script that sends you a Telegram Message when you find another Block.
How is it working?
It is checking your current mined Blocks via Waltonchain API at the start.
After 10 seconds it checks if the amount of your mined blocks increased.
If this is the case you will receive a message in your telegram bot channel.