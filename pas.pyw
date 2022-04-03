import ctypes
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from zmq import device
from values import *

class Security:
    def __init__(self) -> None:
        self.device_state = UNLOCKED
        self.DEVICE_DEFAULT = {}
        self.language_init(LANGUAGE)
        self.bot_init()

    def kitle(self,update: Update, context: CallbackContext) -> None:
        update.message.reply_text(self.DEVICE_DEFAULT.get("close"))
        ctypes.windll.user32.LockWorkStation()
        self.device_state = LOCKED
        self.device_write_state()

    def ac(self,update: Update, context: CallbackContext) -> None:
        self.device_state = UNLOCKED
        update.message.reply_text(self.DEVICE_DEFAULT.get("device_open"))
        self.device_write_state()

    def bot_init(self):
        self.updater = Updater(BOT_KEY)
        self.device_start()
        self.device_state_control()
        self.updater.dispatcher.add_handler(CommandHandler('kitle',self.kitle))
        self.updater.dispatcher.add_handler(CommandHandler('ac',self.ac))
        self.updater.dispatcher.add_handler(CommandHandler('kapat',self.device_shutdown))
        self.updater.start_polling()
        self.updater.idle()
    
    def device_start(self):
        self.updater.bot.send_message(USER_ID,self.DEVICE_DEFAULT.get("open"))
    
    def device_shutdown(self,update: Update, context: CallbackContext) -> None:
        os.system("shutdown /s /t 1")
        update.message.reply_text(self.DEVICE_DEFAULT.get("device_close"))

    def device_unlock_control(self):
        if (self.device_state == LOCKED):
            ctypes.windll.user32.LockWorkStation()
            self.updater.bot.send_message(USER_ID,self.DEVICE_DEFAULT.get("open_prompt"))

    def device_read_state(self):
        with open(FILE_NAME,'r') as file:
            self.device_state = int(file.readline())

    def device_write_state(self):
        with open(FILE_NAME,"w") as file:
            file.write(str(self.device_state))
    
    def device_conf_file_control(self):
        if(not os.path.exists(FILE_NAME)):
            self.device_state = UNLOCKED
            self.device_write_state()
        else:
            self.device_read_state()
    
    def device_state_control(self):
        self.device_conf_file_control()
        self.device_unlock_control()

    def language_init(self,selection):
        if   (selection == TR):
            self.DEVICE_DEFAULT = DEVICE_TR.copy()
        elif (selection == EN):
            self.DEVICE_DEFAULT = DEVICE_EN.copy()
        elif (selection == DU):
            self.DEVICE_DEFAULT = DEVICE_DU.copy()


security = Security()
