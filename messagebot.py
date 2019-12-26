#!/usr/bin/python
import datetime 
import telepot
import json
import time
import requests 
import os 
import glob
import shlex
import shutil
import signal
import subprocess
import sys
import threading
import time
import traceback
from telepot.loop import MessageLoop


cred = json.load(open('config.json', 'r'))
bot = telepot.Bot(cred['telegram']['token'])

# Check IDs and send notifications to users
for owner_id in cred['telegram']['owner_ids']:
    bot.sendMessage(owner_id, str('Hello there, I\'m back online!'))

def handle(msg): 
    # chat_id is the id of user messaging the bot
    chat_id = msg['chat']['id'] 
    command = msg['text']
    print('Got command: %s' % command) 

# Listen for valid messages

# Send owners photo snapshot
    if command == '/snapshot':
        if chat_id in cred['telegram']['owner_ids']:
            for owner_id in cred['telegram']['owner_ids']:
                bot.sendMessage(owner_id, 'Owner ID: '+str(chat_id) + ' requested a snapshot at ' +str(datetime.datetime.now()))
                # Command for snapshot


        else:
            bot.sendMessage(chat_id, "Sorry, I don't know you")
            for owner_id in cred['telegram']['owner_ids']:
                bot.sendMessage(owner_id, str(chat_id) + ' tried to send the /snapshot command')

        print('/snapshot command sent to bot')

# Send owners any requests to be added
    elif command == '/apply':
        if chat_id in cred['telegram']['owner_ids']:
            for owner_id in cred['telegram']['owner_ids']:
                bot.sendMessage(owner_id, 'Owner ID: '+str(chat_id) + ' requested /apply. Already an owner.')
        else:
            bot.sendMessage(chat_id, "Sorry, I don't know you")
            for owner_id in cred['telegram']['owner_ids']:
                bot.sendMessage(owner_id, str(chat_id) + ' is requesting to be added.')

        print('/apply command sent to bot')


# Send users timestamp
    elif command == '/time':
        if chat_id in cred['telegram']['owner_ids']:
            for owner_id in cred['telegram']['owner_ids']:
                bot.sendMessage(owner_id, 'Owner ID: '+str(chat_id) + ' requested /time. Now is '+str(datetime.datetime.now()))
        else:
            bot.sendMessage(chat_id, "Sorry, I don't know you")
            for owner_id in cred['telegram']['owner_ids']:
                bot.sendMessage(owner_id, str(chat_id) + ' tried to message the bot')

        print('/time command sent to bot')


# Send users recent video
    elif command == '/video':
        if chat_id in cred['telegram']['owner_ids']:
            for owner_id in cred['telegram']['owner_ids']:
                bot.sendMessage(owner_id, 'Owner ID: '+str(chat_id) + ' requested a video at ' +str(datetime.datetime.now()))
                # Command for video


        else:
            bot.sendMessage(chat_id, "Sorry, I don't know you")
            for owner_id in cred['telegram']['owner_ids']:
                bot.sendMessage(owner_id, str(chat_id) + ' tried to send the /video command')


        print('/video command sent to bot')



# Send response for unrecognized commands
    else:
        if chat_id in cred['telegram']['owner_ids']:
            for owner_id in cred['telegram']['owner_ids']:
                bot.sendMessage(owner_id, 'Owner ID: '+str(chat_id) + ' inputted an unrecognized command: '+ command)
        else:
            bot.sendMessage(chat_id, "Sorry, I don't know you")
            for owner_id in cred['telegram']['owner_ids']:
                bot.sendMessage(owner_id, str(chat_id) + ' tried to message the bot but used unrecongized command')
        print('Unrecognized command sent to bot')

# adapt the following to the bot_id:bot_token

bot = telepot.Bot(cred['telegram']['token'])  
MessageLoop(bot, handle).run_as_thread() 
print('I am listening ...')

while True:
    time.sleep(10)
