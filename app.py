import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)



def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
   # file=context.bot.get_file(update.message.document).download("a.png")
    update.message.reply_text(update.message.text)
#las imagenes tiene que estar alojadas en un servidor
def images(update,context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = 'https://1.bp.blogspot.com/-q79uC26Cous/XovFGGoMUoI/AAAAAAAAWEs/aVpq-5qhd5AXvYxn5vkvJsZRXWR46M4PQCLcBGAsYHQ/s1600/LASC_Valores%2BScrum_Gazafatonario.png')

def main():
 
    updater = Updater("Token", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("imagen",images))
    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
