import requests
import json
currency = 'RUB'
l_currency = ['EUR','USD','GBP','JPY']

pyload = {'base':currency,'symbols':l_currency}
r = requests.get('https://api.exchangeratesapi.io/latest',params = pyload)

data = r.json()
print(r.url)
dic = data['rates']

for key,value in dic.items():
    print(f'100 RUB (Ruble) {100*value} {key} ga teng')
#print(data['rates']['JPY'])

#Rubl Russia, RUB
#Yevro Yevropa, EUR
#Dollor AQSH, USD
#Funt  britaniya, GPB
#Yen Yaponiya, JPY