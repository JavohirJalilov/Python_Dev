import requests
import json

token = '1362747013:AAH6-Eq0AgF973rHP_8g59FdRjCGhFpuXdY'

def sendMessage(chat_id,text):
    kb1 = {
        'text':'Javohir'
    }
    kb2 = {
        'text':"Yoqubbek"
    }
    kb3 = {
        'text':'Rustam'
    }
    kb4 = {
        'text':'Jamshid'
    }

    keyboard = [
        [kb4,kb2],
        [kb3,kb1]
    ]

    replykeyboard ={
        'keyboard':keyboard
    }
    parametr = {
        'chat_id':chat_id,
        'text':text,
        'parse_mode':'HTML',
        'reply_markup':replykeyboard
    }
    response = requests.get(f'https://api.telegram.org/bot{token}/sendMessage', json=parametr)

def getUpdates():
    
    r = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    data = r.json()
    chat_id = data['result'][-1]['message']['chat']['id']
    text = data['result'][-1]['message']['text']
    return chat_id, text

def get_message():

    re = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    update_id = re.json()['result'][-1]['update_id']
    return update_id

def ismuz():

    chat_id, text = getUpdates()

    res = requests.get(f'https://ismlar.com/search/{text}')
    s = res.text
    
    x = s.index('class="mb-3"')
    y = s.index('</h3>',x)

    x += 111 + len(text)
    tur = s[x:y]

    if text == '/start':
        mano = 'Marhamt! Ismni kiriting.'
        return mano 

    elif tur == 'Исм маъносини топиш учун буюртма бериш':
        mano = 'Afsus, Bunday ism hozircha bizda mavjud emas'
        return mano

    else:
        i = s.index('class="text-size-5"')
        l = s.index('</p>',i)
        i = i+20

        k = s.index('class="fas fa-tag"')
        j = s.index('</a>',k)
        k+=23
        tur = s[k:j]

        mano = s[i:l]
        return f'<u>{tur}</u>'+"\n"+mano

last_update_id = -1

while True:
    update_id = get_message()
    chat_id, text = getUpdates()

    print(f'last: {last_update_id} = id: {update_id}')
    if last_update_id != update_id:
        sendMessage(chat_id,f'<b>{ismuz()}</b>')
        last_update_id = update_id
