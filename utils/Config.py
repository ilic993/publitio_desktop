import configparser
import os

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.settings_file = 'settings.ini'

        # Check if the INI file exists
        if os.path.exists(self.settings_file):
            print("INI file exists.")
        else:
            self.config['UserSettings'] = {
                'api_key': '',
                'api_secret': '',
                'theme': 'System'
            }

            with open('settings.ini', 'w') as configfile:
                self.config.write(configfile)

    def checkKeys(self):
        self.config.read(self.settings_file)
        api_key = self.config.get('UserSettings', 'api_key')
        api_secret = self.config.get('UserSettings', 'api_secret')

        if api_key == '' or api_secret == '':
            return False

        # Check validity of keys

        return True

    def readSetting(self, key):
        self.config.read(self.settings_file)
        return self.config.get('UserSettings', key)

    def changeSetting(self, key, value):
        self.config.set('UserSettings', key, value)

        with open(self.settings_file, 'w') as configfile:
            self.config.write(configfile)
