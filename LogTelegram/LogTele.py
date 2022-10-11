import telegram
from .utils import clean
def send_message(message,bot_id="5774401441:AAEXF28JUJBvM-257dBg2pWMK9WBItWIVeE",chat_id="-879722743"):
    telegram_notify = telegram.Bot(str(bot_id))
    try:
        telegram_notify.send_message(chat_id=chat_id, text=message,
                                parse_mode='Markdown')
    except:
        message = clean(message)
        telegram_notify.send_message(chat_id=chat_id, text=message,
                                parse_mode='Markdown')