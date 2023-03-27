from gpt import gpt
from webex_bot.webex_bot import WebexBot

# Create a Bot Object
bot = WebexBot("YOUR_ACCESS_TOKEN")

#Clear default help command
bot.commands.clear()

# Add new commands for the bot to listen out for.
bot.add_command(gpt())

#Set new command as default
bot.help_command = gpt()

# Call `run` for the bot to wait for incoming messages.
bot.run()