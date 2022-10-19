from instabot import Bot
bot = Bot()

bot.login(username = "Your Username", password = "Your Password")
bot.send_message("Hello there!", ["Receiver's Username"])