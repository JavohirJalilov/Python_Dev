import requests
import json

token = '1164134205:AAEIiVhUKSOKilSTEDgtaoiBx4EvvRpgfOM'

def sendMessage(chat_id,text):

    k_1 = {
        'text':'👉Collect'
    }
    k_2 = {
        'text':'👊Fight'
    }
    k_3 = {
        'text':'✈️Travel'
    }
    k_4 = {
        'text':'🎯Mission'
    }
    k_5 = {
        'text':'🔫Armory'
    }
    k_6 = {
        'text':'🏢Estate'
    }
    k_7 = {
        'text':'👨Recruit'
    }
    k_8 = {
        'text':'💂‍♀️Mercs'
    }
    k_9 = {
        'text':'🗒Menu'
    }
    

    keyboard = [
        [k_1,k_2,k_3],
        [k_4,k_5,k_6],
        [k_7,k_8,k_9]
    ]
    keyboardButton ={
        'keyboard':keyboard
    }
    

    parametr = {
        'chat_id':chat_id,
        'text':text,
        'parse_mode':'HTML',
        'reply_markup':keyboardButton
    }

    response = requests.get(f'https://api.telegram.org/bot{token}/sendMessage', json=parametr)

def getUpdates():
    
    r = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    data = r.json()
    chat_id = data['result'][-1]['message']['chat']['id']
    text = data['result'][-1]['message']['text']

    return chat_id,text

chat_id, text = getUpdates()
sendMessage(chat_id,f'<b>{text}</b>')