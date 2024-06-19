import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define a command handler. This usually takes the two arguments update and context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Send me a message and I will print it here.')

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    print(update.message.text)
    update.message.reply_text(update.message.text)

def main():
    """Start the bot."""
    # Replace 'YOUR_TOKEN' with your actual bot token enclosed in quotes
    application = Application.builder().token("7403487733:AAHMLF5gcpYlR0dvmwOV2YJOAeN79PDnwFM").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non-command i.e. message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
