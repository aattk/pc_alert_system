TR = 0 
EN = 1
DU = 2


# * Tanımlamalar ********************************************************************************
USER_ID   = "Telegram_User_ID"      # ! Who to Notify Device Status
BOT_KEY   = "Telegram_Bot_Key"      # ! 
FILE_NAME = "device_state.txt"
LANGUAGE  = EN
# ***********************************************************************************************

LOCKED    = 1
UNLOCKED  = 0

DEVICE_TR = {
            'open'        : 'Cihaz Açıldı.', 
            'close'       : 'Cihaz Kilitlendi.',
            'device_open' : 'Cihaz Kilidi Açıldı.',
            'device_close': 'Cihaz Kapatılmaya Çalışılıyor.',
            'open_prompt' : 'Cihaz Açılmaya Çalışıldı.'
            }

DEVICE_EN = {
            'open'        : 'Device Opened.',
            'close'       : 'Device Locked.',
            'device_open' : 'Device Unlocked.',
            'device_close': 'Trying to Shutdown Device.',
            'open_prompt' : 'Attempted to Open Device.'
            }

DEVICE_DU = {
            'open' : 'Gerät geöffnet.',
            'close' : 'Gerät gesperrt.',
            'device_open' : 'Gerät entsperrt.',
            'device_close': 'Versuche, das Gerät herunterzufahren.',
            'open_prompt' : 'Versucht, Gerät zu öffnen.'
            }                




