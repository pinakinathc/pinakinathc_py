# -*- coding: utf-8 -*- 
# author: pinakinathc

import os
import hashlib
import smtplib
import json
import getpass

class SendEmail():
    def __init__(self):
        self.smtpObj = smtplib.SMTP('smtp.gmail.com', 587) # Connect to google's smtp server

        # Check if access token available
        this_dir, this_filename = os.path.split(__file__)
        self.token_path = os.path.join(this_dir, 'data', 'access_token.json')

        if not os.path.exists(self.token_path):
            print ('Could not find access file.')
            self.setup()
        try:
            access_token = json.load(open(self.token_path, 'r'))
        except:
            print ('Access token seems to be corrupt. Please contact pinakinathc if this persists.')
            self.setup()
            access_token = json.load(open(self.token_path, 'r'))

        self.bot_email = access_token['bot_email']
        bot_key = access_token['bot_key']

        try:
            self.smtpObj.ehlo()
            self.smtpObj.starttls()
            self.smtpObj.login(self.bot_email, bot_key)
        except Exception as err:
            raise ValueError('Failed while authenticating using bot_email or bot_password. Error message: {}'.format(err))

    def setup(self):
        print ('Welcome to the setup Creator!')
        bot_email = input ('Please enter Bot Email: ')
        bot_raw = getpass.getpass(prompt='Please enter Bot Password: ')
        # bot_raw = input ('Please enter Bot Password:')
        bot_key = hashlib.sha224(str.encode(bot_raw)).hexdigest() # Calculate SHA224 hash
        os.makedirs(os.path.split(self.token_path)[0], exist_ok=True)
        json.dump({'bot_email': bot_email, 'bot_key': bot_key}, open(self.token_path, 'w'))
        print ('Setup complete.')

    def send(self, sender_email, message):
        self.smtpObj.sendmail(self.bot_email, sender_email, 'Subject: Update from pinakinathc.bot-1\n\n{}'.format(message))

    def close():
        self.smtpObj.close()

