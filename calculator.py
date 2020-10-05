import requests
import json

token = '1164134205:AAEIiVhUKSOKilSTEDgtaoiBx4EvvRpgfOM'

def sendMessage(chat_id,text):

    k_1 = {
        'text':'1'
    }
    k_2 = {
        'text':'2'
    }
    k_3 = {
        'text':'3'
    }
    k_4 = {
        'text':'4'
    }
    k_5 = {
        'text':'5'
    }
    k_6 = {
        'text':'6'
    }
    k_7 = {
        'text':'7'
    }
    k_8 = {
        'text':'8'
    }
    k_9 = {
        'text':'9'
    }
    k_0 = {
        'text':'0'
    }
    k_k = {
        'text':'*'
    }
    k_b = {
        'text':'/'
    }
    k_a = {
        'text':'-'
    }
    k_q = {
        'text':'+'
    }
    k_t = {
        'text':'='
    }
    k_n = {
        'text':'.'
    }

    keyboard = [
        [k_7,k_8,k_9,k_k],
        [k_4,k_5,k_6,k_b],
        [k_1,k_2,k_3,k_a],
        [k_0,k_n,k_t,k_q]
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
sendMessage(chat_id,text)