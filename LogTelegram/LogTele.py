import telegram
from .utils import clean
def send_message(message,bot_id="1294069256:AAF6D4XTApkankDYTlDfhOvqT32iKnkrLfo",chat_id="-592682183"):
    telegram_notify = telegram.Bot(str(bot_id))
    try:
        telegram_notify.send_message(chat_id=chat_id, text=message,
                                parse_mode='Markdown')
    except:
        message = clean(message)
        telegram_notify.send_message(chat_id=chat_id, text=message,
                                parse_mode='Markdown')