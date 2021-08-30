import telegram
import requests
import time
import datetime

class LogTelegram():
    def __init__(self,bot_id,chat_id):
        self.bot = bot_id
        self.chat_id = chat_id

    def send_message(self,message):
        telegram_notify = telegram.Bot(str(self.bot))
        telegram_notify.send_message(chat_id=self.chat_id, text=message,
                                parse_mode='Markdown')

if __name__ == "__main__":
    log = LogTelegram(bot_id="1294069256:AAF6D4XTApkankDYTlDfhOvqT32iKnkrLfo",chat_id="-592682183")
    log.send_message('test1')