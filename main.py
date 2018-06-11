from telegram.ext import Updater, CommandHandler
import logging
import config

# Логгер
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Дефолт команда
def start(bot, update):
    update.message.reply_text('Что бы понять кто ты, введи /who_i_am')


def who_i_am(bot, update):
    if update.effective_user.id == config.no_fagot_id:
        update.message.reply_text('хз, но не пидор')
    else:
        update.message.reply_text('ты пидор')

# Функция обработки ошибок
def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

# Точка входа
def main():
    TOKEN = config.token
    REQUEST_KWARGS = {
        'proxy_url': config.proxy
    }

    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("who_i_am", who_i_am))
    dp.add_handler(CommandHandler("help", start))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
