## Create a Telegram Bot

A bot is a software application programmed to perform certain tasks. The robots are automated, which means that they operate according to their instructions without a human user needing to start them. Bots often mimic or replace the behaviour of a human user.

To create a Telegram Bot using Python, we need to go through some steps to get a telegram bot API from the BotFather account on Telegram. BotFather is simply s Bot which helps in creating more bots by providing a unique API. So before using python to create our Telegram bot, we need to go through some steps to get the API.

### Steps to Get the Telegram Bot API

First, create an account on telegram if you don’t have an account. After making your account search for BotFather, which is an official telegram bot that provides API to create more bots. When you will open the chat just write /start and send. The BatFather will reply you with a long text without reading the text you can type **Newbot**.

Now it will reply you again with a long text, asking about a good name for you Telegram bot. You can write any name on it. Now the next step is to give a username to your bot which should be in a format Namebot or Name_bot. And the main thing to notice in this step is that your username should be a unique one, it should not match any other username all around the world.

Now after typing a unique username, it will send you an API key between a long message, you need to copy that username and get started with Python.

### Telegram Bot with Python

Now, we have the API key to build our telegram bot, the next step is to install a package known as telegram, which can be easily installed by using the pip command in your command prompt or terminal;

```py
pip install python-telegram-bot
```

After successfully installing the package, we import the required packages and get started to make a Telegram Bot with Python. We only need the telegram package for this task.

Run the code and write /hello in you your telegram messenger to your telegram bot. It will reply with the text “Hello World”.

### Summary

I hope you liked this project on building a Telegram Bot with Python.